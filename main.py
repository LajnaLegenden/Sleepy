import discord
from discord.ext import commands,tasks
import time;
import os;
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?',
                   description="asd", intents=intents)


dcTimer = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def timer(ctx, timer: float):
    """Adds two numbers together."""
    vcToKick =None
    for vc in ctx.guild.voice_channels:
      for member in vc.members:
          if member == ctx.author:
              vcToKick = vc;
    
    dcTimer[vcToKick] = time.time() + timer*60;
    await ctx.send(dcTimer[vcToKick])

@tasks.loop(minutes=1)
async def send():

    """Sends something every x minutes"""

    response = "blah blah blah"

    for vc in dcTimer:
        print(vc,dcTimer[vc]);
        if dcTimer[vc] < time.time():
            kick_channel = await vc.guild.create_voice_channel("kick")
            for m in vc.members:
                await m.move_to(kick_channel)
            await kick_channel.delete()

@send.before_loop
async def before():
    await bot.wait_until_ready()

send.start()
print(os.getenv('DISCORD'))
bot.run('ODE5NTcwNTY4NTc5Nzc2NTM0.YEoikg.LUiuMat3gNYPf3SwDYqrYdvCUO4')
