#!/usr/bin/python3
# Most of the code is from
# https://developers.google.com/sheets/api/quickstart/python?authuser=3
from __future__ import print_function
import pickle
import os.path
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def load_sheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # If modifying these scopes, delete the file token.pickle.
    SCOPES =  ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1sd1YdDc-pQRNUozYou1mF-sfAQHBiLIRlswofURZuRU'
    SAMPLE_RANGE_NAME = 'A:L'
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        # print('Name, Major:')
        # for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            # for c in row:
                # print(c, end=' #|# ')
            # print("\n")
        # print(type(values))
        df = pd.DataFrame(values[1:], columns=values[0])
        # print(df)
        return df


if __name__ == '__main__':
    df = load_sheet()
    print(df)