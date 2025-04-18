import sys
sys.path.append('src/utils')
from src.utils.DiscordAPI import *
import json
import asyncio
import random


class NinjaSageAuto:
    def __init__(self, auth_token, channel_id):
        self.auth_token = auth_token
        self.channel_id = channel_id
        self.api        = DiscordApi(auth_token,channel_id)
        # self.username   = json.loads(self.api.send_message("Hello").text)['author']['username']

    async def run(self):
        await asyncio.gather(
            self.halo(),
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
            # print(i, message, status, self.username)
            await asyncio.sleep(sleep)

    async def halo(self):
        random_int = random.randint(1, 10)
        list_msg = [":tada:", ":rocket:", ":cry:", ":pray", "moai"]
        for i in range(1, random_int):
            msg = random.choice(list_msg)
            await self.command(f"{msg}")
            print(f"Command {msg} sent")
            await asyncio.sleep(240)
