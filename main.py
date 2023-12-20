import control
import sys
from datetime import date, datetime
import configparser

print(str(sys.argv))

cfg = sys.argv[1]
arrival = sys.argv[2]
departure = sys.argv[3] #d-m-yyyy

a = arrival.split('-')
d = departure.split('-')

#date is in d-m-yyyy format
config = configparser.RawConfigParser()
config.read( f'config/{cfg}.cfg')

user =dict(config.items('INFO'))
print(user)
dob = user['dob'].split('-')
e = user['passport_expiry'].split('-')

#personal info
name=user['name']
dob=date(int(dob[2]), int(dob[1]), int(dob[0]))
passport_number=user['passport_number']
passport_expiry=date(int(e[2]), int(e[1]), int(e[0]))
nationality=user['nationality']
sex=user['sex']
email=user['email']
country_code=user['country_code']
mobile=user['mobile']

#travel info
arrival_date=date(int(a[2]), int(a[1]), int(a[0]))
departure_date=date(int(d[2]), int(d[1]), int(d[0]))
mode=user['mode']
last_embarkation=user['last_embarkation']


url = "https://imigresen-online.imi.gov.my/mdac/main?registerMain"
validation_url = 'https://imigresen-online.imi.gov.my/mdac/egate'

def fillMdac():
    control.openChrome(url)
    control.sleepForMs(4000)

    control.moveMouseToName()
    control.delayTrigger(control.leftClick)
    control.triggerPaste(name)
    control.delayTrigger(control.triggerTab)
    control.triggerPaste(passport_number)
    control.triggerTab()

    control.moveMouseToDOB()
    control.delayTrigger(control.leftClick)
    control.calendarWidgetSetDate(dob)
    control.triggerTab()
    #nationality
    control.triggerTab()
    #sex
    control.delayTrigger(control.triggerEnter)
    control.delayTrigger(control.triggerKey, sex)
    control.delayTrigger(control.triggerEnter)
    control.delayTrigger(control.triggerTab)
    control.sleepForMs(500)

    #pp expiry
    control.calendarWidgetSetDate(passport_expiry)

    control.delayTrigger(control.triggerTab)
    control.triggerPaste(email)
    control.delayTrigger(control.triggerTab)
    control.triggerkeyIn(email)
    control.delayTrigger(control.triggerTab)
    control.triggerPaste(country_code)
    control.delayTrigger(control.triggerTab)
    control.triggerPaste(country_code)
    control.delayTrigger(control.triggerTab)

    #mobile
    control.triggerPaste(mobile)
    control.delayTrigger(control.triggerTab)
    control.triggerPaste(mobile)

    control.scroll(-1000)

    #Travel info
    control.delayTrigger(control.triggerTab)
    control.delayTrigger(control.triggerTab)
    control.calendarWidgetSetDate(arrival_date)
    control.triggerTab()
    control.calendarWidgetSetDate(departure_date)
    control.triggerTab()
    control.delayTrigger(control.triggerEnter)
    control.delayTrigger(control.triggerKey, mode)
    control.delayTrigger(control.triggerEnter)

    control.triggerTab()
    control.triggerTab()
    #accom stay
    control.delayTrigger(control.triggerEnter)
    control.delayTrigger(control.triggerKey, "o")
    control.triggerEnter()
    control.triggerTab()
    #give default address
    control.triggerPaste("106 - 108, Jalan Wong Ah Fook,  80000 Johor Bahru, Johor")
    control.triggerTab()
    control.triggerTab()
    #State
    control.delayTrigger(control.triggerKey, "j")
    control.triggerTab()
    #postcode
    control.triggerPaste("80000")
    control.triggerTab()
    #city
    control.delayTrigger(control.triggerKey, "j")
    control.triggerTab()

    #submit
    control.triggerEnter()


    control.sleepForMs(3000)
#===============================================
#validation
#===============================================
def validateSubmission():
    control.openChrome(validation_url)
    control.sleepForMs(4000)

    #category
    control.moveMouse(848, 724)
    control.delayTrigger(control.leftClick)
    control.delayTrigger(control.triggerKey, "s")
    control.delayTrigger(control.triggerTab)
    control.triggerTab()

    #pp num
    control.triggerPaste(passport_number)
    control.triggerTab()

    #nationality
    control.triggerkeyIn('si')
    control.delayTrigger(control.triggerTab)

    #date of arrival
    control.moveMouse(801, 857)
    control.delayTrigger(control.leftClick)
    control.calendarWidgetSetDate(arrival_date)
    #captcha
    control.moveMouse(787, 929)
    control.delayTrigger(control.leftClick)
    control.sleepForMs(800)
    #submit
    control.moveMouse(908, 1018)
    control.delayTrigger(control.leftClick)

    control.sleepForMs(2000)
    control.scroll(-1000)

#===============================================
#Actual FLow
#===============================================
fillMdac()
validateSubmission()
