import requests
url = "https://airvisual.com/api"
api_key = "d320390b-e709-413d-909b-c1dcb3e83eea"
# res = requests.get(url)
# base_url = url+api_key+

def getCityNames():
    cities = ["hyderabad", "delhi", "bangalore", "mumbai"]
    for cityname in cities:
        yield(cityname)

def readUrl():
    print("reading url")
    cityObj = getCityNames()
    for i in cityObj:
        url_city = url+api_key+i
        res = requests.get(url_city)
        x=res.json()




print(readUrl())
