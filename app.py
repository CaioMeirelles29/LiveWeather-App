import requests
import api_token

api_key = api_token

user_input = input("Selecione a cidade: ")
city_name = user_input

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br")

if weather_data.json()["cod"] == "404":
    print("Cidade não encontrada")
else:
    weather = weather_data.json()["weather"] [0] ["description"]
    temp = round(weather_data.json() ["main"] ["temp"])

    print(f"O tempo em {user_input} está: {weather.capitalize()}")
    print(f"A temperatura em {user_input} é de: {round(temp - 273.15)}ºC")




