import os
import random
import re

import discord
from discord.ext import commands

# this config file is gitignored because it contains secrets
from config import TOKEN
from utils import image_utils, url_utils

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

    lower_case_content = message.content.lower()

    if lower_case_content.starts_with(">"):
        # don't provide a special reaction to commands
        return

    if message.content == "N":
        await message.channel.send("https://static.wikia.nocookie.net/doawk/images/5/59/Manny_says_ploopy.jpg/revision/latest?cb=20190414152105")

    janny_triggers = ["janny", "jenny", "jannies", "jennies"]
    janny_replies = [
        "https://media.discordapp.net/attachments/536819938514436116/867320829816602634/Resilienz_Coping_web.jpg",
        "https://tenor.com/view/1blocked-message-gif-19278188",
        "https://cdn.discordapp.com/attachments/536819938514436116/867745626216333362/unknown.png"]

    for janny_trigger in janny_triggers:
        if janny_trigger in lower_case_content:
            await message.channel.send(random.choice(janny_replies))
            break

    # url_to_download = None
    #
    # if message.embeds:
    #     url_to_download = message.embeds[0].url
    # if message.attachments:
    #     url_to_download = message.attachments[0].url
    #
    # if url_to_download:
    #     downloaded_attachment = url_utils.download_file(url_to_download)
    #
    #     if image_utils.is_image(downloaded_attachment):
    #         nsfw_probability = image_utils.check_image_nsfw(downloaded_attachment)["unsafe"]
    #     elif image_utils.is_video(url_to_download):
    #         nsfw_probability = image_utils.check_video_nsfw(downloaded_attachment)["unsafe"]
    #     else:
    #         nsfw_probability = 0
    #
    #     if nsfw_probability > 0.85:
    #         await message.channel.send(f"I'm {nsfw_probability * 100}% sure this is NSFW. Are you sure you want to post this? Please remember that kneecaps are a privilege, not a right.")
    #
    #     os.remove(downloaded_attachment)

    await bot.process_commands(message)


bot.run(TOKEN)