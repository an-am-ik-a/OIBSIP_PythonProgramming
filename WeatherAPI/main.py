import webbrowser
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather = response.text
            print("----------Weather Report----------")
            print(weather)
            print("----------------------------------")
        else:
            print("Sorry, I couldn't fetch the weather.")
    except:
        print("An error occurred while fetching the weather.")

if (__name__ == "__main__"):
    city=input("Enter the city name: ")
    get_weather(city)