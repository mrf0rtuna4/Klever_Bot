from disnake.ext import commands
import jishaku
from jishaku.features.python import PythonFeature
from jishaku.features.root_command import RootCommand

class sous(PythonFeature, RootCommand):
    pass

def setup(bot: commands.Bot):
    jishaku.Flags.NO_UNDERSCORE = True
    jishaku.Flags.NO_DM_TRACEBACK = True
    jishaku.Flags.FORCE_PAGINATOR = True
    bot.add_cog(sous(bot=bot))
