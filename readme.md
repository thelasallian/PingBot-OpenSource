# NOTICE

The bot is currently hosted 24/7 under `Fly.io`, shared-cpu-1x 256mb VMs with 3GB persistent volume storage and 160 GB outbound data transfer
under Singapore region. During server maintenance, the same code may be hosted under `pythonanywhere.com`, which will run the bot
for 24 hours max without resetting. The bot is also dependent on MongoDB and the [Telegram API server](https://core.telegram.org/). 
For reference, future updates will be based on my public repository [Telegram-Ping-Bot-Prototype](https://github.com/Glinary/Telegram-Ping-Bot-Prototype).

# How to deploy the bot

1. Install flyctl depending on your machine. You may refer to the [official documentation](https://fly.io/docs/hands-on/install-flyctl/).
2. Login to fly.io `fly auth login` or signup `fly auth signup`.
3. Deploy the application `fly launch`.
4. Expect to answer prompts from the terminal by typing `y` or `n`. Reject setting up a Postgresql database and an Upstash Redis database.

# How to stop the bot

1. Login to the fly.io
2. Navigate to the `application name` in the `dashboard` menu
3. Go to `settings`
4. Choose `Delete app`

# Questions/Concerns?
Reach out to the web section or contact the developer through her telegram `@gleezelluy`

# Technologies used
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4.svg?style=for-the-badge&logo=Telegram&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white)
![Fly.io](https://img.shields.io/badge/Fly.io-100000?style=for-the-badge&logo=Fly.io&logoColor=white&labelColor=4B058D&color=470386)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248.svg?style=for-the-badge&logo=MongoDB&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-1D9FD7.svg?style=for-the-badge&logo=PythonAnywhere&logoColor=white)

