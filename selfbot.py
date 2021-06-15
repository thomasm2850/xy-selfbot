import discord
import json
import os
import re
import requests
import threading
from discord.ext import commands, tasks
from threading import *

with open("./config.json") as lol:
    config = json.load(lol)

token = config.get('token')
prefix = config.get('prefix')
nitrosniper = config.get('nitrosniper')
slotbot = config.get('slotbot')
intents = discord.Intents().all()
intents.messages=True
urmom = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)
urmom.remove_command('help')

class colours():
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

@urmom.command()
async def test(ctx):
    await ctx.message.delete()
    print('i am online')

async def banthem(ctx):
    for urmom in ctx.guild.members:
        try:
            await urmom.ban()
            print(f'[>] banned {ctx.guild.member}')
        except:
            pass

async def rolesdel(ctx): 
    for role in ctx.guild.roles:
        if ctx.guild.roles[-1] > role:
                try:
                    await role.delete()
                except:
                    pass

async def channeldel(ctx):
    for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                pass

async def channelspam(ctx):
    for i in range(1, 50):
        try:
            await ctx.guild.create_voice_channel(
                name=f"urmom"
            )
            await ctx.guild.create_category(
                name=f"xy selfbot was here"
            )
        except:
            pass

@urmom.command()
async def nuke(ctx):
    await ctx.message.delete()
    print(colours.CRED + """     
    _.-^^---....,,--_      
 _--                   -_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____""")
    print(f'[>] nuking {ctx.guild.name}')
    Thread(target = await banthem(ctx)).start()
    Thread(target = await rolesdel(ctx)).start()
    Thread(target = await channeldel(ctx)).start()
    Thread(target = await channelspam(ctx)).start()

@urmom.command()
async def banall(ctx, member: discord.Member):
    await ctx.message.delete()
    for urmom in ctx.guild.members:
        try:
            await urmom.ban()
            print(colours.CRED2 + f'[+] banned {member}')
        except:
            pass
        print(colours.CGREY + '[>] banall complete')

@urmom.command()
async def unbanall(ctx, member: discord.Member):
    await ctx.message.delete()
    for urmom in ctx.guild.bans:
        try:
            await urmom.unban()
            print(colours.CRED2 + f'[+] unbanned {member}')
        except:
            pass
        print(colours.CGREY + '[>] unbanall complete')

@urmom.command()
async def dmall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member == urmom.user:
            continue
        try:
            await member.send(message)
        except discord.Forbidden:
            print(colours.CRED + f"[-] {member.name} could not be dmed")
        else:
            print(colours.CGREEN + f"[+] {member.name} has recieved a dm with the content [-{message}-]")   
    print(colours.CGREY + "[>] dmall complete")

@urmom.command()
async def spampin(ctx, count):
    await ctx.message.delete()
    if count == None:
        count = 15
    else:
        async for message in ctx.message.channel.history(limit=int(count)):
            try:
                await message.pin()
                print(colours.CGREEN + '[+] pinned messages')
            except:
                print(colours.CRED + '[-] failed to pin messages')
                pass
    print(colours.CGREY + '[>] spampin complete')


@urmom.command()
async def spam(ctx, amount: int = None, *, message = None):
    await ctx.message.delete()
    if message is None:
        await ctx.send('what message do i spam', delete_after=3)
    elif amount is None:
        await ctx.send(f'how much do you want me to send {message}', delete_after=3)
    else:
        for lol in range(amount):
            await ctx.send(f'{message}')

@urmom.command()
async def selfpurge(ctx):
    await ctx.message.delete()
    urmoms=ctx.author
    async for urmom in ctx.channel.history(limit=8):
        if urmom.author.id == urmoms.id:
            try:
                await urmom.delete()
            except:
                pass

@urmom.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await urmom.change_presence(activity=game)

@urmom.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await urmom.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name=message, ))

@urmom.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await urmom.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=message))

@urmom.event
async def on_message(message):
        async for message in message.channel.history(limit=1):
            if "discord.gift" in message.content:
                if nitrosniper == "True":
                    code = re.search("discord.gift/(.*)", message.content).group(1)
                    if len(code) != 16:
                        print(colours.CRED + '[>] nitro sniper: fake link')
                    else:
                        headers = {"Authorization": token}
                        check = requests.post(
                            f"https://discordapp.com/api/v7/entitlements/gift-codes/{code}/redeem",
                            headers=headers,
                        ).text
                        if "This gift has been redeemed already." in check:
                            print(colours.CRED + "[>] nitro sniper: this gift has already been redeemed")
                        elif "subscription_plan" in check:
                            print(colours.CGREEN + "[+] nitro sniper: valid gift enjoy your free nitro")
                        elif "Unknown Gift Code" in check:
                            print(colours.CRED + '[>] nitro sniper: invalid code')
                else:
                    pass
        await urmom.process_commands(message)

@urmom.event
async def on_message(message):
    async for message in message.channel.history(limit=1):
        if 'Someone Dropped' in message.content:
            if slotbot == 'True':
                if message.author.id == '346353957029019648':
                    await ctx.send('~grab', delete_after=1)
                else:
                    pass
            else:
                pass
        else:
            pass   
    await urmom.process_commands(message)

@urmom.command() 
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title='xy selfbot', colour=0xffffff)
    embed.add_field(name='nuke', value='`nuke`, `unbanall`, `banall`')
    embed.add_field(name='misc', value='`dmall`, `spampin`, `spam`, `playing`, `watching`, `streaming`, `selfpurge`')
    embed.set_thumbnail(url=f'{ctx.message.author.avatar_url}')
    embed.set_footer(text=f'created by fork#6983\nnitro sniper: {nitrosniper}\nslotbot: {slotbot}')
    await ctx.send(embed=embed)

@urmom.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colours.CVIOLET + f"""                                                 
▄▀▀▄  ▄▀▄  ▄▀▀▄ ▀▀▄      ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄     ▄▀▀▀█▄    ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀█▀▀▄ 
█    █   █ █   ▀▄ ▄▀     █ █   ▐ ▐  ▄▀   ▐ █    █     █  ▄▀  ▀▄ ▐ ▄▀   █ █      █ █    █  ▐ 
▐     ▀▄▀  ▐     █          ▀▄     █▄▄▄▄▄  ▐    █     ▐ █▄▄▄▄     █▄▄▄▀  █      █ ▐   █     
     ▄▀ █        █       ▀▄   █    █    ▌      █       █    ▐     █   █  ▀▄    ▄▀    █      
    █  ▄▀      ▄▀         █▀▀▀    ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀ █         ▄▀▄▄▄▀    ▀▀▀▀    ▄▀       
  ▄▀  ▄▀       █          ▐       █    ▐     █        █         █    ▐            █         
 █    ▐        ▐                  ▐          ▐        ▐         ▐                 ▐   \n
 logged is as: {urmom.user}\n
 prefix: {prefix}\n
 nitro sniper: {nitrosniper}\n
 slotbot sniper: {slotbot}\n
 """)

urmom.run(token, bot=False)