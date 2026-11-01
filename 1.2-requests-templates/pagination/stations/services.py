import csv
from django.conf import settings

def work_with_csv() :
    '''Функция чтения csv файла'''
    path = settings.BUS_STATION_CSV

    data = []

    with open(path,mode="r",encoding="utf-8") as file :
        reader = csv.DictReader(file)
        for row in reader :
            data.append(row)
    return data