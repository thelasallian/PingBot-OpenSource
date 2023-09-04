# NOTICE

The bot is currently hosted 24/7 under `Microsoft Azure's Linux VMs`, standard_B1s - 1vcpu 1GiB memory with 64GiB of storage using 
Ubuntu Server 20.04 LTS - x64 Gen2. During server maintenance, the same code may be hosted under `pythonanywhere.com`, which will run the bot
for 24 hours max without resetting. The bot also relies on importing the `Google Sheets` csv file to add/edit the tags, not on `Google Sheets API`. 
Thus, Google Suite must only be active when resetting the bot. A version that does not rely on Google Suite is available under 
my public repository [Telegram-Ping-Bot-Prototype](https://github.com/Glinary/Telegram-Ping-Bot-Prototype).

1. Connect using SSH to the VM `ssh -i \path\to\private_key host_name@public_ip`
1. Install the following dependencies
``` 
    sudo apt-get install python3-pip
    sudo apt-get install tmux
    pip install python-telegram-bot
    pip install pandas
```
3. In case a PATH warning was displayed, you may add to path
`PATH=$PATH:/location/to/installation/folder`
4. Check if it was successfully added `echo $PATH`
5. Make a shared directory in the root folder `sudo chmod 777 pingloi`
6. Import the python code and move it to the shared directory 
   `sudo mv main.py /pingloi`
7. Check if there are tmux sessions under `/pingloi` directory
8. Enter the shared tmux session `tmux -S /pingloi/shared-session attach-session` if it exists
9. If there are no tmux sessions currently running,
    create a shared tmux session named shared-session using `tmux -S /pingloi/shared-session new-session`
10. If you did not attach to the session automatically, follow instruction 9
11. Run the main code `python3 main.py >> stdout.txt`
12. Detach from the tmux session `ctrl + b` then press `d`
13. Make the new folder accessible to all users `sudo chmod 777 /pingloi/shared-session`
14. Exit the SSH terminal

# How to stop/reset the bot:

1. Access the SSH terminal and navigate to the shared directory
2. You may check the running tmux sessions (optional) under `/pingloi` directory
3. Attach to the shared tmux session.  `tmux -S /pingloi/shared-session attach-session`
4. Stop the code by pressing `ctrl + c` or `cmd + c`
5. Run the code again by typing `python3 main.py >> stdout.txt`
6. Detach from the tmux session `ctrl + b` then press `d`
   
# How to edit the tags

1. Access and edit the google sheets under the bot's `/help` command.
   Note that only Eloi, Ray, and Glee has access to edit the file.
2. Reset the bot. You may refer to "How to stop/reset the bot"

# Questions/Concerns?

Reach out to the web section or contact the developer through her telegram `@gleezelluy`

# Technologies used
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4.svg?style=for-the-badge&logo=Microsoft-Azure&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624.svg?style=for-the-badge&logo=Linux&logoColor=black)
![Tmux](https://img.shields.io/badge/tmux-1BB91F.svg?style=for-the-badge&logo=tmux&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853.svg?style=for-the-badge&logo=Google-Sheets&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-26A5E4.svg?style=for-the-badge&logo=Telegram&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-1D9FD7.svg?style=for-the-badge&logo=PythonAnywhere&logoColor=white)

