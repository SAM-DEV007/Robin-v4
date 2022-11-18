from Modules import *
from Responses_Keys import *
import datetime
import wikipedia
import random
import GUI_Creator

Active = False
Sleep = True
Unable = False
GUI = None
_commands = commands


def run_robin(com, command):
    if com != "":
        command = command.replace(com, "", 1)
    if "robin" in command:
        command = command.replace("robin", "", 1)

    robin_commands(command)


def robin_commands(cmd):
    global _commands, Active, Sleep

    if "robin" in cmd:
        cmd = cmd.replace("robin", "", 1)

    if not Active:
        for comm in _commands["hide"]:
            if comm in cmd:
                GUI_Creator.Rob.set("Hiding window")
                speak("Hiding window")
                GUI_Creator.root.withdraw()
                Active = True

    if not Active:
        for comm in _commands["unhide"]:
            if comm in cmd:
                GUI_Creator.Rob.set("Showing window")
                speak("Showing window")
                GUI_Creator.root.deiconify()
                Active = True

    if not Active:
        for comm in _commands["play_video"]:
            if comm in cmd:
                text = cmd.replace(comm, "", 1)
                text = text.strip()

                GUI_Creator.Rob.set("Opening youtube and searching " + text)
                speak("opening youtube and searching " + text)
                search_yt(text)
                Active = True

    if not Active:
        for comm in _commands["weather_and_city"]:
            if comm in cmd:
                _city = cmd.partition(comm)
                length = len(_city)
                city = _city[length - 1]
                city = city.strip()

                status, temp_city, hum_city, weather_city = weather_city_finder(city)

                if status:
                    GUI_Creator.Rob.set("Temp : " + temp_city + ". Humidity : " + hum_city + ". Weather : " +
                                        weather_city)
                    speak("temperature is " + temp_city + " degree celsius. Humidity is " + hum_city + "percent. "
                                                                                                       "Weather is "
                          + weather_city)
                    Active = True

                else:
                    GUI_Creator.Rob.set("Services Offline!")
                    speak("services offline")
                    Active = True


    if not Active:
        for comm in _commands["weather"]:
            if comm in cmd:
                status, temp_city, hum_city, weather_city = weather_finder()

                if status:
                    GUI_Creator.Rob.set("Temp : " + temp_city + ". Humidity : " + hum_city + ". Weather : " +
                                        weather_city)
                    speak("temperature is " + temp_city + " degree celsius. Humidity is " + hum_city + "percent. "
                                                                                                       "Weather is "
                          + weather_city)
                    Active = True

                else:
                    GUI_Creator.Rob.set("Services Offline!")
                    speak("services offline")
                    Active = True


    if not Active:
        for comm in _commands["time"]:
            if comm in cmd:
                temp_time = datetime.datetime.now().strftime("%I:%M %p")
                GUI_Creator.Rob.set("It's " + temp_time + " now")
                speak("It's " + temp_time + " now")
                Active = True

    if not Active:
        for comm in _commands["search_wiki"]:
            if comm in cmd:
                search_info = cmd.replace(comm, "", 1)
                info = wikipedia.summary(search_info, 3)

                GUI_Creator.Rob.set(info)
                speak(info)
                Active = True

    if not Active:
        for comm in _commands["google"]:
            if comm in cmd:
                search_google = cmd.replace(comm, "", 1)
                search_google = search_google.strip()

                GUI_Creator.Rob.set("Opening chrome and searching " + search_google)
                speak("opening chrome and searching " + search_google)
                search_g(search_google)
                Active = True

    if not Active:
        for comm in _commands["websites"]:
            if comm in cmd:
                website = cmd.replace(comm, "", 1)
                website = website.strip()

                GUI_Creator.Rob.set("Opening " + website)
                speak("opening " + website)
                open_website(website)
                Active = True

    if not Active:
        for comm in _commands["name"]:
            if comm in cmd:
                selection = random.choice(dictionary["hello_interaction"])
                GUI_Creator.Rob.set(selection)
                speak(selection)
                Active = True

    if not Active:
        for comm in _commands["owner"]:
            if comm in cmd:
                sel = random.choice(dictionary["creator_interaction"])
                GUI_Creator.Rob.set(sel)
                speak(sel)
                Active = True

    if not Active:
        for comm in _commands["well_being"]:
            if comm in cmd:
                s = random.choice(dictionary["how_are_you_interaction"])
                GUI_Creator.Rob.set(s)
                speak(s)
                Active = True

    if not Active:
        for comm in _commands["gratitude"]:
            if comm in cmd:
                select = random.choice(dictionary["thank_you_interaction"])
                GUI_Creator.Rob.set(select)
                speak(select)
                Active = True

    if not Active:
        for comm in _commands["hello"]:
            if comm in cmd:
                selected = random.choice(dictionary["hello_interaction"])
                GUI_Creator.Rob.set(selected)
                speak(selected)
                Active = True

    if not Active:
        for comm in _commands["my_name"]:
            if comm in cmd:
                GUI_Creator.Rob.set("Your name is " + GUI_Creator.a_user)
                speak("Your name is " + GUI_Creator.a_user)
                Active = True

    if not Active:
        for comm in _commands["close"]:
            if comm in cmd:
                GUI_Creator.Rob.set("Closing chrome instances")
                speak("Closing chrome instances")
                close()
                Active = True

    if not Active:
        for comm in _commands["shut_down"]:
            if comm in cmd:
                GUI_Creator.Rob.set("Robin going to sleep!")
                speak("Robin going to sleep")
                Active = True
                Sleep = True

    if not Active:
        for comm in _commands["quit"]:
            if comm in cmd:
                greet = time_day("Outro")
                GUI_Creator.Rob.set(greet + " Robin going offline!")
                Active = True
                speak(greet + " Robin going offline")
                GUI_Creator.exit_func()

    if not Active and not Unable:
        GUI_Creator.Rob.set("Unable to understand your command!")
        speak("unable to understand your command")
