import discord
import sys
from youtubesearchpython import VideosSearch # is this working? why isn't it throwing an error

async def join(message):
    # this gets the bot to join the channel of a user.
    try:
        voiceState = message.author.voice
        await voiceState.channel.connect()

    except:
        await message.channel.send("Please join a VC before trying to summon me.")

async def leave(message):
    # this gets the bot to leave the discord channel that it is currently in.
    try:
        voiceState = message.author.voice
        await message.channel.send("Goodbye fellow men.")
        await voiceState.channel.disconnect()

    except:
        await message.channel.send("Bitch, I'm not in a vc.")


if __name__ == '__main__':
    
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client)) # log in



    @client.event
    async def on_message(message): # this command listens to all messages
        if message.author == client.user:
            return
        
        if message.content.startswith('!joinMort'):
            await join(message)
            
        elif message.content.startswith('!moan'):
            await message.channel.send("I'm still implementing my song search/play function")

        elif message.content.startswith('!help'):
            await message.channel.send("Howdy.\n!moan will play a song\n!join will have me join\n!depart will have me leave") 
             
                
        elif message.content.startswith('!depart'):
            await leave(message)
            sys.exit()



    client.run('OTA4ODU4NzEzMDczMzkzNzI2.YY72og.XuKIhv6kigBAXBMSAVKnl5tVGbw')
