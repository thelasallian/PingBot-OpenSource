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
7. Make a shared directory in the root folder `sudo chmod 777 pingloi`
8. Import the python code and move it to the shared directory 
   `sudo mv main.py /pingloi`
8. Check if there are tmux sessions under `/pingloi` directory
9. Enter the shared tmux session `tmux -S /pingloi/shared-session attach-session` if it exists
10. If there are no tmux sessions currently running,
    create a shared tmux session named shared-session using `tmux -S /pingloi/shared-session new-session`
11. If you did not attach to the session automatically, follow instruction 9
12. Run the main code `python3 main.py >> stdout.txt`
13. Detach from the tmux session `ctrl + b` then press `d`
14. Make the new folder accessible to all users `sudo chmod 777 /pingloi/shared-session`
17. Exit the SSH terminal

# How to stop/reset the bot:

1. For `emergency cases`, you may delete the VM instance in the Google Cloud Project. 
   This means that a new VM instance will have to be created by the developer.
   Currently, @gleezelluy (telegram) owns the VM instance and has given owner access to TLS.
   Creating a VM instance from scratch willl require another developer with a Google Cloud account.
2. The `safe and recommended option` is to access the running code
   and stop it from the SSH terminal
3. To do so, access the SSH terminal and navigate to the shared directory
4. You may check the running tmux sessions (optional) under `/pingloi` directory
6. Attach to the shared tmux session.  `tmux -S /pingloi/shared-session attach-session`
7. Stop the code by pressing `ctrl + c` or `cmd + c`
8. Run the code by typing `python3 main.py >> stdout.txt`
9. Detach from the tmux session `ctrl + b` then press `d`
   
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

