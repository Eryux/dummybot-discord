# Dummy BOT

DummyBOT is a Discord Bot that perform the most important task on your Discord server, doing nothing.
It will always do nothing, whatever you do !

If you want to add this bot to your server, go to [official website](http://dummybot.pawz.xyz/).

**Next part is only for person who want to launch there own version of Dummy BOT**


### Requirements

* Python 3.5 or 3.6
* discord.py ([github](https://github.com/Rapptz/discord.py))


### Usage

* Edit `dummy.py` and write you Discord bot token as value of `DISCORD_TOKEN` variable.

* Launch `dummy.py` using python `python3 ./dummy.py`


You can also run it in a Docker container :

* Make a docker image : `docker build -t dummybot_discord:latest .`

* Create docker container : `docker create --name="dummybot" dummybot_discord:latest`

* Start container : `docker start dummybot`


### License

MIT License
