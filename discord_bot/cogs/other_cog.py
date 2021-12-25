import discord

from discord_slash import cog_ext , SlashContext
from discord.ext import commands

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Other_cog Loaded Succesfully.')

    @commands.command(name='botstop', aliases=['bstop'])
    async def botstop(self , ctx):
        print('好的wor')
        my_embed=(discord.Embed(title="[**Annoucment**]",description=f"\nBot will be stop and maintains in a few Minutes/Hours/Days depents of the issue."
                                                                            f'\nThanks for your understanding.'
                                                                            f"\nBot already stop working don't use commands until next annoucment."
                                                                            ,color=discord.Color.blurple())
        .add_field(name="Sincerely,",value="<@696599329011400775>" , inline=False)
        .set_footer(text="Thank you!",icon_url="https://cdn.discordapp.com/emojis/889708693925531658.png?size=96")
        
        )
        await ctx.send(embed=my_embed)
        await self.bot.logout()
        return
    
    @commands.command(aliases=["botstart" , "bstart"])
    async def test(self , ctx):
        my_embed=(discord.Embed(title="[**Annoucement**]",description=f"\n<@865454711233708033> Will be stop service until next annoucement."
                                                                    f"\nThe reason why stop is because of the host of error, the loops interrupt The API's and the bot error is to many, I have no ways, i need to put it none service."
                                                                    f"\nI'll try my best to service It and hope It can be fix for less than one week."
                                                                    f"\nFor compensate, I'll add more features and debug more commands."
                                                                    f"\nIf affect to your use, Im so sorry, but I have no other method."
                                                                    f"\nThanks for Your understanding."   

                                                        ,color=discord.Color.blurple())
        .add_field(name="Sincerely,",value="<@696599329011400775>" , inline=False)
        .set_footer(text="Thank you!",icon_url="https://cdn.discordapp.com/emojis/889708693925531658.png?size=96")
        
        )
        await ctx.send(embed=my_embed)

    @commands.command(name="lmao")
    async def lmao(ctx):
        my_embed=(discord.Embed(title="Lmao" , color=discord.Color.blurple())
    )

        await ctx.send(embed=my_embed)

    @cog_ext.cog_slash(name="lmao" , description="FUN FUN XD")
    async def lmao(ctx):
        my_embed=(discord.Embed(title="Lmao" , color=discord.Color.blurple())
    )

        await ctx.send(embed=my_embed)

    @commands.command(name="lmfao")
    async def lmfao(ctx):
        my_embed=(discord.Embed(title="Lmfao" , color=discord.Color.blurple())
    )

        await ctx.send(embed=my_embed)

    @cog_ext.cog_slash(name="lmfao" , description="FUN FUN MORE FUN XD")
    async def lmfao(ctx):
        my_embed=(discord.Embed(title="Lmfao" , color=discord.Color.blurple())
    )

        await ctx.send(embed=my_embed)


def setup(bot):
    bot.add_cog(Other(bot))
