import discord 
import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()

def getquote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote=json_data[0]['q'] + "-" + json_data[0]['a']
    return quote


def getmeme():
    response=requests.get("https://meme-api.com/gimme/wholesomemes")
    json_data=json.loads(response.text)
    meme=json_data["url"]
    return meme

intents=discord.Intents.default()
intents.message_content=True


client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"logged in as {client.user}")

@client.event
async def on_message(message):
    if(message.author==client.user):
        return
    
    if(message.content.startswith("$commands")):
        await message.channel.send(" !hello to greet the bot \n"
        " $meme to get random memes \n"
        " $motivate to get a surge of random motivation \n"
        " $commands to view the possible commands for the bot")
        return


    if(message.content.startswith("!hello")):
        await message.channel.send("Hello!")
        return

    if(message.content.startswith("$motivate")):
        await message.channel.send(getquote())
        return
    if(message.content.startswith("$meme")):
        await message.channel.send(getmeme())
        return

@client.event
async def on_member_join(member):
    await client.get_channel(1353417494492221472).send(f"welcome to the Server {member}")
    return






client.run(os.getenv('TOKEN'))