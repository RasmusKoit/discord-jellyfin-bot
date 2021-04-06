import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix=".", help_command=None, intents=discord.Intents.all())
GUILD_ID = 829049493679898645
@bot.event
async def on_message(message):
    roles = bot.get_guild(GUILD_ID).get_member(message.author.id).roles
    for role in roles:
        print(role)
    await bot.process_commands(message)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.help for help'))
    guild = bot.get_guild(GUILD_ID)
    print(guild)

@bot.command()
async def help(ctx):
    await ctx.channel.send(embed=help_embed())


@bot.command(
    brief="Download your favorite anime",
    aliases=['dl']
)
async def download(ctx, link=""):
    if link == "":
        await ctx.channel.send("Empty link")
    else:
        await ctx.channel.send("pong:" + link)


def help_embed() -> discord.Embed:
    embed = discord.Embed(
        title='Lap Anime anime downloader',
        type='rich',
        color=0xFFC300
    )
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/icons/766284107432067102/a93205363524325d3374f0b7bacdf079.png?size=128')
    embed.add_field(name='Use', value='Tired of watching the same old animes?\n'
                                      'Download more anime!')
    embed.add_field(name='Commands', value='`.download` or `.dl` torrent link\n'
                                           '`.help` tutorial on how to use the bot')
    return embed


bot.run(DISCORD_TOKEN)
