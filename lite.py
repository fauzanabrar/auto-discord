import asyncio

from src.ninja_sage.ninja_sage import *
from src.adventure_frontier.AFAuto import *
import argparse



async def auto_af(auth_token, url, application_id, session_id):
    af = AFAuto(auth_token, url, application_id, session_id)
    await af.run()


async def auto_ninja_sage(auth_token, channel_id):
    af = NinjaSageAuto(auth_token, channel_id)
    await af.run()


async def main(task_type):
    start = time.perf_counter()

    f = open("init.json")
    data_account = json.load(f)

    tasks = []

    for i in data_account:
        # access all the auth token
        auth_token = i["auth_token"]

        # access all the channel id (dank, owo, tatsu) and run the auto
        for j in i["channel_id"]:
            if "ninja_sage" in j and task_type == "ns":
                ninja_sage_channel_id = i["channel_id"][str(j)]
                # ns_auto = asyncio.create_task(auto_ninja_sage(auth_token, ninja_sage_channel_id))
                tasks.append(auto_ninja_sage(auth_token, ninja_sage_channel_id))

            elif "adventure_frontier" in j and task_type == "af":
                af_setup = ["", "", ""]  # url, application_id, session_id
                for k in i["channel_id"][str(j)]:
                    if "url" in k:
                        af_setup[0] = i["channel_id"][str(j)][str(k)]
                    elif "application_id" in k:
                        af_setup[1] = i["channel_id"][str(j)][str(k)]
                    elif "session_id" in k:
                        af_setup[2] = i["channel_id"][str(j)][str(k)]
                # af_auto = asyncio.create_task(auto_af(auth_token, af_setup[0], af_setup[1], af_setup[2]))
                tasks.append(auto_af(auth_token, af_setup[0], af_setup[1], af_setup[2]))

    # Run all tasks concurrently
    await asyncio.gather(*tasks)

    # await asyncio.sleep(2*60*60)

    end = time.perf_counter()
    print(f"It took {round(end-start,0)} second(s) to complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific tasks.")
    parser.add_argument(
        "tasks",
        nargs="+",  # Allows multiple arguments
        choices=["dank", "owo", "tatsu", "ns", "af"],
        help="Specify the tasks to run (e.g., 'ns af').",
    )
    args = parser.parse_args()

    async def run_multiple_tasks(task_list):
        await asyncio.gather(*(main(task) for task in task_list))

    asyncio.run(run_multiple_tasks(args.tasks))