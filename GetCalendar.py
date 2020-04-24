from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_events(num_of_events):
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

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=num_of_events, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    s = ''
    if not events:
        s += 'No upcoming events found.'
    for event in events:
        rawEvent = event['start'].get('dateTime', event['start'].get('date'))
        
        dateSplit = rawEvent.split('-', 3)
        dateSplit[2] = dateSplit[2][0:2]
        date = dateSplit[0] + "/" + dateSplit[1] + "/" + dateSplit[2]
        day = datetime.date(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2])).strftime('%A')
                
        s += str(date) + ' ' + str(day) + ' ' + event['summary']
    return s
