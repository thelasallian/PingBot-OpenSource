# NOTICE

The bot is currently hosted 24/7 under `Google Cloud's Compute Engine`,
e2-micro machine with 10GB of storage using Linux Debian. During server maintenance,
the same code may be hosted under `pythonanywhere.com`, which will run the bot
for 24 hours max without resetting. The bot also relies on importing the `Google Sheets` csv file to add/edit the tags,
not on `Google Sheets API`. Thus, Google Suite must only be active when resetting the bot.
A version that does not rely on Google Suite is available under my public repository [Telegram-Ping-Bot-Prototype](https://github.com/Glinary/Telegram-Ping-Bot-Prototype).
# How to deploy the bot

1. Access the project under Google Cloud
2. Go to Compute Engine > VM Instance > Connect using SSH
3. Install the following dependencies
``` 
    sudo apt-get install python3-pip
    sudo apt-get install tmux
    pip install python-telegram-bot
    pip install pandas
```
4. In case a PATH warning was displayed, you may add to path
`PATH=$PATH:/location/to/installation/folder`

6. Check if it was successfully added `echo $PATH`
7. Make a shared directory in the root folder `sudo chmod 777 foldername`
8. Import the python code and move it to the shared directory 
   `sudo mv main.py /path/to/shared/directory`
8. Check if there are tmux sessions running `tmux ls`
9. Enter the tmux session. Note that 0 may be changed
   depending on the tmux session id number `tmux a -t 0`
10. If there are no tmux sessions currently running,
    create one by typing `tmux`
11. Run the main code `python3 main.py`
12. Confirm if the bot is successfully running
    by waiting for a `Polling` message in the console
13. Exit the SSH session

# How to stop/reset the bot:

1. For `emergency cases`, you may delete the VM instance in the Google Cloud Project. 
   This means that a new VM instance will have to be created by the developer.
   Currently, @gleezelluy (telegram) owns the VM instance and has given owner access to TLS.
   Creating a VM instance from scratch willl require another developer with a Google Cloud account.
2. The `safe and recommended option` is to access the running code
   and stop it from the SSH terminal
3. To do so, access the SSH terminal and navigate to the shared directory
4. Check the running tmux sessions `tmux ls`
6. Enter the chosen tmux session. Note that 0 may be changed
   depending on the tmux session id number `tmux a -t 0`
7. Stop the code by pressing `ctrl + c` or `cmd + c`
8. Run the code by typing `python3 main.py`
   
# How to edit the tags

1. Access and edit the google sheets under the bot's `/help` command.
   Note that only Eloi, Ray, and Glee has access to edit the file.
2. Reset the bot. You may refer to "How to stop/reset the bot"

# Questions/Concerns?

Reach out to the web section or contact the developer through her telegram `@gleezelluy`

# Technologies used
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4.svg?style=for-the-badge&logo=Google-Cloud&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624.svg?style=for-the-badge&logo=Linux&logoColor=black)
![Tmux](https://img.shields.io/badge/tmux-1BB91F.svg?style=for-the-badge&logo=tmux&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853.svg?style=for-the-badge&logo=Google-Sheets&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-1D9FD7.svg?style=for-the-badge&logo=PythonAnywhere&logoColor=white)

