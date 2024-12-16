import discord
import responses
import openai
import os 
from dotenv import load_dotenv
openai.api_key = os.getenv('OPENAI_API_KEY')
token = os.getenv('DISCORD_BOT_TOKEN')

# Set your OpenAI API key
openai.api_key = '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'


async def send_spam(message,user_message, is_private):
    if message == "gametime":
        for i in range(100):
            response = ("<@621898831889694720>""<@309881534205263875>")
            await message.author.send(response) if is_private else await message.channel.send(response)
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)




def run_discord_bot():
    token = 'MTE4OTY4OTIwNzIyNTA2NTUyMg.G2vNwF.h8S3oB6Og-w0HKpfdbbyDbOb-l872p3yX3i1zc'
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    

    @client.event
    async def on_ready():
        
        print(f'{client.user} is now running!')
        print("Bot is active in the following servers:")
        for guild in client.guilds:
            print(f'- {guild.name} (ID: {guild.id})')
        await send_message("Bot is now running", user_message=True, is_private=False)
        

    @client.event
    async def on_message(message):
        if message.author == client.user:  
            return


        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")
        
        with open('user_messages.txt', 'a') as file:
            file.write(f"{username} said: {user_message.lower()} ({channel}) \n")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            user_message = user_message
            await send_message(message, user_message, is_private=False)


    client.run(token)

