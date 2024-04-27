import requests
import json
print("\n                     Welcome Weather Report 1.1              \n")
print("---------------------------------------------------------------------")
while True:
    city = input("Enter Name Of the City :")

    url = f"https://api.weatherapi.com/v1/current.json?key=eed3323c1d104554a4754710230912&q={city}"

    r = requests.get(url)
    try:
        wdic =json.loads(r.text)
        print("Current temprature in degree : ",wdic["current"]["temp_c"])
        print("Current temprature fernite : ",wdic["current"]["temp_f"])
        print("Last Updated : ",wdic["current"]["last_updated"])
        print("---------------------------------------------------------------------")
        print("                     Weather App is Created By the Sam\n\n")
        break
    except KeyError:
        print("You have entered wrong city.")
        city = input("Enter the name of the city :")
    

## api testing url :https://api.weatherapi.com/v1/current.json?key=eed3323c1d104554a4754710230912&q=pune
# free api website : https://www.weatherapi.com/
 

