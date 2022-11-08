import time
import re
from twocaptcha import TwoCaptcha
import string
import requests
import json


from playwright.sync_api import sync_playwright

def solverHcaptcha(sitekey, url):
    solver = TwoCaptcha('d48130f88087c7b46fae7ef52dff8f6a')

    result = solver.hcaptcha(
    sitekey=sitekey,
    url=url,
    )
    # print(result['code'])
    return result['code']


def runVote(auth, url):
    with sync_playwright() as p:
        try:

            browser = p.webkit.launch(headless=True, slow_mo=3 * 100)
            page = browser.new_page()
            page.goto(url, timeout=0)

            # click vote
            print("just wait, berhasil?")
            page.locator("text=Vote").nth(1).click()
            print("udah")
            page.wait_for_timeout(5*1000)

            browser.close()
        except:
            browser.close()
            print("belum authoritize")
            browser = p.webkit.launch(headless=True, slow_mo=3 * 100)
            page = browser.new_page()
            page.goto(url, timeout=0)

            # detect login to vote
            tes = page.locator('//*[@id="chakra-modal-13"]/div[2]/a[1]')
            print(tes.inner_html())
            tes.click(timeout=0)

            # login discord with auth token
            sauth = f'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{auth}"`'
            page.wait_for_selector(
                '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]',
                timeout=0)
            page.evaluate(sauth)
            print("berhasil evaluate")
            page.reload(timeout=0)
            print("berhasil reload")

            # authoritize top.gg
            page.wait_for_selector('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]',
                                   timeout=0)
            authorize = page.locator('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]')
            authorize.click(timeout=0)

            # click vote
            page.wait_for_url(url, timeout=0)
            print("just wait, berhasil?")
            page.locator("text=Vote").nth(1).click()
            print("udah")

            browser.close()

def runVote2(auth, url2):
  with sync_playwright() as p:
    browser = p.webkit.launch(headless=True, slow_mo=3 * 100)
    page = browser.new_page()

    ## next url
    page.goto(url2, timeout=0)

    # click vote
    print("just wait, berhasil?")
    tes = page.locator("text=Upvote")
    tes.nth(1).click()
    print("udah")
    page.wait_for_timeout(3 * 1000)

    # login discord with auth token
    sauth = f'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{auth}"`'
    page.wait_for_selector(
      '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]',
      timeout=0)
    page.evaluate(sauth)
    print("berhasil evaluate")
    page.reload(timeout=0)
    print("berhasil reload")
    page.wait_for_timeout(10 * 1000)
    print("hmm")

    # click vote
    ## next url
    page.goto(url2, timeout=0)

    # click vote
    print("just wait, berhasil?")
    tes2 = page.locator("text=Upvote")
    tes2.nth(1).click()
    print("iklan muncul")
    try:
      tes3 = page.locator("text=Continue")
      tes3.nth(1).click()
      print("udah")
      page.wait_for_timeout(30 * 1000)
    except:
      pass
    browser.close()

authf = "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ" #f
authb = "MTAyMzQzODQ2OTYyMTYyMDg1Nw.GQposd.457v3IY1XOH6Dyurv0nAp2sT6uwqdMa-qPMK_M"  # b
auth = "NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA"

owo         = "https://top.gg/bot/408785106942164992/vote" #owo
dank        = "https://top.gg/bot/270904126974590976/vote"  # dank
mudae       = "https://top.gg/bot/432610292342587392/vote" #mudae
poketwo     = "https://top.gg/bot/716390085896962058/vote" #poketwo
soccerGuru  = "https://top.gg/bot/668075833780469772/vote" #soccer guru
tatsu       = "https://top.gg/bot/172002275412279296/vote"

dank2       = "https://discordbotlist.com/bots/dank-memer/upvote"
tatsu2       = "https://discordbotlist.com/bots/tatsu/upvote"



# runVote(authb, tatsu)
# runVote2(authb, tatsu2)
# runVote(authb, dank)
# runVote2(authb, dank2)
# runVote(authb, owo)

runVote(authf, tatsu)
runVote2(authf, tatsu2)
runVote(authf, dank)
runVote2(authf, dank2)
# runVote(authf, owo)


# runVote(auth, tatsu)
# runVote2(auth, tatsu2)
# runVote(auth, dank)
# runVote2(auth, dank2)
# runVote(auth, owo)