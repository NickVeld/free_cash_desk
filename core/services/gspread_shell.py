import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GShell:
    def __init__(self):
        self.ssheet = None

    def get_from_config(self, config):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name("FreeCashDesk.json", scope)
        self.ssheet = gspread.authorize(credentials).open_by_key(config["gspread_key"])

    def send(self, sheet_name, row, column, info):
        sheet = self.ssheet.worksheet(sheet_name)
        for col in range(len(info)):
            for r in range(min(3, len(info[col]))):
                sheet.update_cell(row + r, column + col, info[col][r])
