from os.path import dirname
import random
import datetime
import sqlite3
import os
from random_object_id import generate

def get_data():
    sigur_data = get_sigur_data()
    arduino_data = get_arduino_data()

    return {
        'guest_id': sigur_data,
        'temperature': arduino_data,
    }


def get_sigur_data():
    random_idx = random.randint(1,10)
    random_guest_id = get_random_id(random_idx)
    return random_guest_id


def get_arduino_data():
    # имитация считывания данных Arduino c сервера Mosquitto
    temperature = round(random.uniform(34.8,37.8),1)
    return temperature


def get_random_id(index):
    db_location = os.path.dirname(dirname(dirname(__file__))) + '\\' + 'db.sqlite3'
    with sqlite3.connect(db_location) as conn:
        c = conn.cursor()
        c.execute('''
        select guest_id from (
            select 
                guest_id,
                row_number() over (order by guest_id asc) as row_number
            from guests
        )
        where row_number = ?
        ''', (index,))
        return c.fetchone()[0]


def get_random_dt():
    timestamps = get_timestamps()

    return timestamps['start'] + datetime.timedelta(
        seconds=random.randint(0, int((timestamps['end'] - timestamps['start']).total_seconds())),
    )


def get_timestamps():
    end = datetime.datetime.now()
    start = end - datetime.timedelta(hours=2)
    return {
        'start' : start,
        'end' : end
    }

