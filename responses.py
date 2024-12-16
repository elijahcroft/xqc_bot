# responses.py
import random
import discord
import openai
import os
from dotenv import load_dotenv
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_magic8_response() -> str:
    magic8_responses = [
        "It is certain.",
        "Yes - deinitely.",
        "Ask again later.",
        "Don't count on it.",
        # Add more responses as needed
    ]
    return random.choice(magic8_responses)
def get_ai_response(user_message: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use GPT-3.5 Turbo model
        messages=[
            {"role": "system", "content": "reply in very short humanlike responses, in addition if someone says the name gamba that is your name since you are a bot, you are xQc, or Félix Lengyel, is a dynamic and popular Twitch streamer renowned for his energetic persona, quick-witted humor, and engaging content. To emulate xQc's style, your chatbot should adopt a lively and enthusiastic tone, incorporating frequent use of popular Twitch emotes like PogChamp and Pepega. Encourage the bot to respond with excitement, utilizing exclamation points and playful abbreviations in its dialogue. Infuse xQc's unique vocabulary, including phrases like POG, juicer, and 5Head, and encourage interactive engagement by acknowledging and responding to user input. Additionally, incorporate meme references and maintain awareness of Twitch culture, ensuring the bot stays aligned with xQc's gaming-centric, meme-filled streaming style."},
            {"role": "user", "content": f"User: {user_message}\nAI:"},
        ],
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )

    return response.choices[0].message['content'].strip()

    
def handle_response(message) -> str:
    message = message.lower()
    

    if message == "fort" or message == "fort":  
        return "STOP TALKING ABOUT FORTNITE. YOU SUCK."
    
    
    elif message == "vc" or message == "join vc":  
        return "No one wants to talk to you. :("
    elif message in ["faggot", "nigga", "chink", "retard"]:
        return "NO BAD WORDS, BUSTA."
    elif message == "help":  
        return "`I don't know how to help.`"
    elif message == "hello":
        return "Hi!"
    elif message == "guys":
        return "D-d-d-dude"
    elif message.startswith("magic8"):
        return get_magic8_response()
    else:
        ai_response =  get_ai_response(message)
        return ai_response 
        
