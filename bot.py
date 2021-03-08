from discord.ext import commands
from os import environ
from lib.database import Database
# from lib.question import Question
import discord
import json


class Zect(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
            help_command=None,
        )
        self.db = Database(self)
        # self.qt = Question(self)
        with open("json/question.json", mode="r", encoding='utf-8') as f:
            self.qu = json.load(f)
            f.close()

    async def on_ready(self):
        status = discord.Game("/vq - Vocaleague")
        # status = discord.Game("メンテナンス中")
        await self.change_presence(activity=status)
