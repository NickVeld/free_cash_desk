import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GShell:
    def __init__(self):
        self.ssheet = None
        self.gspread_key = ""

    def get_from_config(self, config):
        self.gspread_key = config["gspread_key"]
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name("FreeCashDesk.json", scope)
        self.ssheet = gspread.authorize(credentials).open_by_key(self.gspread_key)

    def send(self, address, info):
        sheet = self.ssheet.worksheet(address[0])
        for column in range(len(info)):
            for row in range(min(3, len(info[column]))):
                sheet.update_cell(row + address[1], column + address[2], info[column][row])

    def get_table(self):
        return "https://docs.google.com/spreadsheets/d/" + self.gspread_key
