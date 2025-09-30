import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# ---------- Flask server باش يبقى البوت شغال ----------
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ---------- Discord Bot ----------
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def z9dm(ctx):
    channel_id = 1420070323444781120  # حط هنا ID ديال القناة
    channel_mention = f"START ➡️ <#{channel_id}>"

    embed = discord.Embed(
        title="ZAN9A ROLEPLAY STATUS",
        description="",
        color=0xff0000
    )
    embed.add_field(name="WHITELIST [ ON ✅ ]", value="", inline=False)
    embed.set_image(url="https://i.postimg.cc/WpX5qf6d/standard.gif")

    sent = 0
    failed = 0

    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(content=f"{channel_mention}", embed=embed)
            sent += 1
        except:
            failed += 1

    await ctx.send(f"✅ الإعلان تْصيفط لـ {sent} عضو.\n❌ ما وصلش لـ {failed} عضو (ربما سادين DM).")

# ---------- Start ----------
keep_alive()
bot.run(os.getenv("TOKEN"))
