from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import requests
from bs4 import BeautifulSoup

url ="https://www.muslimpro.com/en/prayer-times"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

for x in soup.findAll('tr', {'class':'active'}):
    data = x.text
    date = data[0:10]
    fajr = data[10:15]
    fajr = fajr.replace(":","")
    sunrise = data[15:20]
    sunrise = sunrise.replace(":","")
    dhuhr = data[20:25]
    dhuhr = dhuhr.replace(":","")
    asr = data[25:30]
    asr = asr.replace(":","")
    maghrib = data[30:35]
    maghrib = maghrib.replace(":","")
    isha = data[35:40]
    isha = isha.replace(":","")
    print(date)

def main_fajr():
   # creates event for prayer times in same day.
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, int(fajr[0:2]), int(fajr[2:4]))+timedelta(days=0)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=0)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Fajr',
           "description": '',
           "start": {"dateTime": start, "timeZone": 'Europe/Dublin'},
           "end": {"dateTime": end, "timeZone": 'Europe/Dublin'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

def main_sunrise():
   # creates event for prayer times in same day.
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, int(sunrise[0:2]), int(sunrise[2:4]))+timedelta(days=0)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=0)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Sunrise',
           "description": '',
           "start": {"dateTime": start, "timeZone": 'Europe/Dublin'},
           "end": {"dateTime": end, "timeZone": 'Europe/Dublin'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

def main_dhuhr():
   # creates event for prayer times in same day.
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, int(dhuhr[0:2]), int(dhuhr[2:4]))+timedelta(days=0)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=0)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Dhuhr',
           "description": '',
           "start": {"dateTime": start, "timeZone": 'Europe/Dublin'},
           "end": {"dateTime": end, "timeZone": 'Europe/Dublin'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

def main_asr():
   # creates event for prayer times in same day.
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, int(asr[0:2]), int(asr[2:4]))+timedelta(days=0)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=0)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Asr',
           "description": '',
           "start": {"dateTime": start, "timeZone": 'Europe/Dublin'},
           "end": {"dateTime": end, "timeZone": 'Europe/Dublin'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

def main_maghrib():
   # creates event for prayer times in same day.
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, int(maghrib[0:2]), int(maghrib[2:4]))+timedelta(days=0)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=0)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Maghrib',
           "description": '',
           "start": {"dateTime": start, "timeZone": 'Europe/Dublin'},
           "end": {"dateTime": end, "timeZone": 'Europe/Dublin'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

def main_isha():
   # creates event for prayer times in same day.
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, int(isha[0:2]), int(isha[2:4]))+timedelta(days=0)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=0)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Isha',
           "description": '',
           "start": {"dateTime": start, "timeZone": 'Europe/Dublin'},
           "end": {"dateTime": end, "timeZone": 'Europe/Dublin'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   main_fajr()

if __name__ == '__main__':
    main_sunrise()

if __name__ == '__main__':
    main_dhuhr()

if __name__ == '__main__':
    main_asr()

if __name__ == '__main__':
    main_maghrib()

if __name__ == '__main__':
   main_isha()

print("Prayer time done for the day")