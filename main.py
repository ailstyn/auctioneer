import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!auction":
        name = input("What would you like to bid?")
        keyword = input("What is the keyword?")
        threshhold = input("What is the minimum bid window?")
        restriction = input("How is the bidding restricted?")
        enddate = input("What day does the bidding end?")
        endtime = input("What time will the bidding end?")
        itemlink = input("Insert a link to the item")

    print(
        f"{name} DKP auction! Closes {enddate} at {endtime} EST. Please bid DKP in this channel. @raiders - green @dkpauction - Green"
        f"/n/n{itemlink}"
        f"/n*Bid format: {keyword} 1dkp main (or 2main)"
        f"/n*Not for resale. Please bid only to use this item. You may return it to the guild bank for your DKP back."
        f"/n*As usual, no joke bids."
        f"/n*{restriction}"
        f"/n*Closes {enddate} at {endtime} EST. Bids during the last {threshhold} automatically extend bidding period."
        f"/n*This channel should be bids only - questions and discussion in #raid-chat-green")


client.run(TOKEN)
