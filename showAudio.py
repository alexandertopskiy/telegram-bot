import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    result = requests.get("https://www.songsterr.com/a/ra/songs.json?pattern={}".format(name))
    a = result.json()
    audios = ''
    for music in a:
        audios = audios + music['title'] + '\n'
    return func.HttpResponse(audios)
