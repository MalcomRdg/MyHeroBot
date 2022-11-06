import discord
import time

#INPUT USER

Asset = "ETHUSDT"
Period = ""



messages = "indiators analysis for the 05/11/2022 based on 4H period:  \n -Simple Moving Average : Bullish sign \n -RSI: Oversold \n -Ichimoku cloud : Neutral \n -BBAND : high volatility detected (consider taking small position)"


TOKEN = "OTUwMDczMDg2NjY4MDYyNzYx.YiTmgw.g9mwRU7aA0hPH4Nh6Tqp68is8V0"
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    channel = client.get_channel(1038539130088468543)
    messagesf = f'{messages}'
    await channel.send(messagesf)

    #user = await client.fetch_user(464813643775868928)
    #await user.send(messages)
    await client.close()
    time.sleep(1)


client.run(TOKEN)