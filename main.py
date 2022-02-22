import discord , os , py_dotenv , json
from discord.ext import commands

py_dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

intents = discord.Intents.all()
default_prefix = "chig"

def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("_")(bot, message)

    with open("./utils/resources/prefixes.json") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("_")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix , default_prefix)(bot, message)


bot = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive=True, strip_after_prefix = True , help_command = None)


for filname in os.listdir(f"./commands"):
    if filname.endswith(".py"):
        bot.load_extension(f"commands.{filname[:-3]}")

for filname in os.listdir("./events"):
    if filname.endswith(".py"):
        bot.load_extension(f"events.{filname[:-3]}")

for filname in os.listdir("./economy"):
    if filname.endswith(".py"):
        bot.load_extension(f"economy.{filname[:-3]}")


bot.run(os.getenv("TOKEN"))


# python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
# python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"
