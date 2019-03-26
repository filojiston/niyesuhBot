import discord
from discord.ext import commands
import random

class Fun:
    def __init__(self, client):
        self.client = client

    @commands.command(
        pass_context = True,
        name = '8ball'
    )
    @commands.cooldown(1, 5)
    async def _8ball(self, ctx, *args: str):
        replies = ['Kesinlikle', 'Gördüğüm kadarıyla, evet', ' Biraz belirsiz, tekrar dene', 'Bana öyle bakma',
        'Kesinlikle öyle', 'Çoğunlukla', 'Sonra tekrar dene', 'Yanıtım hayır',
        'Kuşkusuz', 'Dışarıdan iyi görünüyor', 'Şimdi söylemesem daha iyi', 'Kaynaklarım hayır diyor',
        'Evet, elbette', 'Evet', 'Şimdi kehanette bulunamam', 'Pek iyi görünmüyor',
        'Bana güvenebilirsin', 'Belirtiler olduğu yönünde', 'Konsantre ol ve tekrar sor', 'Çok şüpheli']

        index = random.randint(0, (len(replies) - 1))
        isFound = False

        if (len(args) == 0):
            return
        else:
            for word in args:
                if '?' in word:
                    isFound = True

        if isFound:
            await self.client.say('{}, {}'.format(ctx.message.author.mention, replies[index]))
        else:
            await self.client.say('Bu bir soru gibi görünmüyor :thinking:')

    @commands.command(
        pass_context = True,
        name = 'coinflip',
        aliases = ['cflip', 'yazitura']
    )
    @commands.cooldown(1, 3)
    async def _coinflip(self, ctx, *args: str):
        if (len(args) > 0):
            return
        else:
            status = ['yazı', 'tura']
            index = random.randint(0, (len(status) - 1))
            await self.client.say('{} , **{}**'.format(ctx.message.author.mention, status[index]))

    @commands.command(
        pass_context = True,
        name = 'choose',
        aliases = ['sec']
    )
    @commands.cooldown(1, 3)
    async def _choose(self, ctx, *args: str):
        arg_len = len(args)
        if (arg_len < 2):
            await self.client.say('yetersiz seçenek.', delete_after = 2)
        else:
            if args[0].isdigit():
                num = int(args[0])
                if not arg_len >= num + 2:
                    await self.client.say('yetersiz seçenek.', delete_after = 2)
                else:
                    arg_list = list(args[1:])
                    result_list = random.sample(arg_list, num)
                    for i in range(0, len(result_list)):
                        result_list[i] = '**' + result_list[i] + '**'
                    result = ', '.join(result_list)

                    await self.client.say('{},  i choose: {}'.format(ctx.message.author.mention, result))
            else:
                index = random.randint(0, arg_len - 1)
                result = args[index]
                await self.client.say('{},  i choose: **{}**'.format(ctx.message.author.mention, result))

    @commands.command(
        pass_context = True,
        name = 'say',
        aliases = ['soyle', 'echo']
    )
    @commands.cooldown(1, 3)
    async def _say(self, ctx, *args: str):
        if (len(args) == 0):
            await self.client.say('{}, neyi? '.format(ctx.message.author.mention))
        else:
            output = ' '.join(args)
            await self.client.delete_message(ctx.message)
            await self.client.say('{}'.format(output))

    @commands.command(
        pass_context = True,
        name = 'roll'
    )
    @commands.cooldown(1, 3)
    async def _roll(self, ctx, *args: str):
        if (len(args) != 1):
            return

        try:
            rolls, limit = map(int, args[0].split('d'))
        except Exception:
            await self.client.say('format has to be in NdN.')
            raise Exception
            return

        temp = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        result_list = temp.split(', ')
        for i in range(len(result_list)):
            result_list[i] = '**' + result_list[i] + '**'

        result = ', '.join(result_list)
        await self.client.say('{}, results.. -> {}'.format(ctx.message.author.mention, result))



def setup(client):
    client.add_cog(Fun(client))
