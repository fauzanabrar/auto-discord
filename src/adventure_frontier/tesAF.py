import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.adventure_frontier.AFAuto import *


class AFTest(AFAuto):
    def __init__(self, auth_token, url, application_id, session_id):
        super().__init__(auth_token, url, application_id, session_id)

    def payload(self, type=2):
        return super().payload(type)

    async def schedule(self, sec, callback, *args):
        return await super().schedule(sec, callback, *args)

    async def run(self):
        return await super().run()

    async def command(self, payload, message, loop=1, sleep=2):
        return await super().command(payload, message, loop, sleep)

    def command2(self, payload, message="", sleep=2):
        super().command2(payload, message, sleep)

    def check_massage(self, message):
        res = self.api.retrieve_message(40)
        for i in res:
            try:
                # print(i)
                check_message = i["embeds"][0]["title"]
                if message.lower() in check_message.lower():
                    return i
            except:
                pass

        return None

    async def hunt(self, time=10 * 60):
        return await super().hunt(time)

    async def attack(self, time=10 * 60):
        return await super().attack(time)

    async def pet_attack(self, time=10 * 60):
        return await super().pet_attack(time)

    async def gather(self, time=10 * 60):
        return await super().gather(time)

    async def stats(self, time=10 * 60):
        return await super().stats(time)

    async def use_bandage(self, time=10 * 60):
        data = {
            "data": {
                "version": "1034883078990073951",
                "id": "1034883078956535841",
                "name": "use",
            }
        }
        data.update(self.payload())
        await self.command(data, message="use bandage")

        payload = {
            "type": 3,
            "guild_id": "1362991722476605520",
            "channel_id": "1362992125733503177",
            "message_flags": 64,
            "message_id": "1363029719842426951",
            "application_id": "1034876159197974569",
            "session_id": "539050b262d51344957a4ee2b12d41f6",
            "data": {
                "component_type": 3,
                "custom_id": "use-item-0",
                "type": 3,
                "values": ["use-item-1964c8308a052e307018c5c"],
            },
        }

        status = self.api.send_interact(payload).text
        print(status)

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"bandage at {now}")
        asyncio.create_task(self.schedule(10 * 60, self.use_bandage))

    async def craft_hunt_item(self, time=10 * 60):
        # data = {
        #     "data": {
        #         "version": "1157782679345967281",
        #         "id": "1113153202922209371",
        #         "name": "professions",
        #     }
        # }
        # data.update(self.payload())
        # # await self.command(data, message="")
        # res = self.api.send_interact(data)
        # print(res)
        # await asyncio.sleep(2)

        # # res = self.api.retrieve_message(5)
        # # print(res)
        # # msg_id = res["id"]
        # msg_id = data["data"]["id"]
        msg_id = "1363027019742314537"
        # print(msg_id)
        # data = {
        #     "message_id": msg_id,
        #     "data": {
        #         "component_type": 2,
        #         "custom_id": "recipies-herbalism",
        #     }
        # }

        # data.update(self.payload(3))
        # await self.command(data, message="craft herbalism")
        # await asyncio.sleep(2)

        payload = {
            "type": 3,
            "guild_id": "1362991722476605520",
            "channel_id": "1362992125733503177",
            "message_id": msg_id,
            "application_id": "1034876159197974569",
            "data": {"component_type": 2, "custom_id": "recipies-herbalism"},
        }

        status = self.api.send_interact(payload).text
        print(status)

    async def runTest(self):
        # await self.craft_hunt_item(10 * 60)
        await self.pet_attack(10 * 60)
        # await self.use_bandage(10 * 60)
        await asyncio.sleep(1)

    async def check_black_hole(self, res={}):
        return await super().check_black_hole(res)


init = {
    "auth_token": "NzEyNTYzNzQ3ODEzNTg5MDQy.GTBF5B.JIpfNRW-_WkhcC7lPmQn-qKe_Tt7QRgp3MauKU",
    "channel_id": {
        "ninja_sage_id": "949159340802199593",
        "adventure_frontier": {
            "url": "https://discord.com/channels/1362991722476605520/1362992125733503177",
            "application_id": "1034876159197974569",
            "session_id": "035a9f9f5b08eb9f030bec01a1a7a25e",
        },
    },
}

auth = init["auth_token"]
url = init["channel_id"]["adventure_frontier"]["url"]
app_id = init["channel_id"]["adventure_frontier"]["application_id"]
ss_id = init["channel_id"]["adventure_frontier"]["session_id"]

asyncio.run(AFTest(auth, url, app_id, ss_id).runTest())
