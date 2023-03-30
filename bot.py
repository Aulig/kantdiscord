import asyncio
import random
from asyncio import sleep

import discord
from discord.ext import commands

# this config file is gitignored because it contains secrets
from config import TOKEN
from utils import text_utils

initial_extensions = [
    'cogs.random_stuff',
    'cogs.voice_chat'
]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">", intents=intents)


async def main():
    async with bot:
        for extension in initial_extensions:
            await bot.load_extension(extension)
        await bot.start(TOKEN)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    await bot.change_presence(activity=discord.Game(name='Amogus'))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    lower_case_content = message.content.lower()

    # don't provide a special reaction to commands
    if not lower_case_content.startswith(">"):
        # only for doom (Normally "The Doominator")
        if message.content == "N":
            if "The Doominator" in message.author.name or "Aulig" in message.author.name:
                await message.channel.send(
                    "https://static.wikia.nocookie.net/doawk/images/5/59/Manny_says_ploopy.jpg/revision/latest?cb=20190414152105")
            else:
                gif_msg = await message.channel.send(
                    "https://media.discordapp.net/attachments/512233995124211733/677974431817138227/1510964224_giphy_3.gif")
                await sleep(10)
                await gif_msg.delete()

        janny_triggers = ["janny", "jenny", "jannies", "jennies", "jannys", "jennys", "janitor"]
        janny_replies = [
            "https://media.discordapp.net/attachments/536819938514436116/867320829816602634/Resilienz_Coping_web.jpg",
            "https://tenor.com/view/1blocked-message-gif-19278188",
            "https://cdn.discordapp.com/attachments/536819938514436116/867747945796206642/seethe.mp4",
            """
⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀ ⡜⠀⠀⠀
⠀⠀⠀⠑⡀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ⡔⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⣀⠴⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠤⠄⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣀⠄⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠒⠒⠒⠒⠒⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡰⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀   ⠀⠙⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⢠⠂ ⠀ ⠀⠘⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⢤⡀⢂⠀⢨⠀⢀⡠⠈  ⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⢀⡖⠒⠶⠤⠭⢽⣟⣗⠲⠖⠺⣖⣴⣆⡤⠤⠤⠼⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡈⠃⠀⠀⠀⠘⣺⡟⢻⠻⡆⠀⡏⠀⡸⣿⢿⢞⠄⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢣⡀⠤⡀⡀⡔⠉⣏⡿⠛⠓⠊⠁⠀⢎⠛⡗⡗⢳⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢱⠀⠨⡇⠃⠀⢻⠁⡔⢡⠒⢀⠀⠀⡅⢹⣿⢨⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠠⢼⠀⠀⡎⡜⠒⢀⠭⡖⡤⢭⣱⢸⢙⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠸⢁⡀⠿⠈⠂⣿⣿⣿⣿⣿⡏⡍⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠸⢢⣫⢀⠘⣿⣿⡿⠏⣼⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣠⠊⠀⣀⠎⠁⠀⠀⠀⠙⠳⢴⡦⡴⢶⣞⣁⣀⣀⡀⠀⠀⠀⠀⠀
⠀⠐⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢀⠤⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀
            """,
            # soyjak speech bubble
            "https://i.kym-cdn.com/photos/images/facebook/001/939/162/b61.png",
            "https://media.discordapp.net/attachments/536819938514436116/873831647253000222/1628393963638.png",
            # Yuur Coping
            "https://cdn.discordapp.com/attachments/536819938514436116/919190523930083338/unknown.png"
        ]

        for janny_trigger in janny_triggers:
            if janny_trigger in lower_case_content:
                await message.channel.send(random.choice(janny_replies))

                if random.randint(0, 10) == 4:
                    cope_words = ["cope", "seethe", "malding", "stay mad"]
                    await text_utils.send_words_slowly(cope_words, message.channel)

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


asyncio.run(main())
