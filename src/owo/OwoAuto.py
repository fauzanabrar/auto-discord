import sys

sys.path.append("src/utils")
from src.utils.DiscordAPI import *
import json
import asyncio


class OwoAuto:
    def __init__(self, auth_token, channel_id):
        self.auth_token = auth_token
        self.channel_id = channel_id
        self.api = DiscordApi(auth_token, channel_id)
        self.username = json.loads(self.api.send_message("Hello").text)["author"][
            "username"
        ]

    async def run(self):
        await asyncio.gather(
            self.daily(),
            self.vote(),
            self.pray(),
            self.cookie(),
            self.autohunt(),
            self.auto(),
        )

    async def schedule(self, sec, callback, *args):
        await asyncio.sleep(sec)
        if asyncio.iscoroutinefunction(callback):
            await callback(*args)
        else:
            callback(*args)

    async def command(self, message, loop=1, sleep=5):
        for i in range(loop):
            status = self.api.send_message(f"{message}").status_code
            print(i, message, status, self.username)
            await asyncio.sleep(sleep)

    async def hunt(self):
        await self.command("owo hunt")

    async def battle(self):
        await self.command("owo battle")

    async def pray(self):
        await self.command("owo pray")
        await self.schedule(5 * 60, self.pray)

    async def cash(self):
        await self.command("owo cash")

    async def level(self):
        await self.command("owo level")

    async def quest(self):
        await self.command("owo quest")

    async def coinflip(self):
        await self.command("owo coinflip")

    async def daily(self):
        await self.command("owo daily")
        await self.schedule(24 * 60 * 60, self.daily)

    async def autohunt(self):
        await self.command("owo autohunt")

    async def slots(self):
        await self.command("owo slots")

    async def cookie(self):
        await self.command("owo cookie")

    async def vote(self):
        await self.command("owo vote")
        await self.schedule(12 * 60 * 60, self.vote)

    async def curse(self):
        await self.command("owo curse")
        await self.schedule(5 * 60, self.curse)

    async def action(self):
        await self.command("owo action")

    async def auto(self):
        while True:
            await self.hunt()
            await self.battle()
