import email
import smtplib
from datetime import datetime, timedelta

import requests
import vlc
import time


def create_session_info(center, session):
    return {"name": center["name"],
            "date": session["date"],
            "capacity": session["available_capacity"],
            "vaccine": session["vaccine"],
            "pincodes": center["pincode"],
            "age_limit": session["min_age_limit"]}


def get_sessions(data):
    for center in data["centers"]:
        for session in center["sessions"]:
            yield create_session_info(center, session)


def is_available(session):
    return session["capacity"] > 0


def is_eighteen_plus(session):
    return session["age_limit"] == 18


def get_for_seven_days(start_date):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
    params = {"district_id": 697, "date": start_date.strftime("%d-%m-%Y")}
    # url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
    # params = {"pincode": 248171, "date": start_date.strftime("%d-%m-%Y")}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    resp = requests.get(url, params=params, headers=headers)
    data = resp.json()
    return [session for session in get_sessions(data) if is_eighteen_plus(session) and is_available(session)]


def create_output(session_info):
    return f"{session_info['name']} ({session_info['capacity']})  -  {session_info['pincodes']}"


def main_func():
    new_date = datetime.today() + timedelta(1)
    # print(new_date)
    print(get_for_seven_days(new_date))
    content = "\n".join([create_output(session_info) for session_info in get_for_seven_days(new_date)])
    username = "surajkumar5454@gmail.com"
    password = "Usualgmail@5421"

    if not content:
        print("No availability")

    else:
        print(content)
        base_url = 'https://api.telegram.org/bot1796740053:AAG61ntffQnu9rV_qtoD5wWeA7poXJ2f8bk/sendMessage?chat_id=-578120624&text="{}"'.format(content)
        requests.get(base_url)
        asa_plays = vlc.MediaPlayer("play_file.mp3")
        asa_plays.play()
        time.sleep(40)
        email_msg = email.message.EmailMessage()
        email_msg["Subject"] = "Vaccination Slot Open"
        email_msg["From"] = username
        email_msg["To"] = "surajkumar.geu@gmail.com"
        email_msg.set_content(content)

        with smtplib.SMTP(host='smtp.gmail.com', port='587') as server:
            server.starttls()
            server.login(username, password)
            server.send_message(email_msg, username, "surajkumar.geu@gmail.com")


# schedule.every(9).seconds.do(main_func)

while 1:
    main_func()
    #    schedule.run_pending()
    time.sleep(5)