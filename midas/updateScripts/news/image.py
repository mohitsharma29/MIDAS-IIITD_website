import pickle
import os.path
import io
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def load_image(file_id, name, tstamp):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
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

    service = build('drive', 'v3', credentials=creds)

    # https://developers.google.com/drive/api/v3/manage-downloads#download_a_file_stored_on_google_drive
    request = service.files().get_media(fileId=file_id)
    
    # https://stackoverflow.com/questions/36173356/google-drive-api-download-files-python-no-files-downloaded
    #tstamp = "images/"+tstamp.replace("/","").replace(" ","").replace(":","")+".jpg"
    tstamp = "../../MIDAS-IIITD_website/assets/images/team/"+tstamp.replace("/","").replace(" ","").replace(":","")+".jpg"
    fh = io.FileIO(tstamp,'wb')

    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Downloading "+name+"'s photo: %d%%." % int(status.progress() * 100))


if __name__ == '__main__':
    
    load_image("1_Og9soBbrk2S51Zrg_HnsaCPSFqFOQaO", "Ritwik", "2/27/2020 21:55:03")
