import caldav
from caldav.elements import dav, cdav

def fetch_events(calendar_url, username, password):
    client = caldav.DAVClient(calendar_url, username=username, password=password)
    principal = client.principal()
    calendars = principal.calendars()
    events = []
    for calendar in calendars:
        events.extend(calendar.events())
    return events
