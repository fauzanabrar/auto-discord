import asyncio

from src.tatsu.TatsuAuto import *
from src.dank.DankAuto import *
from src.owo.OwoAuto import *
import threading



async def auto_tatsu(auth_token, channel_id):
    tatsu = TatsuAuto(auth_token, channel_id)
    await tatsu.run()

def auto_dank(auth_token, url, application_id, session_id):
    dank = DankAuto(auth_token, url, application_id, session_id)
    asyncio.run(dank.run())

async def auto_owo(auth_token, channel_id):
    owo = OwoAuto(auth_token, channel_id)
    await owo.run()

async def main():
    start = time.perf_counter()

    f = open("init3.json")
    data_account = json.load(f)

    for i in data_account:
        # access all the auth token
        auth_token = i['auth_token']

        # access all the channel id (dank, owo, tatsu) and run the auto
        for j in i['channel_id']:
            if "dank" in j:
                dank_setup = ["","",""] # url, application_id, session_id
                for k in i['channel_id'][str(j)]:
                    if "url" in k:
                        dank_setup[0] = i['channel_id'][str(j)][str(k)]
                    elif "application_id" in k:
                        dank_setup[1] = i['channel_id'][str(j)][str(k)]
                    elif "session_id" in k:
                        dank_setup[2] = i['channel_id'][str(j)][str(k)]
                # dank_auto = asyncio.create_task(auto_dank(auth_token, dank_setup[0], dank_setup[1], dank_setup[2]))
                t1 = threading.Thread(target=auto_dank, args=(auth_token, dank_setup[0], dank_setup[1], dank_setup[2]))
                t1.start()

            elif "owo" in j:
                owo_channel_id = i['channel_id'][str(j)]
                # owo_auto = asyncio.create_task(auto_owo(auth_token, owo_channel_id))
            elif "tatsu" in j:
                tatsu_channel_id = i['channel_id'][str(j)]
                # tatsu_auto = asyncio.create_task(auto_tatsu(auth_token, tatsu_channel_id))

    t1.join()
    # await tatsu_auto
    # await dank_auto
    # await owo_auto
    await asyncio.sleep(2*60*60)

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')




if __name__ =="__main__":
    start = time.perf_counter()

    f = open("init3.json")
    data_account = json.load(f)

    for i in data_account:
        # access all the auth token
        auth_token = i['auth_token']

        # access all the channel id (dank, owo, tatsu) and run the auto
        for j in i['channel_id']:
            if "dank" in j:
                dank_setup = ["", "", ""]  # url, application_id, session_id
                for k in i['channel_id'][str(j)]:
                    if "url" in k:
                        dank_setup[0] = i['channel_id'][str(j)][str(k)]
                    elif "application_id" in k:
                        dank_setup[1] = i['channel_id'][str(j)][str(k)]
                    elif "session_id" in k:
                        dank_setup[2] = i['channel_id'][str(j)][str(k)]
                t1 = threading.Thread(target=auto_dank, args=(auth_token, dank_setup[0], dank_setup[1], dank_setup[2]))
                t1.start()

            elif "owo" in j:
                owo_channel_id = i['channel_id'][str(j)]
                # owo_auto = asyncio.create_task(auto_owo(auth_token, owo_channel_id))
            elif "tatsu" in j:
                tatsu_channel_id = i['channel_id'][str(j)]
                # tatsu_auto = asyncio.create_task(auto_tatsu(auth_token, tatsu_channel_id))

    t1.join()


    end = time.perf_counter()
    print(f'It took {round(end - start, 0)} second(s) to complete.')