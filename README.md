# Dummy BOT

DummyBOT is a Discord Bot that perform the most important task on your Discord server, doing nothing.
It will always do nothing, whatever you do !

If you want to add this bot to your server, go to [official website](http://dummybot.pawz.xyz/).

**Next part is only for person who want to launch there own version of DummyBOT**


### Requirements

* Python 3.5 / 3.6
* discord.py 0.16 ([github](https://github.com/Rapptz/discord.py))


### Usage

* Edit `dummy.py` and write you Discord bot token as value of `DISCORD_TOKEN`

* (Optional) Add your discord ID to `DISCORD_ADMINS`

* Launch `dummy.py` using python `python3 ./dummy.py`

* Use command `@<bot_name> destroy` to stop the bot 


You can also run it in a Docker container :

* Build docker image : `docker build -t dummybot_discord:latest .`

* Then create and start a container : `docker create -e "DISCORD_TOKEN=<token>" -e "DISCORD_ADMINS=<id_admin>,<another_admin>" --name="dummybot" dummybot_discord:latest` and `docker start dummybot`

* Or using compose : `docker-compose up`


### License

MIT License
