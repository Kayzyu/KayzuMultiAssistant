import asyncio
import os
import time
from os import listdir, mkdir

import heroku3
from aiohttp import ClientSession
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from motor.motor_asyncio import AsyncIOMotorClient as Bot
from rich.console import Console
from rich.table import Table

from config import (ASSISTANT_PREFIX, DURATION_LIMIT_MIN, LOG_GROUP_ID,
                    LOG_SESSION)
from config import MONGO_DB_URI as mango
from config import (MUSIC_BOT_NAME, OWNER_ID, STRING1, STRING2, SUDO_USERS, get_queue)
from Yukki.Core.Clients.cli import (ASS_CLI_1, ASS_CLI_2, LOG_CLIENT, app)
from Yukki.Utilities.changers import time_to_seconds
from Yukki.Utilities.tasks import install_requirements

loop = asyncio.get_event_loop()
console = Console()


### Modules
MOD_LOAD = []
MOD_NOLOAD = []

### Mongo DB
MONGODB_CLI = Bot(mango)
db = MONGODB_CLI.Yukki

### Boot Time
boottime = time.time()

### Clients
app = app
ASS_CLI_1 = ASS_CLI_1
ASS_CLI_2 = ASS_CLI_2
LOG_CLIENT = LOG_CLIENT
aiohttpsession = ClientSession()

### Config
SUDOERS = SUDO_USERS
OWNER_ID = OWNER_ID
LOG_GROUP_ID = LOG_GROUP_ID
MUSIC_BOT_NAME = MUSIC_BOT_NAME
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ASSISTANT_PREFIX = ASSISTANT_PREFIX

### Bot Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""

### Assistant Info
ASSIDS = []
ASSID1 = 0
ASSNAME1 = ""
ASSUSERNAME1 = ""
ASSMENTION1 = ""
ASSID2 = 0
ASSNAME2 = ""
ASSUSERNAME2 = ""
ASSMENTION2 = ""
random_assistant = []


async def initiate_bot():
    global SUDOERS, OWNER_ID, ASSIDS
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID1, ASSNAME1, ASSMENTION1, ASSUSERNAME1
    global ASSID2, ASSNAME2, ASSMENTION2, ASSUSERNAME2
    global Heroku_cli, Heroku_app
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "\x59\x75\x6b\x6b\x69\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x3a\x20\x54\x68\x65\x20\x4d\x6f\x73\x74\x20\x41\x64\x76\x61\x6e\x63\x65\x64\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74"
    )
    console.print(header)
    with console.status(
        "[magenta] Yukki Music Bot Booting...",
    ) as status:
        console.print("┌ [red]Booting Up The Clients...\n")
        await app.start()
        console.print("└ [green]Booted Bot Client")
        console.print("\n┌ [red]Booting Up The Assistant Clients...")
        if STRING1 != "None":
            await ASS_CLI_1.start()
            random_assistant.append(1)
            console.print("├ [yellow]Booted Assistant Client")
        if STRING2 != "None":
            await ASS_CLI_2.start()
            random_assistant.append(2)
            console.print("├ [yellow]Booted Assistant Client 2")
        if LOG_SESSION != "None":
            console.print("\n┌ [red]Booting Logger Client")
            await LOG_CLIENT.start()
            console.print("└ [green]Logger Client Booted Successfully!")
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "cache" not in listdir():
            mkdir("cache")
        if "search" not in listdir():
            mkdir("search")
        console.print("\n┌ [red]Loading Clients Information...")
        getme = await app.get_me()
        BOT_ID = getme.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        if STRING1 != "None":
            getme1 = await ASS_CLI_1.get_me()
            ASSID1 = getme1.id
            ASSIDS.append(ASSID1)
            ASSNAME1 = (
                f"{getme1.first_name} {getme1.last_name}"
                if getme1.last_name
                else getme1.first_name
            )
            ASSUSERNAME1 = getme1.username
            ASSMENTION1 = getme1.mention
        if STRING2 != "None":
            getme2 = await ASS_CLI_2.get_me()
            ASSID2 = getme2.id
            ASSIDS.append(ASSID2)
            ASSNAME2 = (
                f"{getme2.first_name} {getme2.last_name}"
                if getme2.last_name
                else getme2.first_name
            )
            ASSUSERNAME2 = getme2.username
            ASSMENTION2 = getme2.mention
        console.print("\n┌ [red]Loading Sudo Users...")
        sudoersdb = db.sudoers
        sudoers = await sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in SUDOERS:
            if user_id not in sudoers:
                sudoers.append(user_id)
                await sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        SUDOERS = (SUDOERS + sudoers + OWNER_ID) if sudoers else SUDOERS
        console.print("└ [green]Loaded Sudo Users Successfully!\n")
        

loop.run_until_complete(initiate_bot())


def init_db():
    global db_mem
    db_mem = {}


init_db()
