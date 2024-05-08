# -*- coding: UTF-8 -*-

import random

from discord import File
from discord.ext import commands

from cogs.voice_chat import play_url
from utils import image_utils, text_utils


class RandomStuffCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sus", help="Only use this command if you're not the imposter.")
    async def sus(self, ctx):
        potential_responses = [
            "You're so sussy!",
            "https://tenor.com/view/sussy-gif-20489896",
            "AMOGUS.\n:musical_note: bing :musical_note: bing :musical_note: bing :musical_note: bing :musical_note: bing :musical_note: bing :musical_note: bing :musical_note:\n:musical_note: bing :musical_note: bing :musical_note: bing :musical_note:",
            """
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
    ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
    ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⠀
    ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⠀⠀
    ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
    ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
    ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
    ⠀ ⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶ ⢠⣿⣿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """,
            "ඞ"
        ]

        # try to play the amogus sound effect, if not successful, send a text message instead
        if not await play_url(
                "https://cdn.discordapp.com/attachments/535224272805953559/851447691443830835/AMOGUS-5DlROhT8NgU.webm",
                ctx, say_errors=False):
            response = random.choice(potential_responses)
            await ctx.send(response)

    @commands.command(name="soy",
                      help="Someone said something you didn't like? Gonna cry about it? Piss your pants? Use this command instead.")
    async def soy(self, ctx, *args):
        soyjak_links = [
            "https://pbs.twimg.com/media/ER-LfVuXsAAVMCF.png",
            "https://i.kym-cdn.com/photos/images/original/002/070/088/10d.png",
            "https://media.discordapp.net/attachments/586322638377451520/846056799035850772/6ca.png",
            "https://i.imgur.com/aKa00AM.png"
        ]

        split = text_utils.split_text(" ".join(args))
        await ctx.send(image_utils.create_meme(split[0], split[1], random.choice(soyjak_links)))

    @commands.command(name="problem", help="Got a problem?")
    async def problem(self, ctx):
        await ctx.send(file=File("problem.mp3", filename="problem.mp3"))

    @commands.command(name="back", help="Missed me?")
    async def back(self, ctx):
        await ctx.send(file=File("back.mp3", filename="back.mp3"))

    @commands.command(name="joo", help="A plea to joo bidin.")
    async def joo(self, ctx, *args):
        await ctx.send("""https://cdn.discordapp.com/attachments/730713281278509079/801985700005543956/video0.mp4
jooo bidin, jooo bidin, jooo bidin, jooo bidin this message from mohammed kalakeen full face of kurdistan for youu jooo bidin. you go check up in the docter; you have 2 yeal. your live is 2 yeal. 2 yeal from now, from today too 2 yeal o 1 yeal and 6 month o 2 yeal. you life. after this one you pass aweh. you go check up in the docter, this message from mohammed kalakeen full face of kurdistan. you do, do you good job for da usa for da 50 staet in 2 yeal. you do pull down iran for us, we want our kurdistan can-... new country no more iran no more iraq no more tourkey no more suri, full face of kurdistan; we give you""")
        await ctx.send("https://media.discordapp.net/attachments/536819938514436116/874558455669751818/unknown.png")


async def setup(bot):
    await bot.add_cog(RandomStuffCog(bot))
