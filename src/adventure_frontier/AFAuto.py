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
        self.username = json.loads(self.api.send_message("Hello").text)["author"][
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
        await self.auto_all()

    async def auto_all(self):
        while True:
            await self.stats()
            await self.hunt()
            await self.attack()
            await self.gather()

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
        asyncio.create_task(self.schedule(time, self.attack, time))

    async def command(self, payload, loop=1, sleep=2):
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

    