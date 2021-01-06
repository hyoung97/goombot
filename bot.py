import discord
import sports 
client = discord.Client()
TOKEN = 'NzcxNDc1MTY4MjgyODA0MjM0.X5sqPQ.rDYhhrjhi4K_jTzLW7GFekymxKM'
GENERAL_CHANNEL = '243500099248848896'

all_matches = sports.all_matches()
football = all_matches['football']
i = len(football)






@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await message.channel.send("Goomba!")
    if message.content == "Goomba!":
        await message.channel.send("Ah yes, I know of those lads.")
    if message.content == "!glerbTime":
        await message.channel.send("30 seconds of torch turn off torch and wait 45 seconds. Glerb. Enjoy.")
    if message.content == "!goom":
        await message.channel.send("Fucking GOOM!")
    if "marco" in message.content.lower():
        await message.channel.send("Pink Sus. @Pink Crewmate")
    if "hunter" in message.content.lower():
        await message.channel.send("my father's name was mentioned. I will now seek and destroy.")

client.run(TOKEN)
