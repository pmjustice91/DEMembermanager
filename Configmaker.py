from configparser import ConfigParser

config = ConfigParser()

config['Discord Settings'] = {
    'TOKEN': 'Your Token Here',
    'bot_prefix': '!!'
}

config['Google Settings'] = {
    'MEMBER_SHEET_ID': 'Your Google Sheets ID Here',
    'CADET_SHEET_ID': 'Your Google Sheets ID Here'
}

with open('./demm.ini', 'w') as ini_file:
    config.write(ini_file)