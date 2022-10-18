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


# yosshhshshshshs
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=3*100)
#     page = browser.new_page()
#     url = "https://accounts.hcaptcha.com/demo"
#     page.goto(url)
#     # page.pause()
#
#     tes = page.locator('textarea').nth(1)
#     lidi = page.locator('li div').nth(0).inner_html()
#
#     x = re.search(r"(?<=\bdata-sitekey=\")[^\"]*", lidi)
#     print(x.group())
#
#     tes.evaluate("element => element.style.display = 'block'")
#     tes.fill(solverHcaptcha(x.group(),url))
#     print(tes.evaluate("e => e.value"))
#
#     page.locator('//*[@id="hcaptcha-demo-submit"]').click()
#     page.pause()
#
#     browser.close()

#berhasil di cloud yey
# with sync_playwright() as p:
#     # browser = p.chromium.launch(headless=False, slow_mo=3*100)
#     # userDir = "C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
#     # browser = p.webkit.launch_persistent_context(user_data_dir=userDir,headless=False, slow_mo=3*100)
#     # browser = p.webkit.launch_persistent_context(user_data_dir=userDir,headless=False, slow_mo=3*100)
#     browser = p.webkit.launch(headless=True, slow_mo=3*100)
#     page = browser.new_page()
#
#     # url = "https://top.gg/bot/408785106942164992/vote" #owo
#     url = "https://top.gg/bot/270904126974590976/vote" #dank
#     # url = "https://top.gg/bot/432610292342587392/vote" #mudae
#     # url = "https://top.gg/bot/716390085896962058/vote" #poketwo
#     # url = "https://top.gg/bot/668075833780469772/vote" #soccer guru
#     page.goto(url,timeout=0)
#     # page.pause()
#
#
#     tes = page.locator('//*[@id="chakra-modal-13"]/div[2]/a[1]')
#     print(tes.inner_html())
#     tes.click(timeout=0)
#     # auth = "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ" #f
#     auth = "MTAyMzQzODQ2OTYyMTYyMDg1Nw.GQposd.457v3IY1XOH6Dyurv0nAp2sT6uwqdMa-qPMK_M" #b
#     #
#     sauth = f'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{auth}"`'
#     page.wait_for_selector('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]', timeout=0)
#     page.evaluate(sauth)
#     print("berhasil evaluate")
#     page.reload(timeout=0)
#     #
#     print("berhasil reload")
#     page.wait_for_selector('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]',timeout=0)
#     authorize = page.locator('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]')
#     authorize.click(timeout=0)
#     #
#     page.wait_for_url(url, timeout=0)
#     # vote = page.locator('//*[@id="__next"]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/main/div[1]/div/div[2]/button')
#     # vote.click(timeout=0)
#     print("just wait, berhasil?")
#     page.locator("text=Vote").nth(1).click()
#     print("udah")
#     # ge = r"(?<=\bsitekey=)[^\&]*"
#     page.wait_for_timeout(15000)
#
#     # '/html/body/iframe[6]'
#     # '/html/body/div[11]/div[1]/iframe'
#     # page.wait_for_timeout(10000000)
#     # cari_sitekey = page.locator('//html/body/div[11]/div[1]')
#     # print("dapat sitekey")
#     # print(cari_sitekey.inner_html())
#     # sitekey = re.search(ge, cari_sitekey.inner_html()).group()
#     # print("sitekey", sitekey)
#     # tes = page.locator('textarea').nth(1)
#     # tes.evaluate("element => element.style.display = 'block'")
#     # print("textarea udah keliatan, tunggu solve")
#     # tes.fill(solverHcaptcha(sitekey,url))
#     # print(tes.evaluate("e => e.value"))
#     # print("hmm how to submit")
#
#
#     # page.wait_for_timeout(500000)
#
#     # tes = page.locator('textarea').nth(1)
#     # lidi = page.locator('li div').nth(0).inner_html()
#     #
#     # x = re.search(r"(?<=\bdata-sitekey=\")[^\"]*", lidi)
#     # print(x.group())
#     #
#     # tes.evaluate("element => element.style.display = 'block'")
#     # tes.fill(solverHcaptcha(x.group(),url))
#     # print(tes.evaluate("e => e.value"))
#     #
#     # page.locator('//*[@id="hcaptcha-demo-submit"]').click()
#
#
#     browser.close()

# untuk cloud
# with sync_playwright() as p:
#     browser = p.webkit.launch(headless=True, slow_mo=3 * 100)
#     page = browser.new_page()
#
#     # url = "https://top.gg/bot/408785106942164992/vote" #owo
#     url = "https://top.gg/bot/270904126974590976/vote"  # dank
#     # url = "https://top.gg/bot/432610292342587392/vote" #mudae
#     # url = "https://top.gg/bot/716390085896962058/vote" #poketwo
#     # url = "https://top.gg/bot/668075833780469772/vote" #soccer guru
#     page.goto(url, timeout=0)
#
#     # detect login to vote
#     tes = page.locator('//*[@id="chakra-modal-13"]/div[2]/a[1]')
#     print(tes.inner_html())
#     tes.click(timeout=0)
#
#     # login discord with auth token
#     # auth = "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ" #f
#     auth = "MTAyMzQzODQ2OTYyMTYyMDg1Nw.GQposd.457v3IY1XOH6Dyurv0nAp2sT6uwqdMa-qPMK_M"  # b
#     sauth = f'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{auth}"`'
#     page.wait_for_selector(
#         '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]', timeout=0)
#     page.evaluate(sauth)
#     print("berhasil evaluate")
#     page.reload(timeout=0)
#     print("berhasil reload")
#
#     # authoritize top.gg
#     page.wait_for_selector('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]', timeout=0)
#     authorize = page.locator('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]')
#     authorize.click(timeout=0)
#
#     # click vote
#     page.wait_for_url(url, timeout=0)
#     # vote = page.locator('//*[@id="__next"]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/main/div[1]/div/div[2]/button')
#     # vote.click(timeout=0)
#     print("just wait, berhasil?")
#     page.locator("text=Vote").nth(1).click()
#     print("udah")
#     # page.wait_for_timeout(15000)
#
#     # cari site_key pake regex
#     # ge = r"(?<=\bsitekey=)[^\&]*"
#     # cari_sitekey = page.locator('//html/body/div[11]/div[1]')
#     # print("dapat sitekey")
#     # print(cari_sitekey.inner_html())
#     # sitekey = re.search(ge, cari_sitekey.inner_html()).group()
#     # print("sitekey", sitekey)
#
#     # tampilkan textarea
#     # tes = page.locator('textarea').nth(1)
#     # tes.evaluate("element => element.style.display = 'block'")
#     # print("textarea udah keliatan, tunggu solve")
#
#     # solve + isi textarea dengan token hcaptcha
#     # tes.fill(solverHcaptcha(sitekey,url))
#     # print(tes.evaluate("e => e.value"))
#     # print("hmm how to submit")
#
#     # page.wait_for_timeout(500000)
#
#
#     browser.close()

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



owo         = "https://top.gg/bot/408785106942164992/vote" #owo
dank        = "https://top.gg/bot/270904126974590976/vote"  # dank
mudae       = "https://top.gg/bot/432610292342587392/vote" #mudae
poketwo     = "https://top.gg/bot/716390085896962058/vote" #poketwo
soccerGuru  = "https://top.gg/bot/668075833780469772/vote" #soccer guru
tatsu       = "https://top.gg/bot/172002275412279296/vote"

authf = "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ" #f
authb = "MTAyMzQzODQ2OTYyMTYyMDg1Nw.GQposd.457v3IY1XOH6Dyurv0nAp2sT6uwqdMa-qPMK_M"  # b
auth = "NzEyNTYzNzQ3ODEzNTg5MDQy.YVas6Q.xpjaHQGhqmUTOXvZhOTNy4RwGuA"

# runVote(authb, tatsu)
# runVote(authb, owo)
# runVote(authb, dank)

# runVote(authf, tatsu)
# runVote(authf, owo)
# runVote(authf, dank)

runVote(auth, tatsu)
runVote(auth, owo)
runVote(auth, dank)
