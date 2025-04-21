import asyncio
import re
import sys
import time
import random
from src.utils.DiscordAPI import *
import datetime


class AFAuto:

    def __init__(self, auth_token, url, application_id, session_id):
        self.auth_token = auth_token
        self.guild_id = url.split("/")[4]
        self.channel_id = url.split("/")[5]
        self.application_id = application_id
        self.session_id = session_id
        self.api = DiscordApi(self.auth_token, self.channel_id)
        self.username = json.loads(self.api.send_message("Helo").text)["author"][
            "username"
        ]
        self.stream_num = 1
        self.is_focus = False
        self.counter = 1

    def payload(self, type=2):
        return {
            "type": type,
            "application_id": self.application_id,
            "guild_id": self.guild_id,
            "channel_id": self.channel_id,
            "session_id": self.session_id,
        }

    async def schedule(self, sec, callback, *args):
        await asyncio.sleep(sec)
        if asyncio.iscoroutinefunction(callback):
            await callback(*args)
        else:
            callback(*args)

    async def run(self):
        await self.stats(8 * 60)
        await self.hunt(7 * 60 + 10)
        await self.attack(12 * 60 + 10)
        await self.gather(10 * 60 + 10)
        await self.pet_attack(30 * 60 + 20)
        await asyncio.sleep(3 * 365 * 24 * 60 * 60)
        # await self.craft_hunt_item(10 * 60 + 20)


    async def use_bandage(self):
        data = {
            "data": {
                "version": "1034883078990073951",
                "id": "1034883078956535841",
                "name": "use",
            }
        }
        data.update(self.payload())
        await self.command(data)

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
        data = {
            "data": {
                "version": "1157782679345967281",
                "id": "1113153202922209371",
                "name": "professions",
            }
        }
        data.update(self.payload())
        await self.command(data)
        await asyncio.sleep(2)

        res = self.api.retrieve_message()

        msg_id = res["id"]

        data = {
            "message_id": msg_id,
            "data": {
                "component_type": 2,
                "custom_id": "recipies-herbalism",
            },
        }

        data.update(self.payload(3))
        await self.command(data, message="craft herbalism")
        await asyncio.sleep(2)

        # data = {
        #     "data": {
        #         "component_type": 2,
        #         "custom_id": "recipies-herbalism",
        #         "name": "recipes-herbalism",
        #     }
        # }
        # data.update(self.payload())
        # await self.command(data)
        # await asyncio.sleep(2)
        # now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(f"craft at {now}")
        # asyncio.create_task(self.schedule(time, self.attack, time))

    async def stats(self, time=10 * 60):
        data = {
            "data": {
                "version": "1035597151071379566",
                "id": "1034883078956535839",
                "name": "stats",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await self.command(data)
        print(f"stats at {now}")
        asyncio.create_task(self.schedule(10 * 60, self.stats))

    async def gather(self, time=10 * 60):
        data = {
            "data": {
                "version": "1112138299532918850",
                "id": "1112138299532918845",
                "name": "gather",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await self.command(data)
        print(f"gather at {now}")
        asyncio.create_task(self.schedule(time, self.gather, time))

    async def hunt(self, time=10 * 60):
        data = {
            "data": {
                "version": "1147652859383525431",
                "id": "1147652859383525428",
                "name": "hunt",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await self.command(data)
        print(f"hunt at {now}")
        asyncio.create_task(self.schedule(time, self.hunt, time))

    async def attack(self, time=10 * 60):
        data = {
            "data": {
                "version": "1034883078956535842",
                "id": "1034883078885212291",
                "name": "attack",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await self.command(data)
        print(f"attack at {now}")

        # Check if the user is dead
        await self.revive()

        asyncio.create_task(self.schedule(time, self.attack, time + 3))

    async def pet_attack(self, time=10 * 60):
        data = {
            "data": {
                "version": "1251576908278399239",
                "id": "1251576907770757172",
                "name": "petattack",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        await self.command(data, message="pet attack")
        print(f"pet attack at {now}")

        asyncio.create_task(self.schedule(time, self.attack, time))

    async def revive(self, time=0):
        data = {
            "data": {
                "version": "1034883078990073946",
                "id": "1034883078885212298",
                "name": "revive",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        await self.command(data, message="revive")
        print(f"revive at {now}")
        
        if time != 0:
            asyncio.create_task(self.schedule(time, self.attack, time))

    async def command(self, payload, message="", loop=1, sleep=2):
        if message == "":
            message = payload["data"]["name"]
        for i in range(loop):
            status = self.api.send_interact(payload).text
            print(f"{message:42.40} | {status:50.50} | {self.username}")
            await asyncio.sleep(sleep)

    def command2(self, payload, message="", sleep=2):
        if message == "":
            message = payload["data"]["name"]
        status = self.api.send_interact(payload).text
        print(f"{message:42.40} | {status:150.150} | {self.username}")
        if sleep != 0:
            time.sleep(sleep)
