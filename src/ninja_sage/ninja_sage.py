import datetime
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
            "<:Shocked:955336495085019186>",
            "<:patrik:1061825765752193074>",
            "<:aquacry:932341310835286097>",
            ":pray:",
            ":moai:",
            "<:pikathumbsup:931465375462354966>",
            ":exploding_head:",
            "<:kekw:927464653322330173>",
            "<:PepeHappy:932340970878554122>",
            "<:pepewow:932340971025338368>",
            "<:dogelul:955848687702143046>",
            "<:Hehe:932341310751408168>",
        ]
        while True:
            msg = random.choice(list_msg)
            random_int = random.randint(1, 10)

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if random_int < 6:
                await self.command(f"{msg}")
                print(f"Command {msg} sent at {now}")

                res = self.api.retrieve_message(10)
                res = [r for r in res if r["content"] == msg]

                if len(res) == 0:
                    print(f"Command {msg} not found")

                msg_id = res[0]["id"]
                content = res[0]["content"]

                if content == msg:
                    self.api.delete_message(msg_id)
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Command {msg} deleted at {now}")
            else:
                print(f"Command {msg} not sent")

            print(f"Sleeping for 240 seconds")
            await asyncio.sleep(4 * 60)
