import math
import sys

sys.path.append("src/utils")

from src.utils.DiscordAPI import *
from src.utils.Vote import *


class TatsuAuto:
    def __init__(self, auth_token, channel_id):
        self.auth_token = auth_token
        self.channel_id = channel_id
        self.api = DiscordApi(auth_token, channel_id)
        self.all_tasks = [0, 0, 0, 0, 0, 0]  # train, fish, walk, slot, chat, cookie
        self.username = json.loads(self.api.send_message("Hello").text)["author"][
            "username"
        ]

    async def schedule(self, sec, callback, *args):
        await asyncio.sleep(sec)
        if asyncio.iscoroutinefunction(callback):
            await callback(*args)
        else:
            callback(*args)

    async def run(self):
        await asyncio.gather(
            self.daily(), self.run_quest(), self.mail(), self.vote(), self.auto()
        )
        # await self.daily()
        # await self.run_quest()
        # await self.mail()
        # await self.auto()

    async def command(self, message, loop=1, sleep=5):
        for i in range(loop):
            status = self.api.send_message(f"{message}").status_code
            print(i, message, status, self.username)
            await asyncio.sleep(sleep)

    async def confirm(self):
        await self.command("confirm")

    async def exit(self):
        await self.command("exit")

    async def train(self, loop=1):
        await self.command("t!tg train", loop)

    async def fish(self, loop=1):
        await self.command("t!fish", loop)

    async def slot(self, amount=0, loop=1):
        if amount:
            await self.command(f"t!slot {amount}", loop)
        else:
            await self.command("t!slot", loop)

    async def cookie(self, loop=1):
        await self.command("t!cookie", loop)

    async def walk(self, loop=1):
        for i in range(math.ceil(loop / 2)):
            await self.feed()
            await self.command("t!tg walk")
            await self.command("t!tg walk")

    async def feed(self):
        await self.command("t!tg feed")

    async def quest(self, isClaim=False):
        if isClaim:
            await self.command("t!quest claim")
        else:
            await self.command("t!quest 1", sleep=0)

    async def daily(self):
        await self.command("t!daily")
        await self.schedule(24 * 60 * 60, self.daily)

    async def vote(self):
        await self.command("t!vote", sleep=0)
        res = self.api.retrieve_message()

        link_dbl = res["embeds"][0]["fields"][1]["value"].split("(")[1].split(")")[0]
        link_topgg = res["embeds"][0]["fields"][0]["value"].split("(")[1].split(")")[0]

        await Vote(self.auth_token, link_dbl).run()
        await Vote(self.auth_token, link_topgg).run()

        await self.schedule(12 * 60 * 60, self.vote)

    async def mail(self):
        await self.command("t!mail claim all")
        await self.schedule(24 * 60 * 60, self.mail)

    async def open(self):
        await self.command("t!open")
        await self.command("1")
        await self.command("6")  # choose yellow cat pet
        await self.confirm()

    async def active_pet(self):
        await self.command("t!tg edit")
        await self.command("1")
        await self.command("1")
        await self.command("1")

    async def exchange(self, choose1, choose2, amount):
        await self.command("t!exchange")
        await self.command(f"{choose1}")
        await self.command(f"{choose2}")
        await self.command(f"{amount}")
        await self.confirm()

    async def trade(self, menu, receiver, add_or_remove, choose_item, amount):
        await self.command("t!trade")
        await self.command(f"{menu}")
        await self.command(f"{receiver}")
        await self.command(f"{add_or_remove}")
        await self.command(f"{choose_item}")
        await self.command(f"{amount}")
        await self.confirm()

    async def check_quest(self):
        await self.quest()
        res = self.api.retrieve_message(order=10)
        for i in res:
            if len(i["content"].split("**")) >= 3:
                if self.username in i["content"].split("**")[2]:
                    try:
                        tasks = i["embeds"][0]["fields"]
                        for j in tasks:
                            t = j["name"]
                            if "Walk" in t:
                                self.all_tasks[2] = int(t.split()[3])
                            elif " Chat" in t:
                                self.all_tasks[4] = int(t.split()[1])
                            elif " Fish" in t:
                                self.all_tasks[1] = int(t.split()[1])
                            elif " Slots " in t:
                                self.all_tasks[3] = int(t.split()[2])
                            elif "Cookies" in t:
                                self.all_tasks[5] = int(t.split()[1])
                            elif "Train" in t:
                                self.all_tasks[0] = int(t.split()[3])
                        print(self.all_tasks)
                    except:
                        print("error in check quest")
                        await self.check_quest()
                    break

    async def run_quest(self):
        # check quest
        await self.check_quest()

        # run quest
        await self.train(self.all_tasks[0])
        await self.fish(self.all_tasks[1])
        await self.walk(self.all_tasks[2])
        await self.slot(loop=self.all_tasks[3])
        await self.train(self.all_tasks[4])  # chat
        await self.cookie(self.all_tasks[5])

        # claim quest
        await self.quest(isClaim=True)
        await self.schedule(24 * 60 * 60, self.run_quest)

    async def auto(self):
        for i in range(
            1428
        ):  # (60 secs * 60 minutes * 24 hours) / 50 secs = 1728 - 300 (do daily quest) = 1428 times run for a day
            await self.train()
            print("auto", i)
            await asyncio.sleep(45)
