"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is calling up an API to add/delete ceratin event.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""

from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class CalendarEvent():
    """This class is calling an API from google to add/delete a specific action on Google calendar, by connecting the token and matched credential.json
    The API will add an event with its starting date ,ending date and event description.It will also delete an event by matching the primary key accordingly.

    This is supporting that user can make mutiple events with the one uniuqe userID
    """

    def addEvent(self, book):
        SCOPES = "https://www.googleapis.com/auth/calendar"  # : the api address
        store = file.Storage("token.json")
        creds = store.get()
        if(not creds or creds.invalid):
            #: get the unique tied credentials from the Google login of the user.
            flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        service = build("calendar", "v3", http=creds.authorize(
            Http()))  # : sending request

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
        return event["id"]

    def deleteEvent(self, ID):
        """delete the event by matching the primary key ID
        """
        SCOPES = "https://www.googleapis.com/auth/calendar"
        store = file.Storage("token.json")
        creds = store.get()
        if(not creds or creds.invalid):  # : find and match the credential file
            flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        service = build("calendar", "v3", http=creds.authorize(Http()))
        event = service.events().delete(calendarId='primary', eventId=ID).execute()


if __name__ == "__main__":
    CalendarEvent()
