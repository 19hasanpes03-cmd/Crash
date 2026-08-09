import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} başarıyla aktif oldu!')

@bot.command()
async def panel(ctx):
    await ctx.send("Bot çalışıyor! Stok paneli yakında aktif olacak.")

bot.run("MTUzNTk4NTIzNzQ1OTIxNDM4OA.GHHWNl.d-Ra2rvWo6bfD76TJwBJqyOUpyda5mu3w2m0bE")
