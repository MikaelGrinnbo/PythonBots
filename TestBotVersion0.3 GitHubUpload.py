import discord
import random
from discord.ext import commands


## <-- used to symbolize end of command lines


#permissions for bot
intents = discord.Intents().all()
intents.members = True 

client = commands.Bot(command_prefix='!', intents=intents)
##



#if bot is running print text
@client.event
async def on_ready():
    print ("\n------------------------------")
    print (f'{client.user} IS NOW ONLINE')
    print ("------------------------------\n")
##


#text commands
@client.command()
async def hello(ctx):
    response =(random.randint(1 , 5)) #changes the value of response to a random value to and from the selected values

    Response1 = "INSERT MESSAGE 1" #insert desired response
    Response2 = "INSERT MESSAGE 2"
    Response3 = "INSERT MESSAGE 3"
    Response4 = "INSERT MESSAGE 4"
    Response5 = "INSERT MESSAGE 5"



 #random replies
    if (response == 1): #if the value of response is 1, send response1's message
        await ctx.send(Response1) and print ("1: INSERT MESSAGE 1") #print is here for debug purposes, this way you can see in your script what the response value is currently at

    elif (response == 2):
        await ctx.send(Response2) and print ("2: INSERT MESSAGE 2")

    elif (response == 3):
        await ctx.send(Response3) and print ("3: INSERT MESSAGE 3")

    elif (response == 4):
        await ctx.send(Response4) and print ("4: INSERT MESSAGE 4")

    elif (response == 5):
        await ctx.send(Response5) and print ("5: INSERT MESSAGE 5")
##



#join message
@client.event
async def on_member_join(member):
    print ("NEW MEMBER HAS JOINED THE SERVER")
    channel = client.get_channel(INSERT CHANNEL ID) #channel id (used to make it send the message in the desired channel)
    await channel.send("welcome to the server!")
##


"""
#embed 
@client.command()
async def profit(ctx): #defines embed as a commmand | embed with image from path
    embed = discord.Embed(title="click here", url="INSERT LINK TO BE EMBEDED INTO TITLE", description="INSERT CUSTOM DESCRIPTION", color=0x0099ff) #choose color, description url and title
    file = discord.File("INSERT/FILE/PATH/HERE.PNG", filename="image.png")#defines the file path, write path in manually if errors occur
    embed.set_image(url="attachment://image.png") #this does not need any editing upon customization, it only refers to filename definition mention in code above.
    await ctx.send(file=file, embed=embed)
"""


#embed with url link instead of local filepath
@client.command()
async def profit (ctx):
    embed = discord.Embed(title="click here", url="INSERT LINK TO BE EMBEDED INTO TITLE", description="INSERT CUSTOM DESCRIPTION", color=0x0099ff) #choose color, description url and title
    imageurl = 'INSERT LINK' # insert image link
    embed.set_image(url = imageurl)
    await ctx.send(embed=embed)
##


#embed as a help command instead of the default discord help command
""""
#removes the help command from the discord api
client.remove_command('help')
@client.command() #if you wish for a help command in embed format
async def help (ctx): #defines embed as a commmand
    embed = discord.Embed(title="currently existing commands:", url="INSERT LINK TO BE EMBEDED INTO TITLE", description="!hello \n !profit \n!help", color=0x0099ff) #choose color, description url and title
    await ctx.send(embed=embed)  
##
"""


#bot token
client.run('BOT TOKEN')
