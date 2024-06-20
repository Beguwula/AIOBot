import json
import discord
from discord.ext import commands

with open('modules.json') as module_list_file:
    module_list = json.load(module_list_file)

with open('config.json') as config_file:
        config = json.load(config_file)

with open('token.key') as key_file:
        key = key_file.readline()

if module_list["Welcomer"] == True:
    channel = "GuildChannel"

intents = discord.Intents().all()
intents.guild_typing = False
intents.presences = False

bot = commands.Bot(command_prefix=config["PREFIX"], intents=intents)

@bot.event
async def on_member_join(member):
    if module_list["Welcomer"] == True:
        if config["WELCOMER_CHANNEL_MESSAGE_ENABLED"] == True:
            channel_id = config.get("WELCOMER_CHANNEL_ID")
            channel = bot.get_channel(channel_id)
            welcome_message = config.get("WELCOMER_CHANNEL_MESSAGE").format(mention=member.mention)
            await channel.send(welcome_message)
        try:
            dm_message = config.get("WELCOMER_DM_MESSAGE")
            await member.send(dm_message)
        except:
            print("User probably has dms off...")

bot.run(key)
