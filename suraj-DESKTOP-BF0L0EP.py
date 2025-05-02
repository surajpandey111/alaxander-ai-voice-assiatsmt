import pyttsx3
import speech_recognition as sr
import wikipedia
import wikipediaapi
import webbrowser
import wolframalpha
import os
from io import BytesIO
import re
from IPython.display import Markdown
import textwrap
import smtplib
import random
import requests
#import datetime
from datetime import datetime
from selenium import webdriver
import time
#rom serpapi import GoogleSearch
import pathlib
import PIL.Image
from bs4 import BeautifulSoup
import google.generativeai as genai
import google.generativeai as palm


image_dir = "C:\\Users\\SURAJ PANDEY\\Videos\\image"
palm.configure(api_key="gshtyiyto9iu")
genafvasefi.configure(api_key="hggsruryuuyou9iop0o")


def to_markdown(text):
    text = text.replace(".", " *")
    return Markdown(textwrap.indent(text, ">", predicate=lambda _: True))

#gemini-pro
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def run_conversation():
    global chat
    speak("ya WELCOME IN GRAND CHATING CONVERSATION WORLD")
    while True:
        user_input = takeCommand()
        if "retry" in user_input.lower():
            continue
        if "exit" in user_input.lower():
            break
        user_response = chat.send_message(user_input)
        model_response = user_response.text
        print(f"Model:{user_response.text}")
        speak(model_response)
        chat.history.append({"role": "user", "parts": [user_input]})
        chat.history.append({"role": "model", "parts": [user_response.text]})


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    #hour = int(datetime.datetime.now().hour)
    hour = int(datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning! SIR")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon SIR")
    elif hour >= 16 and hour < 22:
        speak("Good Evening SIR")
    else:
        speak("Good Night SIR")
    speak(
        "I am ALAXANDER maded A.I VOICE ASSISTANT by SURAJ kumar PANDEY SIR.please tell me how may I help you "
    )


def wishMe1():
    #hour = int(datetime.datetime.now().hour)
    hour = int(datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")
    elif hour >= 16 and hour < 22:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am GOING GOING GOING BYE BYE!! ")
    c = random.randint(0, 2)
    music1_dir = "C:\\Users\\SURAJ PANDEY\\Music\\byevid"
    song = os.listdir(music1_dir)

    print(song)
    os.startfile(os.path.join(music1_dir, song[c]))


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "retry"
    
    return query


user_agent = "ALAXANDER(worldforensic@gmail.com)"
language = "en"
wiki_wiki = wikipediaapi.Wikipedia(user_agent, language)


def get_summary(page_title):
    page = wiki_wiki.page(page_title)
    return page.summary


def check_page_exists(page_title):
    page = wiki_wiki.page(page_title)
    return page.exists()


def get_page_url(page_title):
    page = wiki_wiki.page(page_title)
    return page.fullurl
def get_apod(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return data
api_key = 'Fe0znWeGxezbMOen0GUJGu4sEdsV53cYdfBzcieP'

def process_query(query):
    if "nasa" in query.lower():
        try:
            apod_data = get_apod(api_key)
            print("Title:", apod_data['title'])
            print("Explanation:", apod_data['explanation'])
            print("Image URL:", apod_data['url'])
            speak(apod_data['title'])
            speak(apod_data['explanation'])
            webbrowser.open(apod_data['url'])
        except requests.exceptions.HTTPError as e:
            print("HTTP error occurred:", e)
            speak("An error occurred while fetching NASA data.")
        except Exception as e:
            print("An error occurred:", e)
            speak("An error occurred while fetching NASA data.")

   
def yt_search(yt_query):
    form_query=yt_query.replace(' ','+')
    yt_url=f'https://www.youtube.com/results?search_query={form_query}'
    webbrowser.open(yt_url)
    
def google_scholar(query):
    formatted_query=query.replace(' ','+')
    search_url=f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={formatted_query}&btnG='
    webbrowser.open(search_url)
    
def map_search(query):
    formatted_query=query.replace(' ','+')
    search_url=f'https://www.google.com/maps/search/{formatted_query}'
    webbrowser.open(search_url)    

def get_image_path(number):
    return os.path.join(image_dir, f"image_{number}.png")


def perform_image_detection(selected_number):
    image_path = get_image_path(selected_number)

    if os.path.exists(image_path):
        img = PIL.Image.open(image_path)
        model = genai.GenerativeModel("gemini-pro-vision")
        #model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(img)
        print(response.text)
        speak(response.text)
    else:
        print(f"Image not found for the selected number:{selected_number}")
        
def image_search(query):
    formatted_query =query.replace(' ','+')
    
    search_url=f'https://www.google.com/search?q={formatted_query}&tbm=isch&ved=2ahUKEwjEr77jvciDAxXnvmMGHbMQC90Q2-cCegQIABAA&oq={formatted_query}&gs_lcp=CgNpbWcQAzINCAAQgAQQigUQQxCxAzINCAAQgAQQigUQQxCxAzINCAAQgAQQigUQQxCxAzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzIKCAAQgAQQigUQQzoICAAQgAQQsQNQpQdY-Rdgxx5oAXAAeAGAAdACiAGTCZIBBzAuNS4wLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=1CGZZcT1Cef9juMPs6Gs6A0&bih=695&biw=1536&rlz=1C1VDKB_en-GBIN1077IN1077'
    webbrowser.open(search_url)
    image_links=scrape_image_links(search_url)
def scrape_image_links(search_url):
    response=requests.get(search_url)
    soup=BeautifulSoup(response.text, 'html.parser')
    image_links=[a['href'] for a in soup.find_all('a',{'class':'image-link'})]
    return image_links
    
def extract_image_details(image_url,tag_or_class):
    response = requests.get(image_url)
    soup=BeautifulSoup(response.text, 'html.parser')
    image_name=soup.find('your_tag_or_class').text
    return image_name
def generate_content_from_images(image_links,tag_or_class):
    for link in image_links:
        image_name=extract_image_details(link,tag_or_class)
        image_response = requests.get(link)
        image = PIL.Image.open(BytesIO(image_response.content))
        
        model=genai.GenerativeModel('gemini-pro-vision')
        #model=genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(image)
        print(f"Details about image '{image_name}':")
        print(response.text)
        speak(response.text)
        
def extract_tag_or_class(user_input):
    tag_match=re.search(r'tag:(\w+)',user_input)
    class_match = re.search(r'class:(\w+)',user_input)
    if tag_match:
        return tag_match.group(1)
    elif class_match:
        return class_match.group(1)
    else:
        return None   
    
def select_image_by_name(image_links,target_name):
    if not image_links:
        print("No images found for the given search query.")
        return None
    for link in image_links:
        image_name=extract_image_details(link)
        if target_name.lower() in image_name.lower():
            return link
    print(f"No image found with the name '{target_name}':")
    return None
    for i, link in enumerate(matching_images, 1):
        print(f"{i}.{link}")
        while True:
            try:
                user_choice=int(input("Enter the number of the image you want to select: "))
                if 1 <= user_choice <= len(matching_images):
                    
                    return matching_images[user_choice -1]
                else:
                    print("Invalid choice.Please enter a valid number.")
            except ValueError:
                print("Invalid input.please enter a number.")
def fetch_asteroids(start_date, end_date, api_key="Fe0znWeGxezbMOen0GUJGu4sEdsV53cYdfBzcieP"):
    if not start_date or not end_date:
        speak("Please provide the start and end dates for fetching asteroid data.")
        return
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        near_earth_objects = data.get("near_earth_objects", {})
        
        if near_earth_objects:
            for date, asteroids in near_earth_objects.items():
                speak(f"On {date}, the following asteroids are expected to approach Earth:")
                for asteroid in asteroids:
                    name = asteroid.get("name")
                    diameter = asteroid.get("estimated_diameter", {}).get("meters", {}).get("estimated_diameter_max", "unknown")
                    velocity = asteroid.get("close_approach_data", [{}])[0].get("relative_velocity", {}).get("kilometers_per_hour", "unknown")
                    distance = asteroid.get("close_approach_data", [{}])[0].get("miss_distance", {}).get("kilometers", "unknown")
                    
                    speak(f"Asteroid {name} with an estimated diameter of {diameter} meters is expected to approach Earth at a velocity of {velocity} kilometers per hour from a distance of {distance} kilometers.")
                    print(f"Asteroid {name} with an estimated diameter of {diameter} meters is expected to approach Earth at a velocity of {velocity} kilometers per hour from a distance of {distance} kilometers.")
                    
        else:
            speak("No asteroid data found for the given dates.")
            print("No asteroid data found for the given dates.")
    else:
        speak("An error occurred while fetching asteroid data.")
        print("An error occurred while fetching asteroid data.")

def prompt_for_date(date_type):
    while True:
        speak(f"Please provide the {date_type} date in the format YYYY-MM-DD.")
        date = input(f"Enter {date_type} date (YYYY-MM-DD): ")
        try:
            # Validate the date format
            valid_date = datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            speak("Invalid date format. Please try again.")
                       
def get_news(country="in"):
    news_country_codes = {
        "india": "in",
        "usa": "us","united states": "us","america": "us","uk": "gb","united kingdom": "gb","australia": "au","canada": "ca","france": "fr","germany": "de","japan": "jp","china": "cn", "pakistan": "pk","bangladesh": "bd","nepal": "np","bhutan": "bt","maldives": "mv","afghanistan": "af","albania": "al","iran": "ir","iraq": "iq","syria": "sy","turkey": "tr","saudi arabia": "sa","uae": "ae","qatar": "qa","kuwait": "kw","oman": "om","bahrain": "bh","jordan": "jo","lebanon": "lb","israel": "il",
    }
    country_code = news_country_codes.get(country.lower(), "in")
    news_api_key = "f0397453a3ab47a3a50332ab786b8339"
    news_url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={news_api_key}"

    try:
        response = requests.get(news_url)
        news_data = response.json()
        if news_data["status"] == "ok":
            articles = news_data["articles"][:25]
            for article in articles:
                speak(article["title"])
                print(article["title"])

        else:
            speak("Unable to fetch news at the moment.")
    except Exception as e:
        print(e)
        speak("An error occurred while fetching news.")    
        
def get_train_status(train_number, start_day):
    url = "https://irctc1.p.rapidapi.com/api/v1/liveTrainStatus"
    headers = {
        "X-RapidAPI-Key": "b2a97dd30emsh94f00a14247a153p15cb2ajsnd8819d6ced32",
        "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
    }
    
    querystring = {"trainNo": train_number, "startDay": start_day}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response_data = response.json()
        if response.status_code == 200 and response_data["status"]:
            data = response_data["data"]
            train_start_date = data["train_start_date"]
            train_name = data["train_name"]
            title = data["title"]
            new_message = data["new_message"]
            source = data["source"]
            destination = data["destination"]
            
            speak(f"Train number {train_number}, the {train_name} started on {train_start_date} from {source} to {destination}.")
            print(f"Train number {train_number}, the {train_name} started on {train_start_date} from {source} to {destination}.")
            speak(f"Latest update: {new_message}")
            print(f"Train number {train_number}, the {train_name}, {title}.")
            print(f"Latest update: {new_message}")
            print(f"Source station: {source}")
            print(f"Destination station: {destination}")
            
        else:
            error_message = response_data.get("message", "An error occurred while fetching train status.")
            speak(error_message)
            print(error_message)
    except Exception as e:
        print(f"Error fetching train status: {e}")
        speak(f"An error occurred while fetching train status information: {e}")

def extract_digits(text):
    return''.join(re.findall(r'\d+',text)) 
        
def prompt_for_train_status():
    print("Please tell me the train number you want to check.")
    speak("Please tell me the train number you want to check.")
    train_number_response = takeCommand().lower()
    train_number = extract_digits(train_number_response)
    print("Please tell me for which day you want to check. You can say today, 1 days ago, 2 days ago, 3 days ago, 4 days ago")
    speak("Please tell me for which day you want to check. You can say today, 1 days ago, 2 days ago, 3 days ago, 4 days ago")
    day_response = takeCommand().lower()
    day_mapping = {"today":"0", "current day":"0", "1 day ago": "1", "1 day": "1", "one day": "1", "2 days ago": "2", "3 days ago": "3", "4 days ago": "4"}       
    start_day = next((code for phrase, code in day_mapping.items() if phrase in day_response), "0")
    speak(f"Checking the status of train number {train_number} for {start_day} days ago.")
    get_train_status(train_number, start_day)
                
def get_newsu():
    news_api_key = "f0397453a3ab47a3a50332ab786b8339"
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"

    try:
        response = requests.get(news_url)
        news_data = response.json()
        if news_data["status"] == "ok":
            articles = news_data["articles"][:10]
            for article in articles:
                speak(article["title"])
                print(article["title"])

        else:
            speak("Unable to fetch news at the moment.")
    except Exception as e:
        print(e)
        speak("An error occurred while fetching news.")


def get_weather(city):
    weather_api_key = "c1fd90b3f1c009b91ebee2f929b181b3"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"

    try:
        response = requests.get(weather_url)
        weather_data = response.json()

        if response.status_code == 200:
            temperature = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            Tc = temperature - 273.15
            Yr = round(Tc, 2)
            print(Yr)
            speak(
                f"The weather in {city} is {description} with a temperature of {Yr} Deegree Celsius."
            )

        else:
            speak(f"Unable to fetch weather for {city} at the moment.")

    except Exception as e:
        print(e)
        speak("An error occurred while fetching weather information.")


def send_email(subject, body, to_email):
    sender_email = "worldforensic@gmail.com"
    sender_password = "dhya zyay xrau ooew"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, to_email, message)

        print("Email sent successfully!!")

    except Exception as e:
        print(f"Eroor sending email: {e}")

def fetch_news(country):
    country_codes = {'india': 'IN', 'usa': 'US', 'united states': 'US', 'america': 'US', 'uk': 'GB', 'united kingdom': 'GB', 'australia': 'AU', 'canada': 'CA', 'france': 'FR', 'germany': 'DE', 'japan': 'JP', 'china': 'CN', 'russia': 'RU', 'brazil': 'BR', 'south africa': 'ZA', 'nigeria': 'NG', 'kenya': 'KE', 'egypt': 'EG', 'mexico': 'MX', 'argentina': 'AR', 'spain': 'ES', 'italy': 'IT', 'netherlands': 'NL', 'switzerland': 'CH', 'sweden': 'SE', 'norway': 'NO', 'denmark': 'DK', 'finland': 'FI', 'ireland': 'IE', 'newzealand': 'NZ', 'singapore': 'SG', 'malaysia': 'MY', 'indonesia': 'ID', 'philippines': 'PH', 'vietnam': 'VN', 'thailand': 'TH', 'south korea': 'KR', 'turkey': 'TR', 'saudi arabia': 'SA', 'uae': 'AE', 'qatar': 'QA', 'kuwait': 'KW', 'oman': 'OM', 'bahrain': 'BH', 'jordan': 'JO', 'lebanon': 'LB', 'pakistan': 'PK', 'bangladesh': 'BD', 'sri lanka': 'LK', 'nepal': 'NP', 'bhutan': 'BT', 'maldives': 'MV', 'afghanistan': 'AF', 'albania': 'AL', 'iran': 'IR', 'iraq': 'IQ', 'syria': 'SY'}
    base_url = 'https://news.google.com/home?hl=en-{}&gl={}&ceid={}'
    country_code = country_codes.get(country.lower(),'IN')
    url = base_url.format(country_code, country_code, country_code)
    webbrowser.open(url)

app_id = "TTGJYL-82236UH42E"
client = wolframalpha.Client(app_id)
engine = pyttsx3.init()

def wolfram_alpha_query(user_query):
    try:
        result = client.query(user_query)

        for pod in result.pods:
            if pod.text:
                print(pod.text)
                speak(pod.text)
    except Exception as e:
        print("Error processing the Wolfran Alpha query:", e)
        

def about_me():
     print("I am Alaxander for Everythings, a voice assistant developed by Suraj Kumar Pandey. My purpose is to provide expert guidance, image processing, information retrieval, counseling, task execution, and learning support. People choose me for my unrivaled mathematical problem-solving abilities, comprehensive question assistance, and efficient coding and software development capabilities. I offer versatility across domains, future-ready AI innovation, and personalized user experiences. Additionally, I prioritize ethical and responsible AI practices, ensuring user privacy and data security. With me, users experience seamless integration with workflows, robust knowledge integration, and an interactive learning environment. I am committed to empowering accessibility and inclusion, revolutionizing technological interaction through voice-driven models, and advancing the quality of life for all users.")
     speak("I am Alaxander for Everythings, a voice assistant developed by Suraj Kumar Pandey. My purpose is to provide expert guidance, image processing, information retrieval, counseling, task execution, and learning support. People choose me for my unrivaled mathematical problem-solving abilities, comprehensive question assistance, and efficient coding and software development capabilities. I offer versatility across domains, future-ready AI innovation, and personalized user experiences. Additionally, I prioritize ethical and responsible AI practices, ensuring user privacy and data security. With me, users experience seamless integration with workflows, robust knowledge integration, and an interactive learning environment. I am committed to empowering accessibility and inclusion, revolutionizing technological interaction through voice-driven models, and advancing the quality of life for all users.")
                    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        user_res = chat.send_message(query)
        model_response = user_res.text
        if "image detection" in query:
            match=re.search(r'\b\d+\b',query)
            
            if match:
                selected_number= int(match.group())
                perform_image_detection(selected_number)
            else:
                print("No number found in the query. Please specify a number for image detection.")
            continue
          
        elif "image search" in query:
            search_query=query.replace("image search","").strip()
            image_links=image_search(search_query)
            time.sleep(20)
            print("Enter the name of the image you want to select from these images:")
            speak("Enter the name of the image you want to select from these images:")
            target_image_name=takeCommand().lower()
            
            tag_or_class="your_tag_or_class"
            selected_image_url = select_image_by_name(image_links, target_image_name)
            if selected_image_url:
                image_name=extract_image_details(selected_image_url, tag_or_class)
                generate_content_from_images([selected_image_url],tag_or_class)
            continue
        elif "youtube music search" in query:
            yt_query=query.replace("youtube music search","").strip()
            yt_search(yt_query)
            continue
        elif "nasa image" in query:
            process_query(query)
            continue
        elif "near earth object" in query:
            speak("Fetching NASA asteroid data...")
            start_date = prompt_for_date("start")
            end_date = prompt_for_date("end")
            fetch_asteroids(start_date, end_date)           
        elif "update news" in query:
            country = query.replace("update news", "").strip().lower()
            get_news(country)
            continue
        elif "nasa" in query:
            get_apod(api_key)
              
        elif "google scholar" in query:
            search_query=query.replace("google scholar","").strip()
            google_scholar(search_query)
            continue
        elif "open news" in query:
            country = query.replace("open news", "").strip().lower()
            fetch_news(country)
        
        #elif "scholar search" in query:
        #    speak("What topic should I search for on Google Scholar?")
        #    topic = takeCommand().lower()
        #    if "retry" in topic:
        #        continue
        #    search_results = google_scholar_search(topic)
        #    if 'organic_results' in search_results:
        #        for result in search_results['organic_results']:
        #            print(result['title'])
        #            speak(result['title'])
        #    else:
        #        print("No search results found for the given topic.")
        #        speak("No search results found for the given topic.")
        
        
        elif "map search" in query:
            map_query=query.replace("map search","").strip()
            map_search(map_query)
            continue
        
        elif "weather in" in query:
            city_name = query.split("weather in")[-1].strip()
            get_weather(city_name)
            continue

        
        elif "train status" in query:
            prompt_for_train_status()
            continue
        elif "tell me about yourself" in query or "about yourself" in query or "who are you" in query:
            about_me()
            continue
        elif "send email" in query:
            speak("what is the subject of the email?")
            subject = takeCommand()

            speak("What is the message of the email?")
            body = takeCommand()

            speak("What is the username of the recipient's email address?")
            username = takeCommand().replace(" ", "")

            speak("What is the domain of the recipient's email address?")
            domain = takeCommand().replace(" ", "")

            to_email = f"{username}@{domain}"
            send_email(subject, body, to_email)
            continue
        
        else:
         if "Say that again please..." in query:
                continue
        if "retry" in query:
                continue
                  
        print(model_response)
        speak(model_response)
        chat.history.append({"role": "user", "parts": [query]})
        chat.history.append({"role": "model", "parts": [user_res.text]})

        if "wikipedia" in query.lower():
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "").strip()

            try:
                results = wikipedia.summary(query, sentences=10)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"Ambiguous term. Suggestions:{e.options}")
                speak(f"Ambiguous trm. Suggestions: {', '.join(e.options)}")
            except wikipedia.exceptions.PageError:
                print(f"Page for '{query}' not found on wikipedia.")
                speak(f"Sorry,I couldn't find information about {query} on wikipedia.")
                continue

        elif "calculate" in query:
            calculation_query = query.lower().split("calculate", 1)[1].strip()
            wolfram_alpha_query(calculation_query)
            continue

        elif "conversation" in query:
            run_conversation()
            continue
            # elif "image detection" in query:
            match = re.search(r"\b\d+\b", query)

            if match:
                selected_number = int(match.group())
                perform_image_detection(selected_number)
            else:
                print(
                    "No number found in the query. Please specify a number for image detection."
                )
            continue

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            continue

        elif "open google" in query:
            webbrowser.open("google.com")
            continue

        elif "open powerful gpt" in query or "chatgpt" in query or "chat GPT" in query:
            webbrowser.open("https://chat.openai.com/")
            continue

        elif "current time" in query:
            webbrowser.open("https://www.timeanddate.com/worldclock/india/new-delhi")
            continue

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
            continue

        elif "open leet code" in query or "open lead code" in query:
            webbrowser.open("leetcode.com")
            continue

        elif "open suraj facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            continue

        elif "play music" in query:
            a = random.randint(0, 15)
            music_dir = "C:\\Users\\SURAJ PANDEY\\Music\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[a]))
            continue

        elif "chacha ka favourite song" in query:
            music_dir3 = "C:\\Users\\SURAJ PANDEY\\Music\\song"
            songs1 = os.listdir(music_dir3)
            print(songs1)
            os.startfile(os.path.join(music_dir3, songs1[0]))
            continue

        elif "play video" in query:
            b = random.randint(0, 10)
            video_dir = "C:\\Users\\SURAJ PANDEY\\Videos\\video"
            videos = os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir, videos[b]))
            continue

        elif "the time" in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
            continue
        elif "the date" in query:
            strftime = datetime.now().strftime("%d/%m/%Y")
            speak(f"Sir, the date is {strftime}")
            print(f"Sir, the date is {strftime}")
            continue

        elif "open code" in query:
            codePath = "C:\\Users\\SURAJ PANDEY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            continue

        elif "wikipedia about" in query:
            query = query.replace("tell me about", "")
            if check_page_exists(query):
                summary = get_summary(query)
                print(summary)
                speak(summary)

                page_url = get_page_url(query)
                print("Wikipedia URL:", page_url)
                webbrowser.open(page_url)
                continue

            else:
                general_response = "I' m sorry, but i could't find just now makebe its not valid page title,please provide valid page title..."
                speak(general_response)
                print(general_response)
                continue

        elif "stock market us" in query:
            url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=ZWTLSV9EWQ8XREJ1"
            r = requests.get(url)
            data = r.json()
            print(data)
            speak(data)
            continue
        elif "stock market india" in query:
            url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey=ZWTLSV9EWQ8XREJ1"
            r = requests.get(url)
            data = r.json()
            print(data)
            speak(data)
            continue

        elif "current news united states" in query or "current news usa" in query:
            get_newsu()
            continue

        elif "rajkiya engineering college azamgarh" in query:
            speak(
                "Rajkiya Engineering College, Azamgarh (formerly MKECIT) was established in 2007 and began offering B.Tech. programs in Information Technology, Mechanical Engineering, and Civil Engineering from 2010. Its aim is to provide education, conduct research, and lead in technological innovation for industrial and infrastructural development."
            )
            webbrowser.open("https://www.gecazamgarh.ac.in/")
            continue

        elif "open my website" in query or "open suraj website" in query:
            webbrowser.open(
                "https://surajinformationtechnologyportfolio.000webhostapp.com/"
            )
            continue

        elif "what you can help to me" in query:
            rocky = "I can do everything at a place has I will start my wishing to you, I will help in everything has you ask any reasoning question a logical or if you want to describe anything's by voice command as well as a print format screen will be provided, it can provide current update of news of all over world and universe specially now India and USA, weather updation if you want to send email only my voice command and what you message it can be also doing it can open all required things, tabs which you want it can play music play video as well as, also your update your college information rajkiya engineering college Azamgarh and other well air quality updation geocoding travel management money management status current seat availability in Bus, Flight and train Hospital facility as(how much seat available currently)blood bank enquiry stock market data India and USA current price of things at different platform Recommendation of price analysis to the lowest price and open their website to purchase counselling JEE main plus advance on basis on rank which college will get book coaching recommendation for 11th 12th 10th 9th 8th, brain augmentation topic which I have to research in now in the USA, so it seems to be discussed by this neuroscience Technologies will be updated as well as our research paper of all the colleges of all the professor will be also updated their news updation for other celestial bodies has other planets has life exist or not relevant research articles future prediction accurate predict for everything and many more..."
            print(rocky)
            speak(rocky)
            continue

        elif "what's your feature" in query:
            feature = " Inquiries and answers to logical or reasoning questions.News updates from around the world, including India and the USA.Weather updates, email composition and sending.Music and video playback.College information updates, including Rajkiya Engineering College, Azamgarh.Air quality updates.Travel management, geocoding, and money management.Availability of seats in buses, flights, and trains.Hospital facility updates, including available beds and blood bank information.Stock Market data for both India and the USA.Price analysis and recommendations for the lowest price.Counseling on JEE Main and Advanced based on your rank, college recommendations, and coaching recommendations for various grades.Brain augmentation research topic suggestions and updates on neuroscience technologies.Research paper updates from professors across various colleges.News and information updates on celestial bodies and the possibility of life on other planet.Relevant research articles and accurate future predictions."
            speak(feature)
            continue

        elif "your feature in short" in query:
            short = "Inquiries, logic Q&A, worldwide news, weather, email, music, video, college info, Air quality, travel, finance, seat availability, hospital updates, stock market data, price analysis, JEE counseling, brain augmentation, neuroscience, research papers, celestial updates, life on planets, research articles, future predictions."
            speak(short)
            continue

        

        if (
            "generate text" in query
            or "solve" in query
            or "logical question" in query
            or "reasoning" in query
            or "explain" in query
            or "start" in query.lower()
        ):
            try:
                speak("Please provide a prompt for text generation.")
                prompt = takeCommand()

                completion = palm.generate_text(
                    model="models/text-bison-001",
                    prompt=prompt,
                    temperature=0,
                    max_output_tokens=800,
                )

                generated_text = completion.result
                print(generated_text)
                speak(generated_text)
                continue

            except Exception as e:
                print(f"Error generating text:{e}")
                speak("Sorry,I couldn't generate the text or solution at the moment.")
                continue

        elif "find" in query:
            query = query.replace("find", "")

            completion = palm.generate_text(
                model="models/text-bison-001",
                prompt=query,
                temperature=0,
                max_output_tokens=800,
            )

            generated_text = completion.result
            print(generated_text)
            speak(generated_text)
        if (
            "true data" in query
            or "explore" in query
            or "research" in query
            or "hunt" in query
            or "super" in query
            or "enquiry" in query
            or "current data" in query.lower()
        ):
            try:
                speak("Please provide a prompt for text generation.")
                prompt = takeCommand()

                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(prompt)
                generated_text = response.text
                print(generated_text)
                speak(generated_text)
                continue

            except Exception as e:
                print(f"Error generating text:{e}")
                speak("Sorry,I couldn't generate the text or solution at the moment.")
                continue

        elif "search" in query:
            query = query.replace("search", "")

            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(query)
            generated_text = response.text
            print(generated_text)
            speak(generated_text)
            continue

        elif "thank you" in query or "thank" in query:
            speak("very very welcome")
            s = random.randint(0, 2)
            video_dir1 = "C:\\Users\\SURAJ PANDEY\\Downloads\\thanku"
            videos1 = os.listdir(video_dir1)
            print(videos1)
            os.startfile(os.path.join(video_dir1, videos1[s]))
            break
        elif "retry" in query:
            continue

        elif "stop" in query or "quit" in query:
            speak("Goodbye!")
            a = wishMe1()
            speak("")
            break
        elif (
            "close" in query
            or "urgent exit" in query
            or "emergency exit" in query
            or "exit" in query
        ):
            speak("TAKE CARE!! BYE BYE")
            break

            # else:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(query)
            generated_text = response.text
            print(generated_text)
            speak(generated_text)
            continue
        #else:
        # if "Say that again please..." in query or "retry" in query:
        #        continue
        #speak(model_response)
        #print(model_response)
        #chat.history.append({"role": "user", "parts": [query]})
        #chat.history.append({"role": "model", "parts": [user_res.text]})
