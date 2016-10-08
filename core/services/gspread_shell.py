import json
from gspread import Client as Client

class GShell:
    def __init__(self):
        self.ssheet = None

    def get_from_config(self, config):
        f = open("FreeCashDesk.json", 'r')
        client = Client(json.loads(f.read()))
        f.close()
        client.login()
        self.ssheet = client.open_by_key(config["gspread_key"])

    def send(self, sheet_name, row, column, info):
        sheet = self.ssheet.worksheet(sheet_name)
        for col in range(len(info)):
            for r in range(min(3, len(col))):
                sheet.update_cell(row + r, column + col, info[col][r])
