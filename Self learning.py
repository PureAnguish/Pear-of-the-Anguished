# work with python 3.6
import discord, time, nltk, numpy, requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from discord.ext import commands
from discord.ext.commands import bot
import random

TOKEN = 65468126548721

client = discord.Client()

bot = commands.Bot(command_prefix='-')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('-hi'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('-8'):
        await message.channel.send(random.choice(['That is a resounding no:8ball:',
                                                  'Negative:8ball:',
                                                  'Abort!:8ball:',
                                                  'It is not looking likely:8ball:',
                                                  'Too hard to tell:8ball:',
                                                  'It is quite possible:8ball:',
                                                  'Definitely:8ball:',
                                                  'Hell yea boi!:8ball:',
                                                  'Yes:8ball:']))
        """Selects a random operator to ban on the attacking side"""
    elif message.content.startswith('-banA'):
        await message.channel.send(random.choice(['Ash:octagonal_sign:',
                                                  'Thermite:octagonal_sign:',
                                                  'Thatcher:octagonal_sign:',
                                                  'Blackbeard:octagonal_sign:',
                                                  'Capitao:octagonal_sign:',
                                                  'Maverick:octagonal_sign:',
                                                  'Hibana:octagonal_sign:',
                                                  'Montagne:octagonal_sign:',
                                                  'Twitch:octagonal_sign:',
                                                  'Lion:octagonal_sign:',
                                                  'Dokkaebi:octagonal_sign:',
                                                  'Sledge:octagonal_sign:',
                                                  'Buck:octagonal_sign:',
                                                  'IQ:octagonal_sign:',
                                                  'Nomad:octagonal_sign:',
                                                  'Gridlock:octagonal_sign:',
                                                  'Jackal:octagonal_sign:',
                                                  'Zofia:octagonal_sign:',
                                                  'Fuze:octagonal_sign:',
                                                  'Finka:octagonal_sign:',
                                                  'Glaz:octagonal_sign:',
                                                  'Blitz:octagonal_sign:',
                                                  'Ying:octagonal_sign:',
                                                  'Nøkk:octagonal_sign:',
                                                  'Amaru:octagonal_sign:']))
        """Selects a random operator to ban on defending side"""
    elif message.content.startswith('-banD'):
        await message.channel.send(random.choice(['Rook:octagonal_sign:',
                                                  'Doc:octagonal_sign:',
                                                  'Smoke:octagonal_sign:',
                                                  'Jager:octagonal_sign:',
                                                  'Mute:octagonal_sign:',
                                                  'Mozzie:octagonal_sign:',
                                                  'Mira:octagonal_sign:',
                                                  'Kaid:octagonal_sign:',
                                                  'Tachanka:octagonal_sign:',
                                                  'Kapkan:octagonal_sign:',
                                                  'Goyo:octagonal_sign:',
                                                  'Ela:octagonal_sign:',
                                                  'Warden:octagonal_sign:',
                                                  'Pulse:octagonal_sign:',
                                                  'Castle:octagonal_sign:',
                                                  'Caveira:octagonal_sign:',
                                                  'Valkyrie:octagonal_sign:',
                                                  'Clash:octagonal_sign:',
                                                  'Maestro:octagonal_sign:',
                                                  'Vigil:octagonal_sign:',
                                                  'Alibi:octagonal_sign:',
                                                  'Echo:octagonal_sign:',
                                                  'Lesion:octagonal_sign:',
                                                  'Frost:octagonal_sign:',
                                                  'Bandit:octagonal_sign:']))
    elif message.content.startswith('-stats'):
        print()
    print(message)
    print(message.author)
    await bot.process_commands(message)


@bot.command()
async def siege(content='repeating...'):
    def convUser(username):
        """Takes raw input from runSearch"""
        names = nltk.word_tokenize(username)
        global fnamelist
        fnamelist = names
        return names

    def getRank(x):
        tokpanel = str(x.find('div', id='season-10'))
        tokpanel = nltk.word_tokenize(tokpanel)
        del tokpanel[0:63]
        del tokpanel[1: len(tokpanel)]
        tokpanel[0] = tokpanel[0][-22:-16]
        tokpanel[0] = tokpanel[0].replace("-", "")
        tokpanel[0] = tokpanel[0].replace("rank", "")
        ranklist = ["Copper IV", "Copper III", "Copper II", "Copper I",
                    "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
                    "Silver IV", "Silver III", "Silver II", "Silver I",
                    "Gold III", "Gold II", "Gold I",
                    "Plat III", "Plat II", "Plat I",
                    "Diamond",
                    "Master"]
        rank = ranklist[int(tokpanel[0]) - 1]
        return rank

    def getWinLoss(x):
        infopanel = x.find('div', id='season-10')
        infopanelsmall = infopanel.find_all('div', class_='value')
        infopanelsmall = str(infopanelsmall)
        infopanel = nltk.word_tokenize(infopanelsmall)
        infopanelsmall = infopanelsmall.split('\n')
        winloss = infopanelsmall
        return winloss

    def getMMR(x):
        infopanel = x.find('div', id='season-10')
        infopanelsmall = infopanel.find_all('div', class_="value")
        infopanelsmall = str(infopanelsmall)
        infopanel = nltk.word_tokenize(infopanelsmall)
        infopanelsmall = infopanelsmall.split('\n')
        mmr = infopanelsmall[9]
        return mmr

    def getHMMR(x):
        infopanel = x.find('div', id='season-10')
        infopanelsmall = infopanel.find_all('div', class_="value")
        infopanelsmall = str(infopanelsmall)
        infopanel = nltk.word_tokenize(infopanelsmall)
        infopanelsmall = infopanelsmall.split("\n")
        hmmr = infopanelsmall[11]
        return hmmr

    def getCasualKD(x):
        mainpanel = str(x.find('div', class_='trn-stats'))
        mainpanel = nltk.word_tokenize(mainpanel)
        del mainpanel[0:375]
        del mainpanel[1:len(mainpanel)]
        KD = mainpanel[0]
        return KD

    def Search(x):
        site = "https://r6.tracker.network/profile/pc/" + x
        # set header to allow script to access site
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)
        page = urlopen(req)
        # parse the site saved in site variable
        soup = BeautifulSoup(page, "html.parser")
        return soup

    def runSearch(x):
        names = convUser(x)
        for i in range(0, len(names)):
            global fKD, fhmmr, fmmr, fwinloss, frank, fname, labels
            # calls each function to get player stats from single save
            fKD = getCasualKD(Search(names[i]))
            fhmmr = getHMMR(Search(names[i]))
            fmmr = getMMR(Search(names[i]))
            fwinloss = getWinLoss(Search(names[i]))
            frank = getRank(Search(names[i]))
            fname = names[i]
            # print the data out in a formatted way
            output = "Siege Stats: \n " + "Ubisoft ID: " + fname + "\n Rank: " + frank + "\n Casual KD: " + fKD + "\n Highest MMR: " + fhmmr + "\n Current MMR: " + fmmr + "\n Ranked Win/Loss: " + fwinloss
            return output

    await bot.say(runSearch(content))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('NjI5MjE4NzE5MzAxNjMyMDE5.XZWlnw.ikiKBI2z3GBrG4bt0cfgfBS6X0c')
