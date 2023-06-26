import disnake
from disnake.ext import commands
from disnake.ui import View, Select
from disnake import SelectOption

class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    async def help(self, ctx):
        embed = disnake.Embed(title="Помощь по командам")
        embed.url = "https://discord.gg/xppzwKWyvC"
        embed.description = "Тут мы собрали все команды бота и разбили их на категории, выберите нужную и увидите список команд из этой категории.\np.s Также вы можете ввести `/` и просмотреть команды по аватарке бота"
        embed.color = disnake.Color.random()

        select_options = [
            SelectOption(label="🔑 Утилиты", value="utils", description="Различные возможно полезные штуки."),
            SelectOption(label="🛠️ Модерация", value="mod", description="Страх хадилки брадилки"),
            SelectOption(label="⚙️ Настройки", value="setg", description="Где? Как? Почему?"),
            SelectOption(label="🛡 Безопасность", value="safe", description="Мы заботимся о вашей безопасности!"),
            SelectOption(label="🍿 Развлекательные", value="heha", description="Ура веселью!")
        ]

        view = View()
        select = Select(placeholder="Выберите категорию", min_values=1, max_values=1, options=select_options)
        view.add_item(select)

        await ctx.reply(embed=embed, view=view)

        select.callback = self.select_callback
    
    async def select_callback(self, interaction):
        category = interaction.data["values"][0]
        embed = disnake.Embed(title="")
        embed.url = "https://discord.gg/xppzwKWyvC"
        embed.color = disnake.Color.random()
    #   category = interaction.message.content.lower()
        if category == "mod":
            embed.title = "**Модерация**:"
            embed.description = "_ _`k.tickets` - Вызывает меню создания тикетов.\n`k.report` - Жалоба на пользователя.\n`k.warn` - Выдать предупреждение юзеру.\n`k.timeout` - Выдать мут юзеру.\n`k.ban` - Забанить кого-либо.\n`k.kick` - Исключить пользователя.\n`k.clear` - Очистить мусор в чатике."
        elif category == "safe":
            embed.title = "**Безопасность**:"
            embed.description = "_ _`k.check` - Проверка URL-адреса на наличие фишинга.\n`k.verify` - Меню верификации пользователя (капча).\n`k.restore` - Попытка восстановить крэшнутый сервер + создание одного канала в случае их удаления.\n`k.lockdown` - Отключение возможности отправки сообщений в канал у упомянутой роли."
        elif category == "heha":
            embed.title = "**Развлекательные**:"
            embed.description = "_ _`k.neko` - Найдет для вас Неко-тян.\n`k.question` - Бот ответит на ваш вопрос.\n`k.hug` - Обнимашки.\n`k.pat` - Погладить кого-то.\n`k.drake` - Генерирует мем с текстом (только на английском).\n`/rp` - Взаимодействие с пользователем (разрешено)."
        elif category == "setg":
            embed.title = "**Настройки**"
            embed.description = "_ _`k.settings verify` - Установка роли верификации.\n`k.settings warns` - Настройки предупреждений.\n`k.settings reports` - Настройки жалоб.\n`k.settings log` - Настройки логов.\n`k.settings welcomer` - Настройка приветствия.\n`k.settings tickets` - Настройка канала для создания тикетов."
        elif category == "utils":
            embed.title = "**Утилиты**"
            embed.description = "_ _`k.stats` - Статистика бота.\n`k.short` - Сократить ссылку.\n`k.check` - Проверить URL-адрес на наличие фишинга (экспериментально).\n`k.gpt` - Задать вопрос нейросети ChatGPT.\n`k.imagine` - Генерация картинки по запросу.\n`k.random` - Рандомизация различной ерунды.\n`k.calc` - Калькулятор для гениев.\n`k.profile` - Отображение вашего профиля.\n`k.steal` - Украсть эмодзи.\n`k.avatar` - Вывести аватар пользователя."
        await interaction.response.send_message(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(HelpCog(bot))
