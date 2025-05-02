import asyncio
import re
import sys
import time
import random
from src.utils.DiscordAPI import *
import datetime


class AFAuto:

    def __init__(self, auth_token, url, application_id, session_id, raid_url):
        self.auth_token = auth_token
        self.guild_id = url.split("/")[4]
        self.channel_id = url.split("/")[5]
        self.application_id = application_id
        self.session_id = session_id
        self.raid_guild_id = raid_url.split("/")[4]
        self.raid_channel_id = raid_url.split("/")[5] 
        self.api = DiscordApi(self.auth_token, self.channel_id)
        self.raid_api = DiscordApi(self.auth_token, self.raid_channel_id)
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

    async def schedule_at(self, target_time, interval, callback, *args):
        """
        Schedule a task to run at a specific time repeatedly.
        
        :param target_time: A string in "HH:MM" format representing the target time.
        :param interval: Interval in seconds for repeated execution.
        :param callback: The coroutine or function to execute.
        :param args: Arguments to pass to the callback.
        """
        while True:
            now = datetime.datetime.now()
            target = datetime.datetime.combine(now.date(), datetime.time.fromisoformat(target_time))
            
            # If the target time has already passed today, schedule for tomorrow
            if now > target:
                target += datetime.timedelta(days=1)
            
            delay = (target - now).total_seconds()
            hours, remainder = divmod(int(delay), 3600)
            minutes, seconds = divmod(remainder, 60)
            readable_delay = f"{hours} hours, {minutes} minutes, {seconds} seconds"
            print(f"Scheduling task to run at {target_time}. Next run in {readable_delay}.")
            
            await asyncio.sleep(delay)
            
            # Execute the callback
            if asyncio.iscoroutinefunction(callback):
                await callback(*args)
            else:
                callback(*args)
            
            # Wait for the interval before scheduling the next run
            await asyncio.sleep(interval)

    async def schedule_raid(self, target_time):
        # Parse the initial target time
        target_datetime = datetime.datetime.strptime(target_time, "%H:%M")
        now = datetime.datetime.now()

        # Adjust the target time to today or tomorrow if it has already passed
        if target_datetime.time() <= now.time():
            target_datetime = target_datetime.replace(year=now.year, month=now.month, day=now.day) + datetime.timedelta(days=1)
        else:
            target_datetime = target_datetime.replace(year=now.year, month=now.month, day=now.day)

        # Schedule the first and second raids concurrently
        first_raid_time = target_datetime.strftime("%H:%M")
        second_raid_time = (target_datetime + datetime.timedelta(hours=12)).strftime("%H:%M")

        await asyncio.gather(
            self.schedule_at(first_raid_time, 10 * 60, self.raid),
            self.schedule_at(second_raid_time, 10 * 60, self.raid)
        )

    async def run(self):
        # await self.stats(10 * 60)
        await self.hunt(7 * 60 + 10)
        await self.attack(3 * 60)
        await self.gather(10 * 60 + 5)
        await self.mine(10 * 60 + 5)
        await self.pet_attack(10 * 60)
        await self.runes(24 * 60 * 60)
        await self.schedule_raid("10:31")
        await asyncio.sleep(3 * 365 * 24 * 60 * 60)

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

    async def mine(self, time=10 * 60):
        data = {
            "data": {
                "version": "1112138299532918851",
                "id": "1112138299532918846",
                "name": "mine",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await self.command(data)

        print(f"mine at {now}")
        asyncio.create_task(self.schedule(time, self.mine, time))

    async def runes(self, time=24 * 60 * 60):
        data = {
            "data": {
                "version": "1086774197101010996",
                "id": "1086774197101010995",
                "name": "runes",
            }
        }
        data.update(self.payload())
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await self.command(data)

        print(f"runes at {now}")
        asyncio.create_task(self.schedule(time, self.runes, time))

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

        asyncio.create_task(self.schedule(time, self.attack, time))

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

        asyncio.create_task(self.schedule(time, self.pet_attack, time))

    async def get_raid_attack_message_id(self):
        # Retrieve the latest messages from the raid channel
        messages = self.raid_api.retrieve_message(10)  # Adjust the number of messages as needed

        for message in messages:
            # Check if the message has components (buttons)
            if "components" in message and message["components"]:
                for component in message["components"]:
                    for button in component["components"]:
                        # Check if the button has the custom_id "raidattack"
                        if button.get("custom_id") == "raidattack":
                            return message["id"]  # Return the message ID

        return None  # Return None if no message with the "raidattack" button is found

    async def raid(self):
        raid_attack_message_id = await self.get_raid_attack_message_id()

        if raid_attack_message_id:
            data = {
                "type": 3,
                "guild_id": self.raid_guild_id,
                "channel_id": self.raid_channel_id,
                "message_id": raid_attack_message_id,
                "application_id": self.application_id,
                "session_id": self.session_id,
                "data": {
                    "component_type": 2,
                    "custom_id": "raidattack"
                }
            }
            
            for i in range(30):
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                await self.command(data, message="raid attack")
                print(f"raid attack at {now}")
                await self.revive()
                await asyncio.sleep(17)

                # Yield control to the event loop
                await asyncio.sleep(0)

        else:
            print("No Raid Attack message found.")

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
            asyncio.create_task(self.schedule(time, self.revive, time))

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
