import asyncio
from playwright.async_api import async_playwright


class Vote:

    def __init__(self, auth_token, link_vote):
        self.auth_token = auth_token
        self.link_vote = link_vote

    async def run(self):
        if "top.gg" in self.link_vote:
            asyncio.create_task(self.vote_topgg())
        elif "discordbotlist.com" in self.link_vote:
            asyncio.create_task(self.vote_dbl())

    async def vote_topgg(self):
        with async_playwright() as p:
            try:
                browser = p.webkit.launch(headless=True, slow_mo=3 * 100)
                page = browser.new_page()
                page.goto(self.link_vote, timeout=0)

                # click vote
                page.locator("text=Vote").nth(1).click()
                page.wait_for_timeout(5 * 1000)

                browser.close()
            except:
                browser.close()
                browser = p.webkit.launch(headless=True, slow_mo=3 * 100)
                page = browser.new_page()
                page.goto(self.link_vote, timeout=0)

                # detect login to vote
                tes = page.locator('//*[@id="chakra-modal-13"]/div[2]/a[1]')
                tes.click(timeout=0)

                # login discord with auth token
                sauth = f'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{self.auth_token}"`'
                page.wait_for_selector(
                    '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]',
                    timeout=0,
                )
                page.evaluate(sauth)
                page.reload(timeout=0)

                # authoritize top.gg
                page.wait_for_selector(
                    '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]',
                    timeout=0,
                )
                authorize = page.locator(
                    '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]'
                )
                authorize.click(timeout=0)

                # click vote
                page.wait_for_url(self.link_vote, timeout=0)
                page.locator("text=Vote").nth(1).click()

                browser.close()

    async def vote_dbl(self):
        with async_playwright() as p:
            browser = p.webkit.launch(headless=False, slow_mo=3 * 100)
            page = browser.new_page()

            ## next url
            page.goto(self.link_vote, timeout=0)

            # click vote
            tes = page.locator("text=Upvote")
            tes.nth(1).click()
            page.wait_for_timeout(3 * 1000)

            # login discord with auth token
            sauth = f'document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{self.auth_token}"`'
            page.wait_for_selector(
                '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]',
                timeout=0,
            )
            page.evaluate(sauth)
            page.reload(timeout=0)
            page.wait_for_timeout(10 * 1000)

            # click vote
            ## next url
            page.goto(self.link_vote, timeout=0)

            # click vote
            tes2 = page.locator("text=Upvote")
            tes2.nth(1).click()
            try:
                tes3 = page.locator("text=Continue")
                tes3.nth(1).click()
                page.wait_for_timeout(30 * 1000)
            except:
                pass
            browser.close()
