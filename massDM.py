'''
from discord.ext import commands
from discord.utils import get

# Bot objects listen for commands on the channels they can "see" and react to them by 
# calling the function with the same name

bot = commands.Bot(command_prefix='.')

# Here we register the below function with the bot Bot
# We also specify that we want to pass information about the message containing the command
# This is how we identify the author






@bot.command(pass_context=True) 





# The command is named MSG
# The `, *, payload` means take everything after the command and put it in one big string


async def MSGG(ctx, *, payload):   
    # get will return the role if the author has it.  Otherwise, it will return None
    if get(ctx.message.author.roles, id="649650879741427740"): 
        for member in ctx.message.server.members:
            await bot.send_message(member, "THIS IS SEND THROUGH MASS DM BOT...IF RECEIVED CONTACT SLAYER ASAP.")

bot.run('NjQzMTgwNTM4MTQ4MTU5NTI5.XeoNMg.UvGEvqtuIWffDiXOknfm5c90nOk')


#####################################DM BOT#############################################################





from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix='.')


@bot.command(pass_context=True) 


# The command is named MSG
# The `, *, payload` means take everything after the command and put it in one big string


async def MSGG(ctx):   
    # get will return the role if the author has it.  Otherwise, it will return None
    if get(ctx.message.author.roles, id="702469635768975360"): 
        for member in ctx.message.server.members:
            await bot.dm_channel.send("THIS IS SEND THROUGH MASS DM BOT...IF RECEIVED CONTACT SLAYER ASAP.")

bot.run('NjQzMTgwNTM4MTQ4MTU5NTI5.XeoNMg.UvGEvqtuIWffDiXOknfm5c90nOk')


'''

import discord
from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix='.')
client= discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True) 


# The command is named MSG
# The `, *, payload` means take everything after the command and put it in one big string


@commands.has_permissions(administrator=True)
#@bot.command(pass_context = True)
async def send(ctx, *, content: str):
        for member in ctx.message.server.members:
            try:
                await bot.send_message(member, content)
                await bot.say("DM Sent To : {} :white_check_mark:  ".format(member))
            except:
                print("can't")
                await bot.say("DM can't Sent To : {} :x: ".format(member))

bot.run('NjQzMTgwNTM4MTQ4MTU5NTI5.XeoNMg.UvGEvqtuIWffDiXOknfm5c90nOk')