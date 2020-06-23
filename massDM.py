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

@bot.command() 


# The command is named MSG
# The `, *, payload` means take everything after the command and put it in one big string


@commands.has_permissions(administrator=True)
#@bot.command(pass_context = True)

                

#@bot.command(pass_context=True)
async def dmtoall(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print(" "+ args + " sent to " + member.name + " ")
            except:
                print("error")
    else:
        await ctx.channel.send("didnt provide arg")
bot.run('token')
