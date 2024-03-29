# -*- coding: UTF-8 -*-
import asyncio
from asyncio import sleep

import discord
from discord.ext import commands

# without these options the bot will often stop playing too soon
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

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


async def safe_is_playing(vc):
    """ this should ignore sporadic disconnects of less than 5 seconds """
    if vc.is_playing():
        return True
    else:
        await sleep(5)
        return vc.is_playing()


async def play_url(url, ctx, say_errors=True):

    """:returns False if error while playing"""

    voice = ctx.message.author.voice
    voice_channel = voice.channel if voice else None

    if voice_channel is None:
        if say_errors:
            await ctx.send("You're not in a VC. Dummy!")
        return False
    elif get_playing_now(voice_channel):
        if say_errors:
            await ctx.send("Already playing something else.")
        return False
    else:
        vc = await voice_channel.connect()

        await sleep(1)

        vc.play(discord.FFmpegPCMAudio(source=url, **FFMPEG_OPTIONS))
        set_playing_now(voice_channel, True)

        # avoid sped up audio in the beginning
        voice.pause()
        await asyncio.sleep(1)
        voice.resume()

        while await safe_is_playing(vc):
            if get_should_skip(voice_channel):
                set_should_skip(voice_channel, False)
                vc.stop()
            else:
                await sleep(1)

        await vc.disconnect()
        set_playing_now(voice_channel, False)

    return True


class VoiceChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="p", help="Play an audio file in your current voice channel.")
    async def play(self, ctx):

        attachments = ctx.message.attachments

        if not attachments:
            await ctx.send("No file attached. Idiot!")
        else:
            await play_url(attachments[0].url, ctx)

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


async def setup(bot):
    await bot.add_cog(VoiceChatCog(bot))
