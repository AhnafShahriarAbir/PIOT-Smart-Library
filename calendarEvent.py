
from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class CreateEvent():

    def addEvent(self, book):
        SCOPES = "https://www.googleapis.com/auth/calendar"
        store = file.Storage("token.json")
        creds = store.get()
        if(not creds or creds.invalid):
            flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        service = build("calendar", "v3", http=creds.authorize(Http()))
        date = datetime.now()
        returnDate = (date + timedelta(days=7)).strftime("%Y-%m-%d")
        time_start = "{}T12:00:00+10:00".format(returnDate)
        time_end = "{}T12:00:00+10:00".format(returnDate)
        event = {
            "summary": "Return Book: " + book,
            "description": "Event to Return Borrowed Book",
            "start": {
                "dateTime": time_start,
                "timeZone": "Australia/Melbourne",
            },
            "end": {
                "dateTime": time_end,
                "timeZone": "Australia/Melbourne",
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "email", "minutes": 5},
                    {"method": "popup", "minutes": 10},
                ],
            }
        }

        event = service.events().insert(calendarId="primary", body=event).execute()
        print("Event created: {}".format(event.get("htmlLink")))
