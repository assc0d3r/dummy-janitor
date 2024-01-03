import os

CLIENT_NAME = "sessions/"+os.getenv("CLIENT_NAME")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
CHAT_ID = os.getenv("CHAT_ID")
SESSION = os.getenv("SESSION")


# MATCHERS_PATH = "/matchers_dir/matchers.db"
MATCHERS_PATH = "matchers.db"

RETENTION_PERIOD = 30

HELP_MESSAGE = """
This is a bot that will clean this chat from toad spam
It works as stupidly as possible. He has a list of matchers. He handles all fucking messages. And if this message contains at least one word from the list, it deletes it after RETENTION_PERIOD seconds.
Teams:
   - /janitor_help - person...

   - /add_matchers
     matcher_1
     matcher_2
     matcher_3
     - adds matchers to the list. It is important to write each new matcher on a new line. And it is not advisable to make multi-line matchers. Because it is impossible. Sausage.
       list is empty by default

   - /delete_matchers
     matcher_1
     matcher_2
     matcher_3
     - removes matchers

   - /list_matchers - list of matchers

   - /set_retention_period N - Assigns RETENTION_PERIOD. Like how long will it take for the bot to be deleted.
