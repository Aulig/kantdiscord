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


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "N":
        await message.channel.send("https://images-ext-2.discordapp.net/external/jMogcAO36oreMXMIcdomxY5KiIg4zQx_d188bA674yM/%3Fcb%3D20190414152105/https/static.wikia.nocookie.net/doawk/images/5/59/Manny_says_ploopy.jpg/revision/latest")
    if "janny" in message.content.lower():
        await message.channel.send("https://tenor.com/view/1blocked-message-gif-19278188")

    await bot.process_commands(message)


bot.run(TOKEN)