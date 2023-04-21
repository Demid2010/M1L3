import discord
from logic import flip_coin, gen_pass

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
    if message.author == client.user:
        return
    if message.content.startswith("$Привет"):
        await message.channel.send("привки!")

    elif message.content.startswith("$пока"):
        await message.channel.send("Досвиданья!")
        
    elif message.content.startswith("$coin"):
        await message.channel.send(flip_coin())

    elif message.content == "$придумай пароль":
        await message.channel.send(gen_pass(10))


client.run("адрес бота")
