import discord
import asyncio
import os
import functools
import itertools
import math
import random

import youtube_dl
import urllib.parse, urllib.request, re
import requests

from discord import Embed, FFmpegPCMAudio
from discord.utils import get

import random
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv('.env')

client = commands.Bot(command_prefix = "k.",
                      case_insensitive = True,
                      activity = discord.Activity(type=discord.ActivityType.watching, name='over the cookies while scouting \'k.\' commands'),
                      status = discord.Status.idle
                      )
client.remove_command('help')

@client.event
async def on_ready():
    print('Kaze has taken off safely.')


@client.command()
async def die(ctx):
    if ctx.author.id in [436973854485643264]:
        await ctx.send(f"Bye Daddy {ctx.author.display_name}!")
        await client.logout()

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = 'absobutely no reason'):
    if ctx.author != member:
        await member.ban(reason = reason)
        await ctx.send(f'{member.mention} has been banned by {ctx.author} for {reason}')
    else:
        await ctx.send(f"Why are you like this... You DO know that you cannot ban {ctx.author} because THAT IS LITERALLY DUMB")

@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} has been unbanned')
            return


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)

        kick = discord.Embed(
        title=f":boot: Kicked {user.name}!",
        description=f"Reason: {reason}\nBy: {ctx.author.mention}"
        )

        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name='Muted')
        await ctx.author.add_roles(member, role)

        embed=discord.Embed(

        title="User Muted!",
        description="**{0}** was muted by **{1}**!".format(member, ctx.message.author),
        colour = discord.Colour(0Xb8f2f2)
        )

        await ctx.send(embed=embed)

        try:
            role = discord.utils.get(member.guild.roles, name='Muted')
            await ctx.author.add_roles(member, role)
        except discord.ext.commands.errors.MissingRequiredArgument:
            await ctx.send('C\'mon mod, please specifiy a user to mute')

        else:
           embed=discord.Embed(

           title="Permission Denied.",
           description="You don't have permission to use this command.",
           colour = discord.Colour(0Xb8f2f2)
           )

           await ctx.send(embed=embed)


@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name='Muted')
        await ctx.author.remove_roles(role)


        embed=discord.Embed(

        title="User Unmuted!",
        description="**{0}** was muted by **{1}**!".format(member, ctx.message.author),
        colour = discord.Colour(0Xb8f2f2)
        )

        await ctx.send(embed=embed)


@client.command()
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'Hell yeah!',
                'Without a doubt.',
                'Yes – definitely.',
                'Of course you dumb dumb.',
                'As I see it, yes.',
                'Most likely.',
                'Yeah pretty much.',
                'Daddy Mizu says yes!',
                'The council says yes.',
                'Uhhhhhhhhh.',
                'I will tell you later.',
                'Better not tell you now.',
                'It is a secret.',
                'Wait till your birthday for an answer.',
                'Eh...no.',
                'Nu!.',
                'Daddy Mizu says nu!',
                'Of course not.',
                'Very doubtful.']
    await ctx.send(f":8ball: **{ctx.author.name}'s Question:** *{question}*\n:8ball: **My wisdom:** *{random.choice(responses)}*.")

@client.command()
async def whoisToru(ctx):
    await ctx.send('Toru is actually ||Toru||')

@client.command()
async def americaisbest(ctx):
    await ctx.send('https://youtu.be/IdKm5lBb2ek?t=118')

@client.command()
async def marryme(ctx):
    await ctx.send('No thanks, I shall be a good child and only do as Oto-san wishes.')

@client.command()
async def loli(ctx):
    await ctx.send('Lolis are the grand supreme beings')

@client.command()
async def cookie(ctx):
    await ctx.send('I am eating a cookie...here have one :cookie:')

@client.command()
async def milk(ctx):
    await ctx.send('*sip* Here, have some calcium boner :milk:')

@client.command()
async def dice(ctx):
    responses = ['1',
                '2',
                '3',
                '4',
                '5',
                '6']
    await ctx.send(f':handshake: *rolling the dice* \n\n:game_die: You rolled a {random.choice(responses)}')

@client.command()
async def jam(ctx):
    await ctx.send('This is :fire: *jams*')

@client.command()
async def back(ctx):
    await ctx.send('*Kaze is awake and has landed safely*')

# hell- i mean music commands

youtube_dl.utils.bug_reports_message = lambda: ''

# rest of music code is in cogs.music

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
