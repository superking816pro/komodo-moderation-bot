from dotenv import load_dotenv
import requests
import json
import inspect
import sys
import os
from discord import app_commands, Intents, Client, Interaction
from colorama import Fore, Style

load_dotenv()


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync()


client = FunnyBadge(intents=Intents.none())

@client.event
async def on_ready():
    print(inspect.cleandoc(f"""
        Logged in as {client.user} (ID: {client.user.id})
        Use this URL to invite {client.user} to your server:
        {Fore.LIGHTBLUE_EX}https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot{Fore.RESET}
    """), end="\n\n")
    
@client.tree.command()
async def hello(interaction: Interaction):
    """ Says hello or something """
    # Responds in the console that the command has been ran
    print(f">{interaction.user} used the command.")

    # Then responds in the channel with this message
    await interaction.response.send_message(inspect.cleandoc(f"""
        Hi **{interaction.user}**, thank you for saying hello to me."""))

# Runs the bot with the token you provided
client.run(os.getenv('BOT_TOKEN'))
