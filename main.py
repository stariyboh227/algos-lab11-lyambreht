import  requests
import json

while True:
    base_url = "http://www.omdbapi.com/?apikey=505480d7&s="
    command = input("Enter command (or 'exit' to quit): ")

    if command.lower() == "exit":
        print("Goodbye!")
        break
    else:
        print(f"You entered: {command}")
        full_url = requests.get(f"{base_url}{command}")
        data = full_url.json()


        print(data)  # https://api.example.com/search?q=python

        for movie in data.get("Search"):
            print(f"{movie["Title"]} ({movie["Year"]})")
