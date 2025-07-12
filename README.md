# My Discord Bot

This is a discord bot that I made using [Discord.py](https://discordpy.readthedocs.io/en/stable/). Feel free to use it on your own personal server if you want to, even though it's pretty simple.

## Requirements

- Python
- Pip
- discord.py

Install all dependecies using:
```
pip install -r requirements.txt
```

## Usage

```
python bot.py --token <your api token>
```
### Commands

**Note**: Commands are invoked using **!**

- **!greet**: Send back a greeting messsage at the author with their username
- **!info**: Takes an argument of member and prints out member's username, display name, and join date
- **!dump**: Takes an argument of a channel and creates a file with all the messages in that text channel, before sending a message to the author as a dm, with the text file as an attachment
