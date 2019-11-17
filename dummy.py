# coding: utf-8

"""
MIT License

Copyright (c) 2019, Candia Nicolas

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
import logging
import logging.handlers
import time
import os

# GLOBALS ---------------------------------------

# Discord BOT Token
DISCORD_TOKEN = "DISCORD-BOT-TOKEN"

# Discord admins user id, required for destroy command
DISCORD_ADMINS = ['215068875648139264']

# Discord client
client = discord.Client()

# Stop flag
stop = False

# UTILS -----------------------------------------

def terminate():
    global stop
    stop = True
    if client.loop.is_running():
        client.loop.stop()

# EVENTS ----------------------------------------

@client.event
@asyncio.coroutine
def on_ready():
    print("Dummy bot is now loaded !")

@client.event
@asyncio.coroutine
def on_message(message):
    mention = "<@{0}>".format(client.user.id)
    if message.content.startswith(mention):
        command = message.content[len(mention)::].strip()
        if command == 'destroy' and message.author.id in DISCORD_ADMINS:
            terminate()
            yield from asyncio.sleep(1)
    
# MAIN ------------------------------------------

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, terminate)
    signal.signal(signal.SIGINT, terminate)

    if "DISCORD_TOKEN" in os.environ:
        DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
    if "DISCORD_ADMINS" in os.environ:
        DISCORD_ADMINS = os.environ['DISCORD_ADMINS'].split(',')

    # Set-up logging
    logger = logging.getLogger('discord')
    logger.setLevel(logging.WARNING)
    log_handler = logging.handlers.RotatingFileHandler(filename='./logs/dummy.log', 
        encoding='utf-8', mode='a', maxBytes=10*1024*1024, backupCount=5)
    log_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(log_handler)

    # Run client
    while not stop:
        try:
            client.loop.run_until_complete(client.start(DISCORD_TOKEN))
        except KeyboardInterrupt:
            stop = True
        except BaseException as e:
            if not stop:
                print("Client disconnected, retry in 15 seconds ...")
                time.sleep(15)
    
    # Exit
    client.loop.run_until_complete(client.logout())
    client.loop.close()