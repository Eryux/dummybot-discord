# coding: utf-8

"""
MIT License

Copyright (c) 2021, Candia Nicolas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import discord
import asyncio
import signal
import os

# GLOBALS ---------------------------------------

# Discord BOT Token
DISCORD_TOKEN = "BOT_TOKEN"

# Discord admins user id, required for commands
DISCORD_ADMINS = [215068875648139264]

# UTILS -----------------------------------------

class DummyClient(discord.Client):

    def __init__(self, intents=None):
        super().__init__(intents=intents)

    async def on_message(self, message):
        if message.channel.type == discord.channel.ChannelType.text:
            if "<@!{0}>".format(self.user.id) or "<@{0}>".format(self.user.id):

                args = message.content.strip().split(' ')

                if len(args) > 1:
                    if args[1] == "destroy" and message.author.id in DISCORD_ADMINS: # stop the bot
                        await self.logout()
                        self.stop()

                    elif args[1] == "join": # join vocal channel
                        channel = None
                        for channel in message.guild.channels:
                            if isinstance(channel, discord.VoiceChannel):
                                for member in channel.members:
                                    if member.id == message.author.id:
                                        for voice_channel in self.voice_clients:
                                            if message.guild.id == voice_channel.guild.id:
                                                print("run")
                                                await voice_channel.disconnect(force=True)
                                                break
                                        await channel.connect()
                                        break

    async def on_ready(self):
        print("[DUMMYBOT] Discord client loaded")

    async def on_connect(self):
        print("[DUMMYBOT] connected to Discord")

    async def on_disconnected(self):
        print("[DUMMYBOT] disconnected from Discord")

    def stop(self):
        exit()
    
# MAIN ------------------------------------------

if __name__ == "__main__":
    print("[DUMMYBOT] Discord started")

    if "DISCORD_TOKEN" in os.environ:
        DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
    if "DISCORD_ADMINS" in os.environ:
        DISCORD_ADMINS = [int(s) for s in os.environ['DISCORD_ADMINS'].split(',')]

    # Run client
    intents = discord.Intents.default()
    intents.members = True

    client = DummyClient(intents=intents)

    signal.signal(signal.SIGTERM, client.stop)
    signal.signal(signal.SIGINT, client.stop)

    client.run(DISCORD_TOKEN)

    print("[DUMMYBOT] terminated")