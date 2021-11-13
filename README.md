# Dummy BOT

DummyBOT is a Discord Bot that perform the most important task on your Discord server, doing nothing.
It will always do nothing, whatever you do !

~~If you want to add this bot to your server, go to official website.~~

**Update 11-13-2021: Official bot is stopped and there is no actual plan to re-launch it. You can always run your own version of the bot by yourself.**

**Next part is only for people who want to launch their own version of DummyBOT**


### Requirements

* Python 3.7
* discord.py - 1.7.3 / [github](https://github.com/Rapptz/discord.py)
* PyNaCl - 1.4.0


### Usage

* Edit `dummy.py` and write your Discord bot token as value of `DISCORD_TOKEN`

* (Optional) Add your discord user id to `DISCORD_ADMINS`

* Launch `dummy.py` using python `python3 ./dummy.py`

* Use command `@<bot_name> destroy` to stop the bot 

* Use command `@<bot_name> join` to make the bot join you in a vocal channel 


You can also run the bot inside a Docker container :

* Build docker image : `docker build -t dummybot_discord:latest .`

* Then create and start a container : `docker create -e "DISCORD_TOKEN=<token>" -e "DISCORD_ADMINS=<id_admin>,<another_admin>" --name="dummybot" dummybot_discord:latest` and `docker start dummybot`


### License

MIT License
