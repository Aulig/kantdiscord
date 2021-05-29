# -*- coding: UTF-8 -*-
from asyncio import sleep

import discord
from discord.ext import commands

playing_now = False
should_skip = False


class VoiceChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="p", help="Play an audio file in your current voice channel.")
    async def play(self, ctx):

        global playing_now
        global should_skip

        attachments = ctx.message.attachments

        if not attachments:
            await ctx.send("No file attached. Idiot!")
        else:
            voice_channel = ctx.message.author.voice.channel
            if voice_channel is None:
                await ctx.send("You're not in a VC. Dummy!")
            elif playing_now:
                await ctx.send("Already playing something else.")
            else:
                vc = await voice_channel.connect()

                vc.play(discord.FFmpegPCMAudio(source=attachments[0].url))
                playing_now = True

                while vc.is_playing():
                    if should_skip:
                        should_skip = False
                        vc.stop()
                    else:
                        await sleep(0.5)

                await vc.disconnect()
                playing_now = False

    @commands.command(name="s", help="Skip/stop the current file from playing.")
    async def skip(self, ctx):

        global playing_now
        global should_skip

        if playing_now and not should_skip:
            should_skip = True
            await ctx.send("Oke")
        else:
            await ctx.send("Nothing playing at the moment. Poophead!")


def setup(bot):
    bot.add_cog(VoiceChatCog(bot))