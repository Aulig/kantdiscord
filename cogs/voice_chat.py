# -*- coding: UTF-8 -*-
from asyncio import sleep

import discord
from discord.ext import commands

PLAYING_NOW = "playing_now"
SHOULD_SKIP = "should_skip"

voice_channel_id_to_state_map = {}


def init_channel_id_to_state_map_if_necessary(channel_id):
    if channel_id not in voice_channel_id_to_state_map:
        voice_channel_id_to_state_map[channel_id] = {PLAYING_NOW: False, SHOULD_SKIP: False}


def get_vc_property(voice_channel, property_name):
    global voice_channel_id_to_state_map

    channel_id = voice_channel.id
    init_channel_id_to_state_map_if_necessary(channel_id)
    return voice_channel_id_to_state_map[channel_id][property_name]


def set_vc_property(voice_channel, property_name, new_value):
    global voice_channel_id_to_state_map

    channel_id = voice_channel.id
    init_channel_id_to_state_map_if_necessary(channel_id)
    voice_channel_id_to_state_map[channel_id][property_name] = new_value


def get_playing_now(voice_channel):
    return get_vc_property(voice_channel, PLAYING_NOW)


def get_should_skip(voice_channel):
    return get_vc_property(voice_channel, SHOULD_SKIP)


def set_playing_now(voice_channel, new_value):
    set_vc_property(voice_channel, PLAYING_NOW, new_value)


def set_should_skip(voice_channel, new_value):
    set_vc_property(voice_channel, SHOULD_SKIP, new_value)


class VoiceChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="p", help="Play an audio file in your current voice channel.")
    async def play(self, ctx):

        attachments = ctx.message.attachments

        if not attachments:
            await ctx.send("No file attached. Idiot!")
        else:
            voice = ctx.message.author.voice
            voice_channel = voice.channel if voice else None
            if voice_channel is None:
                await ctx.send("You're not in a VC. Dummy!")
            elif get_playing_now(voice_channel):
                await ctx.send("Already playing something else.")
            else:
                vc = await voice_channel.connect()

                vc.play(discord.FFmpegPCMAudio(source=attachments[0].url))
                set_playing_now(voice_channel, True)

                while vc.is_playing():
                    if get_should_skip(voice_channel):
                        set_should_skip(voice_channel, False)
                        vc.stop()
                    else:
                        await sleep(0.5)

                await vc.disconnect()
                set_playing_now(voice_channel, False)

    @commands.command(name="s", help="Skip/stop the current file from playing.")
    async def skip(self, ctx):

        voice = ctx.message.author.voice
        voice_channel = voice.channel if voice else None
        if voice_channel is None:
            await ctx.send("You're not in a VC. Dummy!")
        else:
            if get_playing_now(voice_channel) and not get_should_skip(voice_channel):
                set_should_skip(voice_channel, True)
                await ctx.send("Oke")
            else:
                await ctx.send("Nothing playing at the moment. Poophead!")


def setup(bot):
    bot.add_cog(VoiceChatCog(bot))