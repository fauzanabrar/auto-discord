import asyncio

from src.dank.DankAuto import DankAuto



class DankTest(DankAuto):
    def __init__(self, auth_token, url, application_id, session_id):
        super().__init__(auth_token, url, application_id, session_id)

    def payload(self, type=2):
        return super().payload(type)

    async def schedule(self, sec, callback, *args):
        return await super().schedule(sec, callback, *args)

    async def run(self):
        return await super().run()

    async def command(self, payload, loop=1, sleep=2):
        return await super().command(payload, loop, sleep)

    def command2(self, payload, message="", sleep=2):
        super().command2(payload, message, sleep)

    def isFocus(focus=True):
        return super().isFocus()

    def check_massage(self, message):
        res = self.api.retrieve_message(40)
        for i in res:
            try:
                # print(i)
                check_message = i["embeds"][0]['title']
                if message.lower() in check_message.lower():
                    return i
            except:
                pass

        return None

    async def check_alert(self, res={}):
        return await super().check_alert(res)

    async def alert(self):
        return await super().alert()

    async def fish(self):
        return await super().fish()

    async def dig(self):
        return await super().dig()

    async def hunt(self):
        return await super().hunt()

    async def daily(self):
        return await super().daily()

    def highlow(self):
        return super().highlow()

    def choose_postmemes(self, message_id, custom_id, value):
        return super().choose_postmemes(message_id, custom_id, value)

    def postmemes(self):
        return super().postmemes()

    def search(self):
        return super().search()

    def crime(self):
        return super().crime()

    async def beg(self):
        return await super().beg()

    async def use_item(self, item_name, time):
        return await super().use_item(item_name, time)

    async def vote(self):
        return await super().vote()

    async def adventure(self):
        return await super().adventure()

    async def start_new_adventure(self, res):
        return await super().start_new_adventure(res)

    def choose_components(self, arr, res={}):
        super().choose_components(arr, res)

    def choose_components_emoji(self, arr, res={}):
        return super().choose_components_emoji(arr, res)

    async def stream(self):
        return await super().stream()

    def start_new_stream(self, message_id, custom_id):
        super().start_new_stream(message_id, custom_id)

    def stream_action(self, message_id, custom_id, choose):
        super().stream_action(message_id, custom_id, choose)

    async def mini_games(self, res={}):
        return await super().mini_games(res)

    async def work_shift(self):
        return await super().work_shift()

    async def auto(self):
        return await super().auto()

    async def balance(self):
        return await super().balance()

    async def blackjack(self, bet):
        return await super().blackjack(bet)

    async def choose_blackjack(self, res={}):
        return await super().choose_blackjack(res)

    async def choose_blackjack_menu(self, choose, res={}):
        return await super().choose_blackjack_menu(choose, res)

    async def runTest(self):
        res = self.check_massage("Black hole")
        await self.check_black_hole(res)
        await asyncio.sleep(3)

    async def check_black_hole(self, res={}):
        return await super().check_black_hole(res)


init = {
    "auth_token" : "MTAyMzQ0MDQ0OTk0OTY3MTQyNA.GwXXGc.ySIfRxhZjaSJTzJ6oykgJwlnGxn2rODv5ztynQ",
    "channel_id" : {
      "dank": {
        "url": "https://discord.com/channels/1020996568029077596/1041530557600907364",
        "application_id": "270904126974590976",
        "session_id": "b895ddb84ce0aa9180ba5d80b929bcc7"
      },
      "tatsu_channel_id": "1025205981078114374"
    }
  }

auth = init['auth_token']
url = init['channel_id']['dank']['url']
app_id = init['channel_id']['dank']['application_id']
ss_id = init['channel_id']['dank']['session_id']

asyncio.run(DankTest(auth, url, app_id, ss_id).runTest())