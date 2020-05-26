# Most of the code is from
# https://developers.google.com/sheets/api/quickstart/python?authuser=3


import pandas as pd
import pickle
import os.path
import io

from image import load_image
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow

def load_profile_sheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    # If modifying these scopes, delete the file token.pickle.
    SCOPES =  ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    # The ID and range of a sample spreadsheet.
    # https://docs.google.com/spreadsheets/d/1BXJIRv7EUZGb2EgSIueUz7Cv2fFjvdmRGoUxPrt8-Jc/edit?usp=sharing
    SAMPLE_SPREADSHEET_ID = '1BXJIRv7EUZGb2EgSIueUz7Cv2fFjvdmRGoUxPrt8-Jc'
    SAMPLE_RANGE_NAME = 'A:R'
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
        df = pd.DataFrame(values[1:], columns=values[0])
        tsl = list(df['Timestamp'])
        nameL = list(df["Name"])
        imgL = list(df['Image'])
        i = 0
        while i < len(imgL):
            imgL[i] = imgL[i][imgL[i].find("?id=")+4:]
            i+=1
        
        i = 0
        while i < len(tsl):
            load_image(imgL[i], nameL[i], tsl[i])
            i+=1
        
        return df


if __name__ == '__main__':
    df = load_profile_sheet()
    for i in df:
        print(df[i])
    print(df)