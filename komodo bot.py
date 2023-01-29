import discord
from dotenv import load_dotenv
import os

#made by superking816pro at https://github.com/superking816pro
#logo by catalyststuff on Freepik

# creating the bot object
bot = discord.Client(intents=discord.Intents.all())

# Credentials
load_dotenv('.env')

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("komodo moderation bot is in " + str(guild_count) + " discord servers.")

    print(f"Bot logged in as {bot.user}")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    if message.author != bot.user:
        
        if message.content == '!hello':
            respond1 = "hello"
            await message.channel.send(respond1)

        if message.content == '!github-sourcecode':
            respond2 = "soon to be added in github"
            await message.channel.send(respond2)

        if message.content == '!github':
            respond3 = "my creator's github profile = https://github.com/superking816pro"
            await message.channel.send(respond3)

        if message.content == '!discord':
            respond4 = "my creator's discord profile is private for now"
            await message.channel.send(respond4)    

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(os.getenv('BOT_TOKEN'))

print ("made by superking816pro at https://github.com/superking816pro")






















