import disnake
import json
import logging
import os
import sys
from disnake.ext import commands
from disnake.ext.commands import Cog
from disnake import Activity, ActivityType
from datetime import datetime
# from cogs.help_command import HelpCog

logger = logging.getLogger('disnake')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
logger.addHandler(handler)

intents = disnake.Intents.all()
intents.members = True

with open("configuration.json", "r") as config:
  data = json.load(config)
  token = data["token"]
  prefix = data["prefix"]

bot = commands.Bot(prefix, intents = intents, help_command=None)
# bot.help_command = HelpCog()
extensions = ["cogs.ping", "cogs.owner", "cogs.utils", "cogs.help_command", "cogs.sous", "cogs.gpt", "cogs.mod"]
for extension in extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}({bot.user.id}).")      
    print('------')
    await bot.change_presence(activity=Activity(type=ActivityType.watching, name='code Clvr.py'))

@bot.event
async def on_command_error(ctx, error):
   # if isinstance(error, commands.CommandNotFound):
     #   return  # Игнорировать ошибку, если команда не найдена

    # Создание сообщения об ошибке
    error_embed = disnake.Embed(
        title=':x: Ошибка!',
        description=str(error),
        color=0xFF0000  # Красный цвет
    )
    await ctx.reply(embed=error_embed)

bot.run(token)
