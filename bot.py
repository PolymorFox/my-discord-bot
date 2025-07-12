import discord
from discord.ext import commands
import logging
import argparse
import os

parser = argparse.ArgumentParser(description="A simple discord bot with a few commands")
parser.add_argument("--token",type=str)
args = parser.parse_args()

token = args.token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)
log_handler = logging.FileHandler(filename="discord.log",encoding="UTF-8",mode="w")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f"Bot has logged into {guild}")
        server_name = guild.name

@bot.command()
async def greet(ctx):
   await ctx.channel.send(f"{ctx.author.mention} Greetings {ctx.author.name}")

@bot.command()
async def info(ctx, * , member: discord.Member):
    if member is None:
        member = ctx.author

    if member.joined_at is None:
        message = f"""{member.mention}
            Username: {member.name}
            Display Name: {member.display_name}

        """
        await ctx.channel.send(message)
    else:
        join_date = member.joined_at
        message = f"""{ctx.author.mention}
            Username: {member.name}
            Display Name: {member.display_name}
            Join Date: {join_date}

        """
        await ctx.channel.send(message)

@bot.command()
async def dump(ctx,*,channel: discord.TextChannel):
    channel = channel or ctx.channel
    history_file_path = f"history_{channel.name}.txt"

    with open(history_file_path,"w") as history:
        async for message in channel.history(limit=None):
            history.write(f"User {message.author} sent {message.content} at {message.created_at}\n")
        
        history_full_path = os.path.abspath(history_file_path)
        file = discord.File(history_full_path)
        await ctx.author.send(f"{ctx.author.mention} History of {channel.name} on guild {server_name}",file=file)
        os.remove(history_file_path)

bot.run(token=token,log_handler=log_handler)