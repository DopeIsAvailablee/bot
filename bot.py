import discord
from discord.ext import commands
import subprocess

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def create_channel(ctx, channel_name: str):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.command()
async def start(ctx):
    output = subprocess.run(["path/to/minecraft_server_start_command"], capture_output=True, text=True)
    await ctx.send(output.stdout)

@bot.command()
async def restart(ctx):
    output = subprocess.run(["path/to/minecraft_server_restart_command"], capture_output=True, text=True)
    await ctx.send(output.stdout)

@bot.command()
async def stop(ctx):
    output = subprocess.run(["path/to/minecraft_server_stop_command"], capture_output=True, text=True)
    await ctx.send(output.stdout)

bot.run('YOUR_DISCORD_BOT_TOKEN')
