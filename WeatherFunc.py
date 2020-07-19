import logging
import requests
appid = '576f4ed692e288b1aaa29086788ecb4b'
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    city = req.params.get('city')
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'appid': appid})
    data = res.json()
    result = 'Город: ' + data['city']['name'] + " " + data['city']['country'] + "\n"
    for i in data['list']:
        a =  i['dt_txt'] + ' {0:+3.0f}'.format(i['main']['temp']) + " " + i['weather'][0]['description'] + "\n"
        result = result + a
    return func.HttpResponse(result)
    #return func.HttpResponse(city)