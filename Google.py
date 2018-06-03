# -*- coding: utf-8 -*-
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class Sheet():
    def __init__(self, scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'):
        # Setup the Sheets API
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', scopes)
            creds = tools.run_flow(flow, store)
        self.service = build('sheets', 'v4', http=creds.authorize(Http()))
        self.sheets = {}

    def open(self, name, sheet_ID):
        self.sheets[name] = sheet_ID

    def close(self, name):
        if name in self.sheets:
            del self.sheets[name]

    def read(self, name, range):
        if not name in self.sheets:
            return []
        result = self.service.spreadsheets().values().get(spreadsheetId=self.sheets[name], range=range).execute()
        return result.get('values', [])

    def write(self, name, range, values):
        if not name in self.sheets:
            return
        result = self.service.spreadsheets().values().update(spreadsheetId=self.sheets[name], range=range, valueInputOption='USER_ENTERED', body={'values': values}).execute()