import discord
from logic import flip, gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.content.startswith("$Привет"):
        await message.channel.send(f"{message.author.mention}привки!")

    if message.content.startswith("$пока"):
        await message.channel.send(f"{message.author.mention}Досвиданья!")

    if message.content.startswith("$подброс монетки"):
        await message.channel.send(f"{message.author.mention}")
        await message.channel.send(flip_coin())

    if message.content == "$придумай пароль":
        await message.channel.send(f"{message.author.mention}")
        await message.channel.send(gen_pass(10))


client.run("адрес бота")
