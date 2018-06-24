"""import google_api_python_client"""
import json
import discord
import googleapiclient
import oauth2client
import gspread

from discord import Game
from discord.ext.commands import Bot
from pprint import pprint
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from configparser import ConfigParser

#Loads in information from the demm.ini file
parser = ConfigParser()
parser.read('demm.ini')

TOKEN = parser.get('Discord Settings', 'token')
CADET_SHEET_ID = parser.get('Google Settings', 'cadet_sheet_id')
BOT_PREFIX = parser.get('Discord Settings', 'bot_prefix')

VERSION = '1.0'

client = Bot(command_prefix=BOT_PREFIX)

"""---------------------------------------------------------------------------------------------------"""

"""Starting Command to Authorize Google Drive And Sheets"""

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('DEMemberManager-48121228118a.json', scope)

gc = gspread.authorize(credentials)
"""---------------------------------------------------------------------------------------------------"""



#newcadet: Add new Cadet to the Dark Echo Cadet List

@client.command(name="newcadet",
                discription='adds new cadet information to spreadsheet',
                breif='add cadet to list',
                pass_context=True)
async def newcadet(context):
    """Pull Information From Discord Command Message"""
    Recruter_dirty = context.message.author
    Cadet_ID_Dirty = context.message.raw_mentions
    Date_Dirty = context.message.timestamp

    #Convert Cadet ID to Nickname on Server
    Cadet_ID_Dirty_STRING = str(Cadet_ID_Dirty)
    Cadet_ID_Clean = Cadet_ID_Dirty_STRING[2:20]
    Cadet_Name_Dirty = context.message.server.get_member(Cadet_ID_Clean).nick
    Cadet_Name_Clean = str(Cadet_Name_Dirty)
    if Cadet_Name_Clean == 'None': #Checks if the person has a nickname on the server if none then it pulls the Username
        Cadet_Name_Dirty = context.message.server.get_member(Cadet_ID_Clean)
        Cadet_Name_Clean = str(Cadet_Name_Dirty)
        Recruter_Clean = str(Recruter_dirty)
        Date_Clean = str(Date_Dirty)
        cadet_sheet = gc.open_by_key(CADET_SHEET_ID).sheet1
        cadet_sheet.append_row([Cadet_Name_Clean[:-5], Date_Clean[:-13], Recruter_Clean[:-5], "PC"])
        await client.say('Cadet ' + Cadet_Name_Clean + ' has been added to the roster ' + context.message.author.mention)
    else:
        Recruter_Clean = str(Recruter_dirty)
        Date_Clean = str(Date_Dirty)
        cadet_sheet = gc.open_by_key(CADET_SHEET_ID).sheet1
        cadet_sheet.append_row([Cadet_Name_Clean, Date_Clean[:-13], Recruter_Clean[:-5], "PC"])
        await client.say('Cadet ' + Cadet_Name_Clean + ' has been added to the roster ' + context.message.author.mention)



@client.command(name='status',
                description='What is the status of the Bot',
                breif='Bot Status',
                pass_context=True)
async def status(context):
    await client.say("Logged in as " + client.user.name + " " + VERSION + context.message.author.mention)





@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Ready and Waiting"))
    print("Logged in as " + client.user.name + " " + VERSION)



client.run(TOKEN)