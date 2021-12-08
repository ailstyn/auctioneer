import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = "!")

@client.event()
async def on_message("how"):
    await ctx.send(f"name, keyword, restriction, duration (days), end time, "
        f"threshold time (hours), item link. Class/race restrictions and the "
        f"item link must be wrapped in quotes."
        )    

@bot.command()
async def newauction(ctx, name, keyword, restriction, endday, endtime, threshold, itemlink):
    await ctx.send(f"You are making a new auction for {name}. "
        f"Members can bid by using the {keyword} keyword. "
        f"You have declared only {restriction} may place bid (auctioneer does not track this). "
        f"Bidding will end after {endday} days at {endtime}, "
        f"bidding in the last {threshold} hours will reset the timer to {threshold}. "
        f"The link for the item is {itemlink}."
                    )

    print(
        f"{name} DKP auction! Closes {enddate} at {endtime} EST. Please bid DKP in this channel. @raiders - green @dkpauction - Green"
        f"/n/n{itemlink}"
        f"/n*Bid format: {keyword} 1dkp main (or 2main)"
        f"/n*Not for resale. Please bid only to use this item. You may return it to the guild bank for your DKP back."
        f"/n*As usual, no joke bids."
        f"/n*Bids are restricted to:{restriction}"
        f"/n*Closes {enddate} at {endtime} EST. Bids during the last {threshold} automatically extend bidding period."
        f"/n*This channel should be bids only - questions and discussion in #raid-chat-green")


client.run(TOKEN)
