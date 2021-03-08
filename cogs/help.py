from discord.ext import commands
from typing import TYPE_CHECKING
import discord

if TYPE_CHECKING:
    from bot import Aria # noqa


command_list = [
    '`help` -> このメッセージを表示します。',
    '`join` -> ユーザー登録をします。',
    '`vq [思考秒数] [連続回数]` -> ゲームを開始します。',
    '``'
    ''
]


class Help(commands.Cog):
    def __init__(self, bot: 'Aria') -> None:
        self.bot = bot

    @commands.command()
    async def help(self, ctx: commands.Context) -> None:
        embed = discord.Embed(
            title='Vocaleague',
            description='レイナのコマンド一覧を表示します。',
            timestamp=ctx.message.created_at,
            color=0x1976D2,
        )
        embed.add_field(
            name='リンク一覧',
            value='[招待URL](https://discord.com/api/oauth2/authorize?client_id=\
                  711804442374307870&permissions=8&scope=bot)\n'
                  '不明な点があったら[twitter](https://twitter.com/SAS3279)にDMしてください',
            inline=False,
        )
        embed.add_field(
            name='コマンド一覧',
            value='\n'.join([f'{ctx.prefix}' + cmd for cmd in command_list]),
            inline=False,
        )
        await ctx.send(embed=embed)


def setup(bot: 'Aria') -> None:
    bot.add_cog(Help(bot))
