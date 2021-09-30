
import os
import random

from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
dl_trigger = "$dl"

@client.event
async def on_message(message):

    if message.content.startswith(dl_trigger):
        request = message.content.strip(dl_trigger)
        full_request = ["+" + word if index == 0 else word for index, word in enumerate(request.split())]
        url = "https://www3.yggtorrent.nz/engine/search?name="+ full_request.join() + "eragon&description=&file=&uploader=&category=all&sub_category=&do=search&order=desc&sort=seed"

