import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="/", intents=disnake.Intents.all())


@bot.slash_command()
async def help(interaction: disnake.AppCmdInter):
    await interaction.send("U can use such commands as: /functions, /owner and /whysobad")

    @bot.slash_command()
async def functions(interaction: disnake.AppCmdInter):
    await interaction.send("Unfortunately, i dont have any specific functions yet :(")

    @bot.slash_command()
async def owner(interaction: disnake.AppCmdInter):
    await interaction.send("morsteenx is the owener of this server")

    @bot.slash_command()
async def whysobad(interaction: disnake.AppCmdInter):
    await interaction.send("The bot is still in development,so please be patient ;)")

bot.run(" ")