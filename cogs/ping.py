import disnake
import time
from disnake.ext import commands
from datetime import datetime, timezone
from datetime import timedelta


class ping(commands.Cog, name="Основное", description="Всякий бред"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time() 
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def stats(self, ctx):
        uptime = str(timedelta(seconds=int(round(time.time()-startTime))))
       # uptime = int(round(time.time()-startTime))
        embed = disnake.Embed(
            title="**Статистика бота**",
            description=f"Бот работает: **{uptime}**\n\n"
                        "__**Общая информация**__\n"
                        "Разработчик: **mr_fortuna**\n"
                        "Тестировщик(и): **helaney, 0qd7**\n"
                        "Команд использовано: **-**\n\n"
                        "__**Информация про меня**__\n"
                        "Язык программирования: **Python**\n"
                        "Библиотека: **Disnake**\n"
                        "Статус: **В разработке**\n"
                        f"Пинг: **{round(self.bot.latency * 1000)}ms**\n\n"
                        "__**Прочее**__\n"
                        "Команд у бота: **none**\n"
                        "Блэклист: **none юзеров**\n"
                        f"Пользователей: **{len(self.bot.users)}**\n"
                        f"Серверов: **{len(self.bot.guilds)}**",
            color=0x66c14f
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1044684301834395728/1072072754079207434/20230118_112247.jpg")
        embed.set_footer(icon_url=self.bot.user.avatar.url, text=f"Беспокоишься обо мне пупс?")
        disnake.ui.Button(label="Сервер поддержки", style=disnake.ButtonStyle.link, url="https://discord.gg/xppzwKWyvC")
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(ping(bot))