import discord

from discord.ext import commands

import requests

import json

bot = commands.Bot(
  command_prefix='!'
)

client = discord.Client()

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user.name}')


def get_us():
    response = requests.get('http://covidtracking.com/api/us')
    data = json.loads(response.text)
    us = 'today: ' + str(data[0]['positiveIncrease']) + ' / total: ' + str(data[0]['positive'])
    return(us)


def get_state():
    response = requests.get('https://covidtracking.com/api/states')
    data = json.loads(response.text)
    state = 'today: ' + str(data[5]['positiveIncrease']) + ' / total: ' + str(data[5]['positive'])
    return(state)


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!us'):
        status = get_us()
        await message.channel.send(status)

    if msg.startswith('!ca'):
        status = get_state()
        await message.channel.send(status)


bot.run('TOKEN')
