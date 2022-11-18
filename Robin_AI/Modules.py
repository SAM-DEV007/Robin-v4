import speech_recognition as speech
import pyttsx3
import datetime
from googlesearch import search
import webbrowser
import requests
from Responses_Keys import *
import Commands
import GUI_Creator
import os
import traceback

api_key_city = keys["api_key_city"]
api_key = keys["api_city"]
url_weather = keys["url_weather"]

listener = speech.Recognizer()
replier = pyttsx3.init()
rate = replier.getProperty('rate')
replier.setProperty('rate', 150)


def time_day(i):
    _hour = datetime.datetime.now().hour

    if i == "Intro":
        if 5 < _hour < 12:
            greetings = "Good Morning!"
        elif 12 <= _hour < 18:
            greetings = "Good Afternoon!"
        else:
            greetings = "Good Evening!"

        return greetings

    elif i == "Outro":
        if _hour >= 18 or _hour < 5:
            greetings = "Good Night!"
        else:
            greetings = "Have a good day!"

        return greetings


def intro():
    greet = time_day("Intro")
    name = GUI_Creator.a_user

    GUI_Creator.Rob.set(greet + " Robin is online!")
    replier.say(name + "" + greet + " Robin is online!")
    replier.runAndWait()


def weather_city_finder(city):
    complete_url_weather_city = url_weather + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url_weather_city)

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temp = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]

        weather_desc = z[0]["description"]

        temp_celsius = (current_temp - 273.15)
        temp_celsius = "{:.2f}".format(temp_celsius)

        # Converting them to strings
        temperature = str(temp_celsius)
        humidity = str(current_humidity)
        weather = str(weather_desc)

        return True, temperature, humidity, weather

    else:
        return False, None, None, None


def weather_finder():
    my_ip_url = "https://ip.42.pl/raw"
    response_ip = requests.get(my_ip_url)

    my_ip = response_ip.text

    city_finder_url = "http://api.ipstack.com/" + my_ip + "?access_key=" + api_key_city
    res = requests.get(city_finder_url)

    a = res.json()

    city_name = a["city"]

    complete_url_weather = url_weather + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url_weather)

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temp = y["temp"]
        current_humidity = y["humidity"]
        z = x["weather"]

        weather_desc = z[0]["description"]

        temp_celsius = (current_temp - 273.15)
        temp_celsius = "{:.2f}".format(temp_celsius)

        # Converting them to strings
        temperature = str(temp_celsius)
        humidity = str(current_humidity)
        weather = str(weather_desc)

        return True, temperature, humidity, weather

    else:
        return False, None, None, None


def speak(text):
    replier.say(text)
    replier.runAndWait()


def search_g(text):
    query = text.strip()

    for _ in search(query, num_results=1):
        webbrowser.open("https://www.google.com/search?q=%s" % query)


def open_website(text):
    web = text.strip()

    webbrowser.open("https://" + web + ".com")


def close():
    os.system('taskkill /im chrome.exe /f')


def search_yt(text):
    query = text.strip()

    for _ in search(query, num_results=1):
        webbrowser.open("https://youtube.com/search?q=%s" % query)


def take_cmd():
    cmd = ""

    try:
        with speech.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold = False
            voice = listener.listen(source, timeout=5.0)
    except ValueError:
        pass
    except speech.WaitTimeoutError:
        voice = ""
    except:
        z = traceback.format_exc()
        GUI_Creator.fatal(0, True, z, "Error", True)

    try:
        cmd = listener.recognize_google(voice)
        cmd = cmd.lower()
    except speech.RequestError:
        x = traceback.format_exc()
        GUI_Creator.fatal(..., True, x, "Warn")
        GUI_Creator.Rob.set("ROBIN'S API UNAVAILABLE!")
    except speech.UnknownValueError:
        Commands.Unable = True
    except AssertionError:
        z = traceback.format_exc()
        GUI_Creator.fatal(0, True, z, "Warn")
    except:
        y = traceback.format_exc()
        GUI_Creator.fatal(0, True, y, "Error", True)

    if cmd is not None:
        return cmd
