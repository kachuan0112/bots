import discord
import os

from itertools import cycle
from discord.ext import commands , tasks

################################################

bot = commands.Bot(command_prefix= "=" , case_insensitive=True, description="Testing propose only")

bot.remove_command("help")

################################################

status = cycle(
    ['=help','=play','In Devolopment'])

@bot.event
async def on_ready():
    change_status.start()
    print(f"{bot.user.name} is ready to use".format(bot))

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

################################################

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

################################################

bot.run(TOKEN)