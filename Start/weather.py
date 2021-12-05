import requests
def get_weather_desc_and_temp():
    api_key = "b587f170d81e273ac157ca181a113fea"
    city = "Shenzhen"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()
    # print(json)

    # [0]:First weather
    description = json.get("weather")[0].get("description")
    minimum = json.get("main").get("temp_min")
    maximum = json.get("main").get("temp_max")
    
    # Dicationary Type Key can't use " ",only use ' '
    return {'description':description,
            'minimum':minimum,
            'maximum':maximum}
def main():
    weather_dict = get_weather_desc_and_temp()
    # Print Result
    print("Today's forecast is",weather_dict.get("description"))
    print("The minimum temperature is ",weather_dict.get("minimum"))
    # Summary: 1.weather is list, it can use [0];
    #          2.main is dicationary,it can't use [0].
    print("The maximum temperature is ",weather_dict.get("maximum"))
main()
