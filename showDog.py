import logging
import requests
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    result = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
    url = result.json()[0]
    return func.HttpResponse(url)
