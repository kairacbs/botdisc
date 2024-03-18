import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.reactions = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.name == "registro" and message.content.lower() == "registrar":
        await message.channel.send("Por favor, digite o apelido desejado para registrar no servidor.")

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            msg = await bot.wait_for('message', timeout=60.0, check=check)
            nome = msg.content
            await message.author.edit(nick=nome)
            await message.channel.send(f"Seu apelido foi registrado como {nome}.")
        except asyncio.TimeoutError:
            await message.channel.send("Você demorou muito para responder. Tente novamente mais tarde.")

bot.run('MTIxOTM0ODEzNTk2OTgyMDgwNQ.GKIUO5.APupWAeZAd4DR7akM7Plzkj-0jlNr9cRAsRMhA')