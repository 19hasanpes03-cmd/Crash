import discord
from discord.ext import commands
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Render'ın web servisi için arka planda port dinleyen mini sunucu
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot 7/24 aktif calisiyor!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

# Discord Bot Kodları
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

bot.run("MTUzNTk4NTIzNzQ1OTIxNDM4OA.GsRq0A.oUZbzLwAXm0JxkP8AFMiZ5Ma79CCjbNdydfXeU")
