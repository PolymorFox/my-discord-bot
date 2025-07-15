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

- **!greet**: Replies to the command author with a greeting that includes their username.
- **!info `<member>`**: Displays the specified member's username, display name, and the date they joined the server.
- **!dump `<channel>`**: Collects all messages from the specified text channel, saves them to a file, and sends that file to the author via direct message.
- **!send `<member>`**: Sends a hello message directly to the specified member.
- **!flood `<member>` `<limit>` `[message]`**: Sends the specified member a number of direct messages equal to `<limit>`. Optionally, you can provide a custom `[message]`; if omitted, a default hello message is used.
