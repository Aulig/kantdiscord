import os

import discord
from discord.ext import commands

# this config file is gitignored because it contains secrets
from config import TOKEN

initial_extensions = ['cogs.random_stuff',
                      'cogs.voice_chat']

bot = commands.Bot(command_prefix=">")

if __name__ == '__main__':

    # gameserver.gratis seems to have ffmpeg preinstalled :)
    # import platform
    # if platform.system() == "Linux":
    #     os.system("sudo apt install ffmpeg")

    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    await bot.change_presence(activity=discord.Game(name='Amogus'))


bot.run(TOKEN)