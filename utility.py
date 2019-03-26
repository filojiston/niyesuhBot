import discord
from discord.ext import commands

class Utility:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True,
        name = 'avatar',
        description = 'returns the avatar url of the mentioned user.'
    )
    async def _avatar(self, ctx):
        if ctx.message.mentions.__len__() == 0:
            user = ctx.message.author
            avatar_url = user.avatar_url
            await self.client.say('{}\'s avatar is here: {}'.format(user.mention, avatar_url))
        elif ctx.message.mentions.__len__() != 1:
            await self.client.say('Please mention just 1 user.', delete_after = 3)
        else:
            user = ctx.message.mentions[0]
            avatar_url = user.avatar_url
            await self.client.say('{}\'s avatar is here: {}'.format(user.mention, avatar_url))

    @commands.command(pass_context=True,
        name = 'clear',
        description = 'clears the given number of messsages.' )
    @commands.cooldown(1, 5)
    @commands.has_permissions(administrator = True)
    async def _clear(self, ctx, amount=20):
        channel = ctx.message.channel
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount)):
            messages.append(message)
        try:
            await self.client.delete_messages(messages)
            await self.client.say('**{0}** messages has been deleted. :white_check_mark:'.format(len(messages)), delete_after = 2.5)
        except discord.errors.ClientException as error:
            await self.client.say('Sadece **[2, 100]** aralığında mesaj silinebilir. :x:', delete_after = 5)
            raise error
        except discord.errors.HTTPException as error:
            await self.client.say('**14** günden daha eski mesajlar silinemez. :x:', delete_after = 5)
            raise error

def setup(client):
    client.add_cog(Utility(client))
