import smtplib
import requests
import datetime
import time

MY_LAT: int = 42.179560
MY_LONG: float = -87.930440
FLAG_FOR_UNIX_TIME = 0


def is_ISS_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    response.raise_for_status()

    data = response.json()

    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']

    iss_position: tuple = (longitude, latitude)
    my_position: tuple = (MY_LAT, MY_LONG)

    if latitude - 5 <= MY_LAT <=  latitude + 5 and longitude - 5 <= MY_LONG <= longitude + 5:
      return True

def is_night():
    parameters: dict = {
      "lat": MY_LAT,
      "lng": MY_LONG,
      "time": FLAG_FOR_UNIX_TIME
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json")
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
      return True

while True:
    time.sleep(120)
    if is_ISS_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky!"
        )
