from re import T
import discord
import random
from discord.ext import commands
from asyncio import *
import asyncio
import datetime
from discord import colour
from discord import embeds
from discord.ext import tasks


class CONFIG:
    TOKEN = "OTUwOTg1MTg4NjQ3Nzk2NzQ3.Yig3-Q.rhlLLYxt2p6P6il9KiqxTNjYsTk"  # Tokeno inja bezar
    PREFIX = "!"


winnerr = [0x00e3f1, 0x008810, 0xecb600]
startt = [0x060eb9, 0xb90609, 0x000000]
err = [0xf100b1, 0x29041f, 0xff5300]

client = commands.Bot(command_prefix=CONFIG.PREFIX)
client.remove_command("help")





@client.event
async def on_ready():
  print(f"Developer's {len(client.users)}, In {len(client.guilds)} Server's Is Rune:)")
  while True:
      servers = client.guilds
      servers.sort(key=lambda x: x.member_count, reverse=True)
      y = 0
      for x in client.guilds:
            y += x.member_count
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Over {len(client.guilds)}+ Servers! , See {y}+ Users!",status=discord.Status.idle), status=discord.Status.idle)
      await asyncio.sleep(60)
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Over {len(client.guilds)}+ Servers! , See {y}+ Users!",status=discord.Status.idle), status=discord.Status.idle)
      await asyncio.sleep(60)



    

@client.command(aliases=["Gstart", "GSTART", "giveawaystart", "GIVEAWAYSTART"])
@commands.has_permissions(manage_channels=True)
async def gstart(ctx, mins : int=None, * , prize: str=None):
    if mins == None:
        embed = discord.Embed(title="Please Enter Your Time In The Middle Section", colour=random.choice(err))
        embed.set_footer(text="Example : $gstart (Time) (Prize)", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    elif prize == None:
        embed = discord.Embed(title="Please Enter Your Prize In The Last Section", colour=random.choice(err))
        embed.set_footer(text="Example : $gstart (Time) (Prize)", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        amount = 1
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title = "Give Away 💎", description = f"**Prize: ||{prize}|| 💎**", colour =random.choice(startt))


        end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

        start = ctx.message.created_at
        
        embed.add_field(name = "🏗 Hosted By :", value = f"<@{ctx.author.id}>")
        embed.add_field(name = "⏳ Ended :", value = f"||{end}||", inline=False)
        embed.add_field(name = "⏱ Started :", value = f"{start}", inline=False)
        embed.add_field(name = "📶 Tips :", value = "Click on 🎉", inline=False)
        embed.set_footer(text = f"Finish in {mins} Minutes")
        my_msg = await ctx.send(embed = embed)
        



        await my_msg.add_reaction("🎉")
        


        await asyncio.sleep(mins*60)


        new_msg = await ctx.channel.fetch_message(my_msg.id)


        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(client.user))

        winner = random.choice(users)


        embed = discord.Embed(title = "Give Away 💎", colour =random.choice(winnerr))
        embed.add_field(name = "🏗 Hosted By :", value = f"<@{ctx.author.id}>", inline=False)
        embed.add_field(name = "🏆 Winner :", value = f"<@{winner.id}>", inline=False)
        embed.add_field(name = "🎁 Prize :", value = f"{prize}", inline=False)
        embed.set_footer(text = "Finish")

        await my_msg.edit(embed=embed)

        await ctx.send(f"You Are a Winner <@{winner.id}>🏆")


@client.command(aliases = ['r'])
@commands.has_permissions(manage_messages = True)
async def groll(ctx, msg_id : int=None):
    if msg_id == None :
        embed = discord.Embed(title="Please Enter Giveaway Message ID", colour=random.choice(err))
        embed.set_footer(text="Example : $groll 951351715953422222", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else :
        new_msg_1 = await ctx.channel.fetch_message(msg_id)
        users = await new_msg_1.reactions[0].users().flatten()
        users.pop(users.index(client.user))
        winner = random.choice(users)
        await ctx.send(f"You are a New Winner {winner.mention}🏆")

        







    
    









client.run(CONFIG.TOKEN)