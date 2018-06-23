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

VERSION = '1.0'
TOKEN = 'YOUR DISCORD BOT TOKEN HERE'
CADET_SHEET_ID = 'YOUR SHEET ID HERE'
MEMBER_SHEET_ID = ''
BOT_PREFIX = "#"

client = Bot(command_prefix=BOT_PREFIX)

"""---------------------------------------------------------------------------------------------------"""

"""Starting Command to Authorize Google Drive And Sheets"""

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('YOUR CREDENTIALS FILE HERE', scope)

gc = gspread.authorize(credentials)
"""---------------------------------------------------------------------------------------------------"""





@client.command(name="new",
                discription='adds new cadet information to spreadsheet',
                breif='add cadet to list',
                pass_context=True)
async def new(context):
    Recruter_dirty = context.message.author
    Cadet_ID_Dirty = context.message.raw_mentions
    Date_Dirty = context.message.timestamp
    Cadet_ID_Dirty_STRING = str(Cadet_ID_Dirty)
    Cadet_ID_Clean = Cadet_ID_Dirty_STRING[2:20]
    Cadet_Name_Dirty = context.message.server.get_member(Cadet_ID_Clean)
    print(Recruter_dirty)
    print(Cadet_ID_Dirty)
    print(Date_Dirty)
    print(Cadet_Name_Dirty)
    print(Cadet_ID_Clean)
    Recruter_Clean = str(Recruter_dirty)
    Cadet_Name_Clean = str(Cadet_Name_Dirty)
    Date_Clean = str(Date_Dirty)
    Cadet_NICK =
    print(Cadet_NICK)
    cadet_sheet = gc.open_by_key(CADET_SHEET_ID).sheet1
    cadet_sheet.append_row([Cadet_Name_Clean, Date_Clean, Recruter_Clean])



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