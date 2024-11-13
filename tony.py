import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import wikipedia
import subprocess
import pyjokes
from time import sleep
import os
import random
import webbrowser
import geopy.distance
from geopy.geocoders import Nominatim
import psutil
import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import json
import socket
import time
import wolframalpha
import pyautogui
import cv2

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function for the AI to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function for the AI to listen for commands
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # remove background noise
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command)
        return command
    except:
        print("Sorry, I didn't catch that.")
        return ""

# Define a function to generate a random greeting
def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
    
# Define a function to generate a random date
def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)
    
# Define a function to generate a joke
def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    engine.say(joke)
    engine.runAndWait()
    
# Open chrome/website
def open_chrome():
    url = "https://www.google.co.in/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)

# Define a function to get the user's current location
def get_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("me")
    return (location.latitude, location.longitude)

# Define a function to retrieve information about a person from Wikipedia
def get_bio_of(name):
    try:
        page = wikipedia.page(name)
        return page.summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "Can you please be more specific about which " + name + " you are referring to?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information about " + name + "."
    
# Define a function to search for and open a specific YouTube video
def search_youtube(query):
    api_key = "your-google-api"
    query = urllib.parse.quote(query)
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&type=video&key={api_key}"
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    video_id = data["items"][0]["id"]["videoId"]
    webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
    speak("Opening YouTube video.")

# Define a function to google search
def search_google(query):
    api_key = "your-google-api"
    cx = "your-csx"
    query = urllib.parse.quote(query)
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    search_results = data.get("items", [])
    if search_results:
        first_result = search_results[0]
        webbrowser.open(first_result["link"])
        speak("Here is what I found on Google.")
    else:
        speak("Sorry, I couldn't find anything on Google for that.")
        
def get_ip_address():
    """
    Returns the IP address of the computer.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address
# Get the IP address
ip_address = get_ip_address()

# Define a function to switch window
def switch_window(command):
    """
    Switch to the window specified in the command.
    """
    if "switch to" in command:
        window_name = command.replace("switch to", "").strip()
        if window_name:
            try:
                pyautogui.getWindowsWithTitle(window_name)[0].activate()
                return f"Switched to {window_name} window."
            except:
                return f"Could not find a window named {window_name}."
        else:
            return "Please specify a window name."
    else:
        return None
    
# Set up News API key and endpoint
api_key = "your-news-api"
news_endpoint = "https://newsapi.org/v2/top-headlines"

def get_international_news():
    """
    Fetch and read out the top international news headlines from News API.
    """
    # Define API request parameters
    params = {
        "country": "us",
        "category": "general",
        "pageSize": 5,
        "apiKey": api_key
    }

    # Send API request and parse response
    response = requests.get(news_endpoint, params=params)
    news_data = json.loads(response.text)

    # Extract and read out news headlines
    headlines = [article["title"] for article in news_data["articles"]]
    for headline in headlines:
        engine.say(headline)
        engine.runAndWait()
        
# Define a function to report weather        
def get_weather_report(city):
    """
    Retrieve the weather report for a given city using OpenWeatherMap API.
    """
    api_key = "your-open-weather-api"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        temperature_celsius = round(temperature - 273.15, 2)
        return f"The current weather in {city_name} is {weather} with a temperature of {temperature_celsius}°C."
    else:
        return f"Sorry, could not find weather information for {city_name}."
    
# replace YOUR_API_KEY with your actual API key
api_key = 'your-news-api'

def get_ipl_scores():
    url = f"https://newsapi.org/v2/everything?q=ipl%20scores&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        if articles:
            score_text = ""
            for article in articles:
                title = article['title']
                description = article['description']
                score_text += f"{title}: {description}\n"
            return score_text
        else:
            return "Sorry, I could not find any IPL scores at the moment."
    else:
        return "Sorry, I could not retrieve the latest scores at the moment."
    
def get_ipl_news():
    url = f"https://newsapi.org/v2/everything?q=ipl%20news&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        if articles:
            news_text = ""
            for article in articles:
                title = article['title']
                description = article['description']
                news_text += f"{title}: {description}\n"
            return news_text
        else:
            return "Sorry, I could not find any IPL news at the moment."
    else:
        return "Sorry, I could not retrieve the latest news at the moment."
    
def take_photo():
    # initialize camera
    cam = cv2.VideoCapture(0)

    # read from camera
    ret, image = cam.read()
    
    # generate unique file name
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    img_name = f"photo_{timestamp}.jpg"
    
    # save image
    cv2.imwrite(img_name, image)

    # release camera
    cam.release()
    
    # read and display captured image for 5 seconds
    cv2.imshow("Captured Photo", image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    
def get_historical_events(query):
    api_key = "your-loc-government-api"
    base_url = "https://www.loc.gov"
    search_url = base_url + "/search/?q={}&fo=json".format(query)
    response = requests.get(search_url, headers={"Authorization": api_key})
    if response.status_code == requests.codes.ok:
        data = response.json()
        results = data["results"]
        if results:
            for result in results:
                if "description" in result:
                    speak(result["description"])
                else:
                    speak("Sorry, I couldn't find any description for this item.")
        else:
            speak("Sorry, I couldn't find any historical events related to your query.")
    else:
        speak("Sorry, there was an error with your request.")

def get_historical_info(query):
    api_key = 'your-google-api'
    api_endpoint = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
        'types': 'HistoricalEvent,Person,Organization,Place'
    }
    response = requests.get(api_endpoint, params=params)
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        if 'itemListElement' in data and len(data['itemListElement']) > 0:
            result = data['itemListElement'][0]['result']
            if 'detailedDescription' in result:
                description = result['detailedDescription']['articleBody']
                speak(description)
            else:
                speak("Sorry, I couldn't find any information on that.")
        else:
            speak("Sorry, I couldn't find any information on that.")
    else:
        speak("Sorry, there was an error processing your request.")
        
# Set Wolfram|Alpha API key
app_id = "your-wolf-frame-api"
client = wolframalpha.Client(app_id)

# Define a function to get the answer to a scientific, engineering, or mathematical question
def get_wolframalpha_answer(query):
    # Send the query to the Wolfram|Alpha API
    res = client.query(query)

    # Extract the answer from the response
    try:
        answer = next(res.results).text
        return answer
    except StopIteration:
        # No answer found
        return "Sorry, I could not find an answer to your question."
    
# Define a function to extract information about a movie from the OMDB API
def get_movie_info(title):
    url = f"http://www.omdbapi.com/?apikey=your-omdb-api
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data['Response'] == 'True':
            info = f"{data['Title']} ({data['Year']})\n" \
                   f"Plot: {data['Plot']}\n" \
                   f"Starring: {data['Actors']}\n" \
                   f"IMDb Rating: {data['imdbRating']}"
            return info
        else:
            return "Sorry, I could not find information about that movie"
    else:
        return "Sorry, there was an error retrieving information from the OMDB API"


# Define a function to get a list of movie recommendations from Wikipedia
def get_movie_recommendations(topic):
    try:
        page = wikipedia.page(topic)
        recommendations = wikipedia.get_section(page.title, "2").split('\n')
        recommendations = [r.strip() for r in recommendations if r.strip() != '']
        if len(recommendations) > 0:
            return recommendations
        else:
            return "Sorry, I could not find any movie recommendations for that topic"
    except wikipedia.exceptions.PageError:
        return "Sorry, I could not find a Wikipedia page for that topic"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Sorry, there are multiple pages for that topic: {e.options}"
    
# Define the base URL for the Restcountries API
BASE_URL = "https://restcountries.com/v2/"

# Define a function to get information on all countries
def get_all_countries():
    # Send a request to the API
    response = requests.get(BASE_URL + "all")
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
        # Extract the name and population of each country
        countries = [(country['name'], country['population']) for country in data]
        # Return the list of countries
        return countries
    else:
        # Return an error message if the request failed
        return "Sorry, there was an error retrieving information from the Restcountries API"

def get_country_info(name):
    url = f"https://restcountries.com/v2/name/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data:
            data = data[0]  # Access the first item in the list
            currencies = ", ".join([currency["name"] for currency in data["currencies"]])
            languages = ", ".join([language["name"] for language in data["languages"]])
            subregions = ", ".join(data["subregion"])
            info = f"Name: {data['name']}\n" \
                   f"Capital: {data['capital']}\n" \
                   f"Region: {data['region']}\n" \
                   f"Population: {data['population']}\n" \
                   f"Currencies: {currencies}\n" \
                   f"Languages: {languages}\n" \
                   f"Calling Codes: {', '.join(data['callingCodes'])}\n" \
                   f"Demonym: {data['demonym']}"
            return info
        else:
            return "Sorry, I could not find information about that country"
    else:
        return "Sorry, there was an error retrieving information from the REST Countries API"

# Define a function to fetch search results
def fetch_search_results(query):
    serpapi_key = "your-serpapi-key"
    params = {
        "engine": "google",
        "q": query,
        "api_key": serpapi_key
    }

    # Create a GoogleSearch instance with the provided parameters
    search = GoogleSearch(params)

    # Fetch and process search results
    results = search.get_dict()
    organic_results = results["organic_results"]

    # Respond based on the search result
    if organic_results:
        first_result = organic_results[0]
        title = first_result.get("title", "N/A")
        snippet = first_result.get("snippet", "N/A")

        response = f"The top result is: {title}. Here's a snippet: {snippet}"
        print(response)
        speak(response)
    else:
        response = "I'm sorry, I couldn't find any results for your query."
        print(response)
        speak(response)
        
# Loop to continuously listen for and respond to commands
while True:
    command = listen()
    if "hello" in command:
        speak(greeting() + " How can I assist you?")
    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time + ".")
    elif "what date is it" in command:
        current_date = day = int(datetime.datetime.now().day)
        month = int(datetime.datetime.now().month)
        year = int(datetime.datetime.now().year)
        speak("The current date is")
        print(day, month, year)
        speak(day)
        speak(month)
        speak(year)
    elif "what is your name" in command:
        speak("my name is antony edward stark everyone call me tony i am created by mr.liyander")
    elif "tell about your creator" in command:
        speak("my creator is mr.liyander whenever he is free he will create new highly advance technology")
# open chrome
    elif "open chrome" in command:
         speak("Opening Google Chrome.")
         os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

# Chrome search
    elif "find" in command:
        speak("what should i search?")
        chromepath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"  # location
        query = listen()
        wb.get(chromepath).open_new_tab(query + ".com")
        
# Wikipedia search
    elif "wikipedia" in command:
        speak("Searching...")
        command = command.replace("wikipedia", "")
        result = wikipedia.summary(command, sentences=2)
        speak(result)
        print(result)

# Launch software
    elif "open notepad" in command:
        speak("opening notepad")
        location = "C:/WINDOWS/system32/notepad.exe"
        notepad = subprocess.Popen(location)

    elif "close notepad" in command:
        speak("closing notepad")
        notepad.terminate()
        
# Random jokes
    elif "tell me a joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)

# Logout/Shutdown/Restart
    elif "logout" in command:
         speak('logging out in 5 second')
         sleep(5)
         os.system("shutdown - l")

    elif "shutdown" in command:
         speak('shutting down in 5 second')
         sleep(5)
         os.system("shutdown /s /t 1")

    elif "restart" in command:
         speak('restarting in 5 second')
         sleep(5)
         os.system("shutdown /r /t 1")
         
    elif "open hidden menu" in command:
        speak('opening hidden menu')
        # Win+X: Open the hidden menu
        pyautogui.hotkey('winleft', 'x')

    elif "open task manager" in command:
        speak('opening task manager')
        # Ctrl+Shift+Esc: Open the Task Manager
        pyautogui.hotkey('ctrl', 'shift', 'esc')

    elif "open task view" in command:
        speak('opening task view')
        # Win+Tab: Open the Task view
        pyautogui.hotkey('winleft', 'tab')

    elif "take screenshot" in command:
        # win+perscr
        pyautogui.hotkey('winleft', 'prtscr')
        speak("done")

        # Take screenshot save in Given location
        '''        
    elif "take screenshot" in command:
        img = pyautogui.screenshot()
        img.save("D:/screenshot_1.png")  # file mane and location
        speak("Done")
        '''

    elif "open snip" in command:
        speak('opening snip')
        pyautogui.hotkey('winleft', 'shift', 's')

    elif "close this app" in command:
        speak('closing the app')
        # alt + f4: close this app
        pyautogui.hotkey('alt', 'f4')

    elif "open setting" in command:
        speak('opening settings')
        # win+i = open setting
        pyautogui.hotkey('winleft', 'i')

    elif "create new virtual desktop" in command:
        speak('creating new virtual desktop')
        # Win+Ctrl+D: Add a new virtual desktop
        pyautogui.hotkey('winleft', 'ctrl', 'd')
        
    elif "open youtube" in command:
        speak('opening youtube')
        webbrowser.open("https://www.youtube.com")
    
    elif "play music" in command:
        speak("Playing music.")
        music_dir = "C:\\Users\\Smile\\Music\\m"
        songs = os.listdir(music_dir)
        song = os.path.join(music_dir, random.choice(songs))
        os.startfile(song)
        
    elif "open video file" in command:
        speak("Playing video.") 
        video_dir = r"E:\s"
        videos = os.listdir(video_dir)
        video = os.path.join(video_dir, random.choice(videos))
        os.startfile(video)
        
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        
    elif "where is" in command:
        location = command.replace("where is", "")
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(location)
        if location:
            user_location = get_location()
            queried_location = (location.latitude, location.longitude)
            distance = geopy.distance.distance(user_location, queried_location).km
            speak(location.address + " is " + str(round(distance, 2)) + " kilometers away from you.")
            webbrowser.open("https://maps.googleapis.com/" + location.address)
        else:
            speak("Sorry, I couldn't find that location.")
            
    elif "what's my system status" in command:
        # Getting RAM usage
        svmem = psutil.virtual_memory()
        used_memory = str(round(svmem.used / (1024 * 1024), 2))
        
        # Getting CPU usage
        cpu_percent = psutil.cpu_percent()
        
        # Speaking out the system status
        speak(
              f"RAM usage is {used_memory} megabytes. "
              f"CPU usage is {cpu_percent} percent.")
        
    elif "bio of" in command:
        # Retrieve information from Wikipedia API and speak it
        name = command.split("person info ")[-1]
        info = get_bio_of(name)
        speak(info)
        
    elif "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        search_youtube(query)
        
    elif "play video on youtube" in command:
        speak("What video would you like to watch?")
        query = listen()
        search_youtube(query)
        
    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        search_google(query)
        
    elif "what is my ip address" in command:
         ip_address = get_ip_address()
         speak(f"Your IP address is {ip_address}")
         
# switch window
    elif "switch to" in command:
        result = switch_window(command)
        print(result)
        speak(result)
        
    elif "international news" in command:
        get_international_news()
        
    elif command.startswith("weather in"):
        city = command.replace("weather in", "").strip()
        weather_report = get_weather_report(city)
        if weather_report:
            speak(weather_report)
        else:
            speak("Sorry, I couldn't find weather information for that city.")
            
    elif "what are the latest sports" in command:
         sports_scores = get_sports_scores()
         if sports_scores:
             speak(sports_scores)
         else:
             speak("Sorry, I could not retrieve the latest sports scores at the moment.")
             
    elif "ipl score" in command:
        ipl_scores = get_ipl_scores()
        speak(ipl_scores)
        
    elif "ipl news" in command:
        ipl_news = get_ipl_news()
        speak(ipl_news)
        
    elif "take a photo" in command:
        take_photo()
        speak("Photo captured successfully.")
    elif "display photo" in command:
        display_photo()
        
    elif "library of congress" in command:
        query = command.replace("library of congress", "")
        results = get_historical_events(query)
        
    elif "history of" in command:
        speak("Please wait while I search for historical events.")
        query = command.replace("history of","")
        get_historical_info(query)
        
    # Get the Wolfram|Alpha answer
    elif "what is" in command or "tell about" in command:
        speak("Please wait while I search for an answer.")
        answer = get_wolframalpha_answer(command)
        speak(answer)
        
    elif "movie" in command:
        title = command.split('movie ')[-1].split(' ')[0]
        title = get_movie_info(title)
        speak("Here's what I found:")
        speak(title)
   
    elif "get recommendation on" in command:
        topic = command.split('get recommendations on ')[-1].split(' ')[0]
        topic = get_movie_recommendations(topic)
        speak("Here's what I found:")
        speak(topic)
        
    elif "all countries" in command:
        query = get_all_countries()
        speak(query)
        
    elif "country" in command:
        name = command.split('country')[-1].strip()
        name = get_country_info(name)
        speak("Here's what I found:")
        speak(name)
        
    elif "result for" in command:
        speak("Please wait while I search.")
        query = command.replace("result for", "").strip()
        fetch_search_results(query)
        
    elif "goodbye" in command:
        speak("Goodbye! see you next time")
        break
