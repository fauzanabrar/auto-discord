import sys

sys.path.append("src/utils")
from src.utils.DiscordAPI import *
import json
import asyncio
import random


class NinjaSageAuto:
    def __init__(self, auth_token, channel_id):
        self.auth_token = auth_token
        self.channel_id = channel_id
        self.api = DiscordApi(auth_token, channel_id)
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
        list_msg = [
            ":tada:",
            ":rocket:",
            ":cry:",
            ":pray",
            "moai",
            ":wave:",
            ":exploding_head:",
            "halo",
        ]
        while True:
            msg = random.choice(list_msg)
            random_int = random.randint(1, 10)
            if random_int < 4:
                await self.command(f"{msg}")
                print(f"Command {msg} sent")
            else:
                print(f"Command {msg} not sent")
            print(f"Sleeping for 240 seconds")
            await asyncio.sleep(240)
