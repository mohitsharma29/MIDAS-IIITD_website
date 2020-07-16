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

# If modifying these scopes, delete the file token.pickle.
SCOPES =  ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# The ID and range of a sample spreadsheet.
# https://docs.google.com/spreadsheets/d/1BXJIRv7EUZGb2EgSIueUz7Cv2fFjvdmRGoUxPrt8-Jc/edit?usp=sharing
SAMPLE_SPREADSHEET_ID = '1VlX9JdKqatkIG7zuEMh_rNo-cTVetY10OFhNfOXum8k'
SAMPLE_RANGE_NAME = 'A:G'

def load_news_sheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
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
        nameL = list(df["Title"])
        imgL = list(df['Poster/Photograph (if any)'])
        i = 0
        """
        while i < len(imgL):
            imgL[i] = imgL[i][imgL[i].find("?id=")+4:]
            i+=1
        
        i = 0
        while i < len(tsl):
            load_image(imgL[i], nameL[i], tsl[i], img_path='assets/images/news/')
            i+=1
        """
        return df

def dftomd(df):
    # mdt = ['','position', 'type', 'organization','nickname','handle','email','profile_link','twitter','facebook','insta','github','scholar','image','cv','alum']
    i = 0
    files = []
    while i < len(df):
        s = ""
        s = s + "---\nlayout: news\ntitle: "
        k = 0

        s+='"'+df.iloc[i]['Title']+'"\nauthor: '
        s+='"'+df.iloc[i]['Author']+'"\nauthor_handle: '
        s+='"'+df.iloc[i]['Author_handle']+'"\nimage: '
        s = s + "/assets/images/news/" + df.iloc[i]['Timestamp'].replace("/","").replace(" ","").replace(":","")+".jpg\ncategory: news\ntags: "
        s+=df.iloc[i]['Tags']+'\n---\n'
        s+= df.iloc[i]['Content']+'\n\n'
        print(df.iloc[i]['Timestamp'].split(' '))
        temp = df.iloc[i]['Timestamp'].split(' ')[0].split('/')
        with open('../../news/_posts/' + temp[2] + '-' + temp[0] + '-' + temp[1] + '-' + df.iloc[i]['Title'] + '.md', 'w') as f:
            f.write(s)
        i+=1

if __name__ == '__main__':
    df = load_news_sheet()
    #print(df)
    # print(df.columns)
    s = dftomd(df)
    #print(s)
