import discord
from discord.ext import commands
import time

IDs = {
    'same as __main.py__'
}

class Mod:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, hidden=True,
        aliases = ['hadiköyüne', 'yallahköyüne']
    )
    async def logout(self, ctx):
        ID_list = list(IDs.values())
        if ctx.message.author.id in ID_list:
            await self.client.delete_message(ctx.message)
            await self.client.logout()

    @commands.command(
        pass_context = True,
        name = 'ping',
        hidden = True
    )
    async def _ping(self, ctx):
        before = time.monotonic()
        message = await self.client.say('pong!')
        ping = (time.monotonic() - before) * 1000
        await self.client.edit_message(message, new_content = 'ping -> **{}** ms'.format(int(ping)))

def setup(client):
    client.add_cog(Mod(client))
