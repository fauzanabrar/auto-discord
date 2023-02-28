import re
import time

import nopecha
import asyncio

from playwright.async_api import async_playwright, expect
from threading import Thread
import json
import requests


def get_api_key(auth, channel_id, order=0):
    print("Get Nopecha API Key")
    header = {'authorization': auth}
    r = requests.get(f'https://discord.com/api/v8/channels/{channel_id}/messages', headers=header)

    if order != 0:
        jsonn = json.loads(r.text)

        return jsonn[0:order]

    jsonn = json.loads(r.text)
    key = jsonn[0]['content']
    print("Get key:", key)
    return key


async def nopecha_solver_async(type, task, image_urls):
    # nopecha.api_key = "spkj3unz8pr44jrw"
    print("Try Solve chaptcha")
    # solve a recognition challenge
    clicks = nopecha.Recognition.solve(
        type=type,
        task=task,
        image_urls=image_urls,
    )

    # return the grids to click
    return clicks


async def get_task_and_img_async(locator):
    inner = locator.locator(
        ".prompt-text").inner_text()
    task_images = locator.locator(".task-image")
    img_urls = []
    task = await inner
    count = await task_images.count()
    print(count)
    regex = "(https?\:\/[^\"\'\n\<\>\;\)\s]*)|(www?\.[^\"\'\n\<\>\;\s]*)|([^\s\&\=\;\,\<\<\>\"\'\(\)]+\/[\w\/])([^\"\'\n\;\s]*)|((?<!\<)[\/]+[\w]+[^\'\"\s\<\>]*)"
    for i in range(count):
        attr = await task_images.nth(i).locator(".image-wrapper").locator(".image").get_attribute("style")
        img_url = re.findall(regex, attr)[0][0]
        img_urls.append(img_url)

    return (task, img_urls)


async def solve_hcaptcha_async(iframe_locator):
    print("Solving the captcha ....")
    task, img_urls = await get_task_and_img_async(iframe_locator)
    print("Task and image get it! ")
    solve = await nopecha_solver_async("hcaptcha", task, img_urls)
    for i in range(len(solve)):
        if solve[i]:
            await iframe_locator.get_by_role("button", name=f"Challenge Image {i + 1}").click()
    try:
        await iframe_locator.get_by_role("button", name="Submit Answers").click()
        print("Solve Captcha berhasil !")
    except:
        await iframe_locator.get_by_role("button", name="Next Challenge").click()
        await solve_hcaptcha_async(iframe_locator)


async def login_discord_auth(auth, url, page):
    print("Try Login", auth, url)
    # login discord with auth token
    sauth = f'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{auth}"`'
    await page.wait_for_selector(
        '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]',
        timeout=0)
    await page.evaluate(sauth)
    await page.reload(timeout=0)

    try:
        await page.wait_for_timeout(10 * 1000)
        await expect(page).to_have_url(url)
    except:
        # await page.get_by_role("button", name="Authorize").click(timeout=30 * 1000)
        await page.locator('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]').click(
            timeout=10 * 1000)
        print("Login Success", auth, url)


async def run_vote(auth, url, browser):
    print("Running vote1", auth, url)
    try:
        context = await browser.new_context()
        page = await context.new_page()
        page.set_default_timeout(15 * 1000)
        await page.goto(url, timeout=0)

        try:
            await expect(page.locator("text=Login to vote")).to_have_count(0)
        except:
            # detect login to vote
            tes = await page.wait_for_selector('//*[@id="chakra-modal-13"]/div[2]/a[1]')
            await tes.click(timeout=5 * 1000)

            try:
                await page.wait_for_timeout(15 * 1000)
                await expect(page).to_have_url(url)
                print(page.url)
            except:
                await login_discord_auth(auth, url, page)

        await page.wait_for_url(url)
        await page.wait_for_timeout(13 * 1000)
        await page.get_by_role("button", name="Vote").click(timeout=0)
        await page.wait_for_timeout(5 * 1000)
        print("Vote clicked!", auth, url)

        a = page.locator("div > iframe")
        count = await a.count()
        for i in range(count):
            frame = a.nth(i).frame_locator(":scope")
            if await a.nth(i).get_attribute("title") == "Main content of the hCaptcha challenge":
                try:
                    await solve_hcaptcha_async(frame)
                except Exception as e:
                    print(e)
                    print("Nothing captcha !")

        print("Just wait", auth, url)
        await page.wait_for_timeout(10 * 1000)
        print("----------------------------- Vote berhasil -----------------------------")
        await context.close()
    except Exception as e:
        await context.close()
        print("Error run vote:", e)
        print("Run Again !!")
        await run_vote(auth, url, browser)


async def run_vote2(auth, url, browser):
    print("Running vote2", auth, url)
    try:
        context = await browser.new_context()
        page = await context.new_page()
        page.set_default_timeout(20 * 1000)
        await page.goto(url, timeout=0)
        print("visit")
        # click vote
        tes = page.locator("text=Log in")
        await tes.nth(1).click()
        await page.wait_for_timeout(3 * 1000)
        print("clicked")
        try:
            await expect(page).to_have_url(url)
        except:
            await login_discord_auth(auth, url, page)
            print("Login success", auth, url)

        await page.wait_for_url(url)
        await page.locator("text=Upvote").nth(1).click()
        try:
            await expect(page).to_have_url(f"{url}/thanks")
        except:
            try:
                # await expect(page).to_have_url(f"{url}#goog_rewarded")
                await page.wait_for_url(f"{url}#goog_rewarded")
                await page.frame_locator(
                    "[id=\"google_ads_iframe_\\/421469808\\,22280442474\\/discordbotlist\\.com_rvideo_0\"]").get_by_text(
                    "Continue").nth(1).click()

                print("Wait ads", auth, url)
                # wait ads
                await page.wait_for_timeout(40 * 1000)
            except Exception as e:
                print(e)
                # await page.locator("span:nth-child(5) > .svg-inline--fa > path").click()
                # await page.wait_for_timeout(10 * 1000)
                # await page.wait_for_url(f"{url}/thanks")

        await page.wait_for_timeout(10 * 1000)
        print("----------------------------- Vote berhasil -----------------------------")
        await context.close()
    except Exception as e:
        await context.close()
        print("Error run vote2:", e)
        print("Run Again !!")
        await run_vote2(auth, url, browser)





async def run(auth, url, browser):
    if "top" in url:
        await run_vote(auth, url, browser)
    elif "discordbotlist" in url:
        await run_vote2(auth, url, browser)
    else:
        print("Error: URL Wrong choose top or discordbotlist")


auth = "YOUR AUTH TOKEN"

dank = "https://top.gg/bot/270904126974590976/vote"  # dank
tatsu = "https://top.gg/bot/172002275412279296/vote"

dank2 = "https://discordbotlist.com/bots/dank-memer/upvote"
tatsu2 = "https://discordbotlist.com/bots/tatsu/upvote"

auth_list = [auth]
url_list = [dank, dank2, tatsu, tatsu2]
channel_id = "1055217631990394991"


async def main():
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=True)

        for a in auth_list:
            for u in url_list:
                await run(a, u, browser)

        await browser.close()


while True:
    asyncio.run(main())
    time.sleep(12*3600)
