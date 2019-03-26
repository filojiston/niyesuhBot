import discord
from discord.ext import commands
import random

TOKEN = 'your token here'

client = commands.Bot(command_prefix = '>')
# client.remove_command('help')

extensions = ['mod', 'utility', 'fun']

IDs = {
    "your admin dict -> key : id format"
}

@client.event
async def on_ready():
    print('Logged on as {0}'.format(client.user))
    await client.change_presence(game = discord.Game(name = 'the best LoL player -> "Liseyna"', type=3), status = discord.Status.idle)

@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(ctx.message.channel, content = 'command is on a %.2fs cooldown' % error.retry_after)
    elif isinstance(error, commands.CommandNotFound):
        error_name = ctx.message.content[1:].split()[0]
        await client.send_message(ctx.message.channel, content = 'There is no **{0}** command here.'.format(error_name))
    raise error

# for loading an extension
@client.command(pass_context = True, name = 'load', hidden = True)
@commands.cooldown(1, 3)
async def _load(ctx, extension):
    ID_list = list(IDs.values())
    if ctx.message.author.id in ID_list:
        try:
            client.load_extension(extension)
            print('{} loaded.'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

# for unloading an extension
@client.command(pass_context = True, name = 'unload', hidden = True)
@commands.cooldown(1, 3)
async def _unload(ctx, extension):
    ID_list = list(IDs.values())
    if ctx.message.author.id in ID_list:
        try:
            client.unload_extension(extension)
            print('{} unloaded.'.format(extension))
        except Exception as error:
            print('{} cannot be unloaded. [{}]'.format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('{} loaded.'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    client.run(TOKEN)
