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
    if (message.guild.voice_client): # If the bot is in a voice channel 
            await message.guild.voice_client.disconnect() # Leave the channel
            await message.channel.send('Bai bai fellow humans.')
    else: # But if it isn't
        await message.channel.send("I'm not in a voice channel, use the '>come' to make me join")
    await message.guild.voice_client.process_commands(message) # Always put this at the bottom of on_message to make commands work properly
    await message.delete()

async def mute(message): 
    voice_client = message.guild.voice_client
    if not voice_client:
        await message.channel.send("Please join a VC before trying to mute me.")
        return
    channel = voice_client.channel
    await voice_client.voice_state(message.guild.id, channel.id, self_mute=True)

async def unmute(message): 
    voice_client = message.guild.voice_client
    if not voice_client:
        await message.channel.send("Please join a VC before trying to unmute me.")
        return
    channel = voice_client.channel
    await voice_client.voice_state(message.guild.id, channel.id, self_mute=False)

if __name__ == '__main__':
    
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client)) # log in



    @client.event
    async def on_message(message): # this command listens to all messages
        if message.author == client.user:
            return
        
        if message.content.startswith('>come'):
            await join(message)
            await message.delete()
            
        elif message.content.startswith('>sing'):
            await message.channel.send("I'm still implementing my song search/play function")
            await message.delete()
        elif message.content.startswith('>help'):
            await message.channel.send("Howdy.\n>play will make me play a song\n>come make me join your VC\n>leave will make me leave") 
            await message.delete()

        elif message.content.startswith('>mute'):
            print(client.user.name)
            await client.user.edit(mute=True)
            #await mute(message)
            await message.channel.send("I will not talk now.")
            await message.delete()
        elif message.content.startswith('>unmute'):
            await client.user.edit(mute=False)
            #await unmute(message)
            await message.channel.send("I will now talk.")  
            await message.delete()
        elif message.content.startswith('>leave'):
            await leave(message)
            sys.exit()



    client.run('OTA4ODU4NzEzMDczMzkzNzI2.YY72og.XuKIhv6kigBAXBMSAVKnl5tVGbw')
