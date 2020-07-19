import logging
from datetime import datetime
from pytz import timezone
import pytz

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    moscow = timezone("Europe/Moscow")
    london = timezone("Europe/London")
    paris = timezone("Europe/Paris")
    n_york = timezone("America/New_York")
    pekin = timezone("Japan")
    strf = "%H:%M:%S"
    moscow_t = "Время в Москве: " + datetime.now(moscow).strftime(strf) + "\n"
    london_t = "Время в Лондоне: " + datetime.now(london).strftime(strf) + "\n"
    paris_t = "Время в Париже: " + datetime.now(paris).strftime(strf) + "\n"
    n_york_t = "Время в Нью-Йорке: " + datetime.now(n_york).strftime(strf) + "\n"
    pekin_t = "Время в Пекине: " + datetime.now(pekin).strftime(strf) + "\n"
    result = moscow_t + london_t + paris_t + n_york_t + pekin_t
    return func.HttpResponse(result)
