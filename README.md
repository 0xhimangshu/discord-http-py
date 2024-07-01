<h1 align="center"> Discord HTTP interaction bot example </h1>
<h3 align="center">An awesome open source project to demonstrate usage of discord http interactions in python!</h3>

[![License](https://img.shields.io/github/license/0xhimangshu/discord-http-interaction-bot.svg?style=for-the-badge)](https://github.com/0xhimangshu/discord-http-interaction/blob/main/LICENSE) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logoSize=auto)](https://github.com/psf/black)

<h2>About this project</h2>
<p>This repository is an open source project to demonstrate the usage of discord http interactions in python. </p>

* This repo is open source and free to use.
* Http interactions can be used to host serverless bots, it saves us a lot of hosting resources and money.

You may also suggest changes by forking this repo and creating a pull request or opening an issue

# Built with
[![Python](https://img.shields.io/badge/python-3.11.3+-000000?style=for-the-badge&logo=python&logoColor=yellow&logoSize=auto)](https://python.org/) [![AIOHTTP](https://img.shields.io/badge/iohttp-3.8.6-000000.svg?style=for-the-badge&logo=aiohttp&logoColor=white&logoSize=auto)](https://github.com/aio-libs/aiohttp) [![PyNaCl]( https://img.shields.io/badge/PyNaCl-1.5.0-black?style=for-the-badge)](https://github.com/pyca/pynacl)


## Getting Started

1. Clone this repo on your local machine
  ```sh
  git clone https://github.com/0xhimangshu/discord-http-py
  ```
2. Install the requirements (Sorry i use reqs instead of requirements)
  ```sh
  python -m pip install -U -r reqs.txt
  ```
3. Create a discord application and bot on [Discord Developer Portal](https://discord.com/developers/applications)
4. Rename the [example.config.py](https://github.com/0xhimangshu/discord-http-py/blob/master/example.config.py) file to config.py
5. Complete the .env file with your bot token, application id and public key from the discord developer portal.
6. Edit commands in [commands.py](https://github.com/0xhimangshu/discord-http-py/blob/main/commands.py)
* Note: You will have to run upsert.py before main.py to upload your slash commands to discord.
7. Run the bot
  ```sh
  python main.py
  ```
8. Sorry, you are not done yet! you have to use a server like [ngrok](https://ngrok.com/) to start a local webserver.
9. Please install any server like ngrok and start a local webserver on port 3000.
  ```sh
  ngrok http 3000
  ```
10. Copy the https url from the ngrok terminal and paste it in the discord developer portal in the interaction section.
11. You are done! Now you can use your bot in any server you want.
12. Ah! not done yet, You can use web services like vercel to host your bot 24/7 for free. You can also use heroku.
13. This is serverless hosting so it wont cost you much :wink:
## Join discord server if you want to
[![Discord](https://img.shields.io/badge/Discord-000000.svg?style=for-the-badge&logo=discord&logoColor=white&logoSize=auto)](https://discord.gg/kBUegfgYkg)
