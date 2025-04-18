import asyncio
import re
import sys
import time
import random
from src.utils.DiscordAPI import *
from src.utils.Vote import *
from src.utils.BlackjackSolver import blakcjackSolver


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
            print("sleep 10 minutes")
            await asyncio.sleep(10 * 60)

    async def stats(self):
        data = {
            "data": {
                "version": "1035597151071379566",
                "id": "1034883078956535839",
                "name": "stats",
            }
        }
        data.update(self.payload())
        await self.command(data)
        print("stats")

    async def gather(self):
        data = {
            "data": {
                "version": "1112138299532918850",
                "id": "1112138299532918845",
                "name": "gather",
            }
        }
        data.update(self.payload())
        await self.command(data)
        print("gather")

    async def hunt(self):
        data = {
            "data": {
                "version": "1147652859383525431",
                "id": "1147652859383525428",
                "name": "hunt",
            }
        }
        data.update(self.payload())
        await self.command(data)
        print("hunt")

    async def attack(self):
        data = {
            "data": {
                "version": "1034883078956535842",
                "id": "1034883078885212291",
                "name": "attack",
            }
        }
        data.update(self.payload())
        await self.command(data)
        print("attack")

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

    def isFocus(focus=True):
        def _isFocus(func):

            async def wrap(self, *args, **kwargs):
                if self.is_focus:
                    print("focus so dont do that")
                    print("wait")
                    await asyncio.sleep(3)

                print("not focus")
                if focus:
                    self.is_focus = True
                    if asyncio.iscoroutinefunction(func):
                        await func(self, *args, **kwargs)
                    else:
                        func(self, *args, **kwargs)
                    self.is_focus = False
                else:
                    if asyncio.iscoroutinefunction(func):
                        await func(self, *args, **kwargs)
                    else:
                        func(self, *args, **kwargs)

            return wrap

        if callable(focus):
            return _isFocus(focus)
        else:
            return _isFocus

    def check_massage(self, message):
        res = self.api.retrieve_message(10)
        for i in res:
            try:
                check_message = i["interaction"]["name"]
                if message.lower() in check_message.lower():
                    return i
            except:
                pass

        return None

    async def check_alert(self, res={}):
        if res == {}:
            res = self.api.retrieve_message()
        try:
            if "You have an unread alert!" in res["embeds"][0]["title"]:
                await self.alert()
        except:
            # print("")
            pass

    async def check_black_hole(self, res={}):
        if res == {}:
            res = self.api.retrieve_message()
        try:
            if "BLACK HOLE".lower() in res["embeds"][0]["title"].lower():
                print("Ada blackhole")
            # await self.alert()
        except:
            # print("")
            pass

    async def alert(self):
        data = {
            "data": {
                "version": "1022917002748235836",
                "id": "1011560370864930852",
                "name": "alert",
            }
        }
        data.update(self.payload())
        await self.command(data)

    @isFocus
    async def fish(self):
        data = {
            "data": {
                "version": "1022917002878259287",
                "id": "1011560371078832206",
                "name": "fish",
            }
        }
        data.update(self.payload())
        await self.command(data)
        res = self.api.retrieve_message()
        await self.check_alert(res)
        await self.mini_games(res)

    @isFocus
    async def dig(self):
        data = {
            "data": {
                "version": "1022917002878259285",
                "id": "1011560371078832204",
                "name": "dig",
            }
        }
        data.update(self.payload())
        await self.command(data)
        res = self.api.retrieve_message()
        await self.check_alert(res)
        await self.mini_games(res)

    @isFocus
    async def daily(self):
        data = {
            "data": {
                "version": "1022917002748235840",
                "id": "1011560370864930856",
                "name": "daily",
            }
        }
        data.update(self.payload())
        await self.command(data)
        asyncio.create_task(self.schedule(24 * 60 * 60, self.daily))

    @isFocus
    def highlow(self):
        data = {
            "data": {
                "version": "1022917002748235843",
                "id": "1011560370911072258",
                "name": "highlow",
            }
        }
        data.update(self.payload())
        self.command2(data)

        res = self.api.retrieve_message()

        message_id = res["id"]
        try:
            guess_num = int(((res["embeds"][0]["description"]).split("**"))[1])
            choose = ""
            if guess_num >= 50:
                choose = "Lower"
            else:
                choose = "Higher"

            components = res["components"][0]["components"]
            for i in components:
                if choose.lower() == i["label"].lower():
                    custom_id = i["custom_id"]
                    data = {
                        "message_id": message_id,
                        "data": {
                            "component_type": 2,
                            "custom_id": custom_id,
                            "name": f"choose {choose}",
                        },
                    }
                    data.update(self.payload(3))
                    self.command2(data)
                    break
        except:
            print("Error cant guess the highlow number")

    def choose_postmemes(self, message_id, custom_id, value):
        data = {
            "message_id": message_id,
            "data": {
                "component_type": 3,
                "custom_id": custom_id,
                "type": 3,
                "values": [value],
                "name": value,
            },
        }
        data.update(self.payload(3))
        return data

    @isFocus
    def postmemes(self):
        data = {
            "data": {
                "version": "1022917002794381384",
                "id": "1011560370911072263",
                "name": "postmemes",
            }
        }
        data.update(self.payload())
        self.command2(data)

        res = self.api.retrieve_message()

        try:
            message_id = res["id"]
            custom_id1 = res["components"][0]["components"][0][
                "custom_id"
            ]  # select platform
            custom_id2 = res["components"][1]["components"][0][
                "custom_id"
            ]  # select meme type
            post_btn = res["components"][2]["components"][0]["custom_id"]  # post button

            platforms = ["discord", "reddit", "twitter", "facebook"]
            meme_types = ["Fresh", "Repost", "Intellectual", "Copypasta", "Kind"]

            self.command2(
                self.choose_postmemes(message_id, custom_id1, random.choice(platforms))
            )

            self.command2(
                self.choose_postmemes(message_id, custom_id2, random.choice(meme_types))
            )

            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": post_btn,
                    "name": "post memes",
                },
            }

            data.update(self.payload(3))

            self.command2(data)
        except Exception as e:
            print(e)
            print("Error cant postmemes")

    @isFocus
    def search(self):
        data = {
            "data": {
                "version": "1022917002987315252",
                "id": "1011560371267579935",
                "name": "search",
            }
        }
        data.update(self.payload())
        self.command2(data)

        res = self.api.retrieve_message()

        choose = [
            "ZomB's Grave",
            "Toxic waste plant",
            "Soul's chamber",
            "Tesla",
            "Dog",
            "Grass",
            "Phoenix pits",
            "Twitch",
            "Police officer",
            "McDonald's",
            "Sewer",
            "Ocean",
            "Pantry",
            "Mailbox",
            "Area51",
            "Fridge",
            "Hospital",
            "Basement",
            "Bathroom",
            "Beehive",
            "Kitchen",
            "Stock Market",
            "Book",
            "Dresser",
            "Briefcase",
            "Glovebox",
            "Street	",
            "Bushes",
            "Car",
            "Vacuum",
            "Dark room",
            "Aeradella's home",
            "Air",
            "Attic",
            "Bank",
            "Bed",
            "Bus",
            "Car",
            "Coat",
            "Computer",
            "Crawlspace",
            "Dumpster",
            "Garage",
            "God's Own Place",
            "Immortals Dimension",
            "Lego bin",
            "Movie Theater",
            "Purse",
            "Shoe",
            "Sink",
            "Supreme Court",
            "Twitter",
            "Tree",
            "Uber",
            "Van",
        ]
        self.choose_components(choose, res)

    @isFocus
    def crime(self):
        data = {
            "data": {
                "version": "1022917002878259283",
                "id": "1011560371078832202",
                "name": "crime",
            }
        }
        data.update(self.payload())
        self.command2(data)

        res = self.api.retrieve_message()

        choose = [
            "Tax evasion",
            "DUI",
            "Driving under the influence (DUI)",
            "Piracy",
            "Eating A Hot Dog Sideways",
            "Hacking",
            "Treason",
            "Bank robbing",
            "Murder",
            "Boredom",
            "Cyber bullying",
            "Drug distribution",
            "Identity theft",
            "Littering",
            "Shoplifting",
            "Vandalism",
            "Trespassing",
            "Fraud",
            "Arson",
        ]
        self.choose_components(choose, res)

    @isFocus
    async def beg(self):
        data = {
            "data": {
                "version": "1022917002878259280",
                "id": "1011560371041095699",
                "name": "beg",
            }
        }
        data.update(self.payload())
        await self.command(data)

    @isFocus
    async def use_item(self, item_name, time):
        data = {
            "data": {
                "version": "1022917002987315258",
                "id": "1011560371267579941",
                "name": "use",
                "options": [
                    {"type": 3, "name": "item", "value": item_name.capitalize()}
                ],
            }
        }
        data.update(self.payload())
        await self.command(data)
        asyncio.create_task(self.schedule(time, self.use_item, item_name, time))

    @isFocus
    async def vote(self):
        data = {
            "data": {
                "version": "1034827622045192221",
                "id": "1011560370994954286",
                "name": "vote",
            }
        }
        data.update(self.payload())
        await self.command(data)

        res = self.api.retrieve_message()
        link_dbl = res["components"][0]["components"][0]["url"]
        link_topgg = res["components"][0]["components"][1]["url"]

        asyncio.create_task(Vote(self.auth_token, link_dbl).run())
        asyncio.create_task(Vote(self.auth_token, link_topgg).run())

        asyncio.create_task(self.schedule(12 * 60 * 60, self.vote))

    @isFocus
    async def adventure(self):
        print("adventure", self.username)
        data = {
            "data": {
                "version": "1022917002848903204",
                "id": "1011560371041095695",
                "name": "adventure",
            }
        }
        data.update(self.payload())
        self.api.send_interact(data)

        allQuestion = [
            ["You uh, just came across a pair of Odd Eyes floating around", ["Flee"]],
            [
                "You got abducted by a group of aliens, who are trying to probe you. What do you do?",
                ["Sit back and enjoy"],
            ],
            ["A friendly alien approached you slowly. What do you do?", ["Probe"]],
            [
                "This planet seems to be giving off radioactive chemicals. What do you do?",
                ["Distant Scan"],
            ],
            ["Oh my god even in space you cannot escape it", ["Never"]],
            ["You're picking up a transmission from deep space!", ["*<)\#%':](.)#"]],
            ["You ran out of fuel! What next?", ["Urinate"]],
            ["A small but wise green alien approaches you", ["Do"]],
            ["You encountered someone named Dank Sidious, what do you do?", ["Do it"]],
            ["You accidentally bumped into the Webb Telescope. Oh god.", ["Flee"]],
            ["You see a shooting star!", ["Wish"]],
            ["You found a strange-looking object. What do you do?", ["Ignore"]],
            [
                "Whaaaat!? You found a space kitchen! It looks like it is full of shady stuff. What do you do?",
                ["Inspect"],
            ],
            ["You flew past a dying star", ["Flee"]],
        ]

        await asyncio.sleep(2)
        try:
            res = self.check_massage(message="adventure")

            if not "footer" in (res["embeds"][0]):
                print("gak ada footer", self.username)
                print(res)
                # self.is_focus = False
                await self.start_new_adventure(res)

            elif "🚀" in res["embeds"][0]["footer"]["text"]:
                print("ada footer", self.username)
                print(res)
                question = res["embeds"][0]["description"]
                answer = ""
                for i in allQuestion:
                    if i[0].lower() in question.lower():
                        answer = i[1]
                print("dapat answer", answer, self.username)
                self.choose_components(answer, res)
                print("berhasil answer", self.username)
                asyncio.create_task(self.schedule(5 * 60, self.adventure))
            else:
                print("gak ada apa2", self.username)
                print(res)
                # asyncio.create_task(self.schedule(4 * 60, self.adventure))
                # self.is_focus = False
                await self.start_new_adventure(res)

        except:
            print("Error adventure cant read")
            asyncio.create_task(self.schedule(4 * 60, self.adventure))
            # await self.adventure()

    async def start_new_adventure(self, res):
        if len(res["components"]) >= 2 and len(res["components"][1]["components"][0]):
            print("start new adventure", self.username)
            custom_id = res["components"][1]["components"][0]["custom_id"]
            message_id = res["id"]
            data = {
                "message_id": message_id,
                "message_flags": 0,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id,
                    "name": "start button",
                },
            }
            data.update(self.payload(3))
            self.command2(data)

            res = self.api.retrieve_message()
            message_id = res["id"]
            custom_id = res["components"][2]["components"][1]["custom_id"]
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id,
                    "name": "choose all item",
                },
            }
            data.update(self.payload(3))
            self.command2(data)

            res = self.api.retrieve_message()
            message_id = res["id"]
            custom_id = res["components"][1]["components"][1]["custom_id"]
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id,
                    "name": "unselect the pepe trophy",
                },
            }
            data.update(self.payload(3))
            self.command2(data)

            res = self.api.retrieve_message()

            message_id = res["id"]
            custom_id = res["components"][2]["components"][0]["custom_id"]
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id,
                    "name": "start adventure",
                },
            }
            data.update(self.payload(3))
            self.command2(data)
            # await self.adventure()

        asyncio.create_task(self.schedule(5 * 60, self.adventure))

    def choose_components(self, arr, res={}):
        if res == {}:
            res = self.api.retrieve_message()

        message_id = res["id"]
        try:
            components = res["components"][0]["components"]
            choose = arr
            for j in choose:
                for i in components:
                    if j.lower() == i["label"].lower():
                        custom_id = i["custom_id"]
                        data = {
                            "message_id": message_id,
                            "data": {
                                "component_type": 2,
                                "custom_id": custom_id,
                                "name": i["label"],
                            },
                        }
                        data.update(self.payload(3))
                        self.command2(data)
                        break
                else:
                    continue
                break
        except:
            # raise Exception("Error choose components", self.username)
            print("Error choose components", self.username)

    def choose_components_emoji(self, arr, res={}):
        if res == {}:
            res = self.api.retrieve_message()
        message_id = res["id"]
        # print(res)
        try:
            components = (
                res["components"][0]["components"] + res["components"][1]["components"]
            )
            choose = arr
            # print(choose)
            for j in choose:
                for i in components:
                    # print(i['emoji']['name'])
                    if j == i["emoji"]["name"]:
                        custom_id = i["custom_id"]
                        # print(custom_id)
                        data = {
                            "message_id": message_id,
                            "data": {
                                "component_type": 2,
                                "custom_id": custom_id,
                            },
                        }
                        data.update(self.payload(3))
                        self.command2(data, message=i["emoji"]["name"])
                        break
                else:
                    continue
                break

        except:
            raise Exception("Error choose components", self.username)

    @isFocus
    async def stream(self):

        data = {
            "data": {
                "version": "1022917002987315255",
                "id": "1011560371267579938",
                "name": "stream",
            }
        }
        data.update(self.payload())
        self.command2(data)

        res = self.api.retrieve_message()

        message_id = res["id"]
        try:
            custom_id = res["components"][0]["components"][0]["custom_id"]
            isStreaming = False
            for i in res["embeds"][0]:
                if i == "description":
                    content = res["embeds"][0]["description"]
                    if "without any interaction" in content:
                        isStreaming = True
                        custom_id = [
                            res["components"][0]["components"][0]["custom_id"],
                            res["components"][0]["components"][1]["custom_id"],
                            res["components"][0]["components"][2]["custom_id"],
                            res["components"][0]["components"][4]["custom_id"],
                        ]
                        if self.stream_num % 6 == 0:
                            self.stream_action(message_id, custom_id, 1)
                        elif self.stream_num % 13 == 0:
                            if random.randint(0, 10) <= 7:
                                self.stream_action(message_id, custom_id, 3)
                            self.stream_action(message_id, custom_id, 4)
                        else:
                            self.stream_action(message_id, custom_id, 2)
                        self.stream_num = self.stream_num + 1
        except:
            print("Erorr to read stream message")

        try:
            if not isStreaming:
                self.start_new_stream(message_id, custom_id)
        except:
            print("Error Start stream", self.username)

        asyncio.create_task(self.schedule(10 * 60, self.stream))

    def start_new_stream(self, message_id, custom_id):

        # go live
        data = {
            "message_id": message_id,
            "data": {
                "component_type": 2,
                "custom_id": custom_id,
                "name": "start stream",
            },
        }
        data.update(self.payload(3))
        self.command2(data)

        # choose game

        res = self.api.retrieve_message()

        custom_id = res["components"][0]["components"][0]["custom_id"]
        all_game = []
        options = res["components"][0]["components"][0]["options"]

        for i in options:
            all_game.append(i["value"])

        choose_game = random.choice(all_game)

        data = {
            "message_id": message_id,
            "data": {
                "component_type": 3,
                "custom_id": custom_id,
                "type": 3,
                "values": [choose_game],
                "name": f"choose {choose_game}",
            },
        }
        data.update(self.payload(3))
        self.command2(data)

        # start live
        res = self.api.retrieve_message()
        custom_id = res["components"][1]["components"][0]["custom_id"]
        data = {
            "message_id": message_id,
            "data": {
                "component_type": 2,
                "custom_id": custom_id,
                "name": f"start {choose_game}",
            },
        }
        data.update(self.payload(3))
        self.command2(data)

        res = self.api.retrieve_message()

        message_id = res["id"]
        custom_id = [
            res["components"][0]["components"][0]["custom_id"],
            res["components"][0]["components"][1]["custom_id"],
            res["components"][0]["components"][2]["custom_id"],
        ]

        self.stream_action(message_id, custom_id, 2)

    def stream_action(self, message_id, custom_id, choose):
        data = {}
        if choose == 1:
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id[choose - 1],
                    "name": "run ad stream",
                },
            }
        elif choose == 2:
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id[choose - 1],
                    "name": "read chat stream",
                },
            }
        elif choose == 3:
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id[choose - 1],
                    "name": "collect donation stream",
                },
            }
        elif choose == 4:
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id[choose - 1],
                    "name": "collect donation stream",
                },
            }

        data.update(self.payload(3))
        self.command2(data)

    async def mini_games(self, res={}):

        if res == {}:
            res = self.api.retrieve_message()

        if not "description" in (res["embeds"][0]):
            print("dont have description")
            return
        choose = []
        desc = res["embeds"][0]["description"]

        if "Dunk the ball!" in desc:
            print("dunk the ball")
            b = desc.split("\n")
            c = b[2]

            if c.count("<:emptyspace:827651824739156030>") == 0:
                choose.append("left")
            elif c.count("<:emptyspace:827651824739156030>") == 1:
                choose.append("middle")
            elif c.count("<:emptyspace:827651824739156030>") == 2:
                choose.append("right")

        elif "Hit the ball!" in desc:
            print("hit the ball")
            b = desc.split("\n")
            c = b[2]

            if c.count("<:emptyspace:827651824739156030>") == 0:
                choose.append("middle")
            elif c.count("<:emptyspace:827651824739156030>") == 1:
                choose.append("right")
            elif c.count("<:emptyspace:827651824739156030>") == 2:
                choose.append("left")

        elif "Catch the fish!" in desc:
            print("catch the fish")
            b = desc.split("\n")
            c = b[1]

            if c.count("<:emptyspace:827651824739156030>") == 0:
                choose.append("left")
            elif c.count("<:emptyspace:827651824739156030>") == 1:
                choose.append("middle")
            elif c.count("<:emptyspace:827651824739156030>") == 2:
                choose.append("right")

        elif "Dodge the Fireball!" in desc:
            print("dodge the fireball")
            b = desc.split("\n")
            c = b[2]

            if c.count("<:emptyspace:827651824739156030>") == 0:
                choose.append("right")
                # await asyncio.sleep(1)
            elif c.count("<:emptyspace:827651824739156030>") == 1:
                choose.append("left")
            elif c.count("<:emptyspace:827651824739156030>") == 2:
                choose.append("middle")
                # await asyncio.sleep(1)

        elif "emoji" in desc:
            print("Look at the emoji closely!")
            b = desc.split("\n")
            emoji = b[1]
            # print(emoji)
            await asyncio.sleep(5)
            # time.sleep(5)
            res = self.api.retrieve_message()
            # print(res)
            self.choose_components_emoji([emoji], res)

        elif "color" in desc:
            print("Look at each color next to the words closely")
            b = desc.split()
            c = len(b)
            # print(c) ## can 9 length
            try:
                colors = [b[9], b[10], b[11], b[12], b[13], b[14]]

                await asyncio.sleep(6)
                # time.sleep(5)
                res = self.api.retrieve_message()
                desc = res["embeds"][0]["description"]
                b = desc.split("`")
                ask = b[1]
                # print(res)
                # print(b[1])

                for i in range(len(colors)):
                    if ask in colors[i]:
                        print(colors[i - 1])
                        answer = colors[i - 1].split(":")[1]
                        self.choose_components([answer], res)
            except:
                print("Error cant choose color")

            return

        elif "Remember words order!" in desc:
            print("Remember words order!")
            b = desc.split("\n")
            await asyncio.sleep(5)
            # time.sleep(5)
            res = self.api.retrieve_message()
            for i in range(len(b)):
                if i != 0:
                    self.choose_components([b[i].strip("`")], res)

            return

        # dodge the worm

        if len(choose) != 0:
            print("time to choose", choose)
            self.choose_components(choose, res)

    @isFocus
    async def work_shift(self):
        data = {
            "data": {
                "version": "1022917002987315259",
                "id": "1011560371267579942",
                "name": "work",
                "options": [
                    {
                        "type": 1,
                        "name": "shift",
                    }
                ],
            }
        }
        data.update(self.payload())
        self.command2(data)

        res = self.api.retrieve_message()

        try:
            await self.mini_games(res)
        except:
            print("Error cant mini games", self.username)

        asyncio.create_task(self.schedule(1 * 60 * 60, self.work_shift))

    async def auto(self):
        try:
            while True:
                await self.fish()
                await asyncio.sleep(4)
                await self.dig()
                await asyncio.sleep(4)
                await self.hunt()
                await asyncio.sleep(4)
                await self.beg()
                await asyncio.sleep(4)
                await self.highlow()
                await asyncio.sleep(4)
                await self.search()
                await asyncio.sleep(4)
                await self.crime()
                await asyncio.sleep(4)
                await self.postmemes()
                await asyncio.sleep(4)
        except:
            await self.auto()

    @isFocus
    async def balance(self):
        data = {
            "data": {
                "version": "1022917002848903206",
                "id": "1011560371041095697",
                "name": "balance",
            }
        }
        data.update(self.payload())
        await self.command(data)
        res = self.api.retrieve_message()
        print(res)
        regex = "(?<=Wallet\*\*: ⏣ )[0-9,]+"
        balance = re.findall(regex, res["embeds"][0]["description"])[0]
        print(balance)

    @isFocus
    async def blackjack(self, bet):

        try:
            await self.balance()
            data = {
                "data": {
                    "version": "1011560371603132435",
                    "id": "1011560371078832199",
                    "name": "blackjack",
                    "type": 1,
                    "options": [{"type": 3, "name": "bet", "value": bet}],
                }
            }
            data.update(self.payload())
            await self.command(data)

            for i in range(50):
                res = self.check_massage("blackjack")
                if not res:
                    break

                if "description" not in res["embeds"][0]:
                    await self.choose_blackjack(res)
                    continue

                desc = res["embeds"][0]["description"]

                if "payout" in desc.lower():
                    await self.choose_blackjack_menu("play again", res)
        except:
            print("Error blackjack")
        asyncio.create_task(self.schedule(100, self.blackjack, "7k"))

    async def choose_blackjack(self, res={}):
        if res == {}:
            res = self.api.retrieve_message()

        message_id = res["id"]

        regex = "(?<=\s)[JQKA0-9]+(?=`)|[\?](?=\s`\])"

        dealer = re.findall(regex, res["embeds"][0]["fields"][0]["value"])
        player = re.findall(regex, res["embeds"][0]["fields"][1]["value"])
        action = blakcjackSolver(dealer, player)
        print(dealer, player)

        if action == "H":
            action = "Hit"
        elif action == "S":
            action = "Stand"
        elif action == "D":
            action = "Double"
        elif action == "DS":
            action = "Double"
        elif action == "Y":
            action = "Hit"
        elif action == "Y/N":
            action = "Hit"
        elif action == "SUR":
            action = "Surrender"

        choose = action

        if choose.lower() in "surrender":
            custom_id = res["components"][1]["components"][0]["custom_id"]
            data = {
                "message_id": message_id,
                "data": {
                    "component_type": 2,
                    "custom_id": custom_id,
                    "name": "surrender",
                },
            }
            data.update(self.payload(3))
            self.command2(data)

        # try:
        components = res["components"][0]["components"]
        for i in components:
            if choose.lower() in i["label"].lower():
                custom_id = i["custom_id"]
                data = {
                    "message_id": message_id,
                    "data": {
                        "component_type": 2,
                        "custom_id": custom_id,
                        "name": i["label"],
                    },
                }
                data.update(self.payload(3))
                self.command2(data)

                break

    async def choose_blackjack_menu(self, choose, res={}):
        if res == {}:
            res = self.api.retrieve_message()
        # self.counter += 1
        message_id = res["id"]
        option = ["play again", "end", "switch table"]
        # try:
        if self.counter == 20:
            choose = "end"
        components = res["components"][0]["components"]
        for i in components:
            if choose.lower() in i["label"].lower():
                custom_id = i["custom_id"]
                data = {
                    "message_id": message_id,
                    "data": {
                        "component_type": 2,
                        "custom_id": custom_id,
                        "name": i["label"],
                    },
                }
                data.update(self.payload(3))
                self.command2(data)

                break
