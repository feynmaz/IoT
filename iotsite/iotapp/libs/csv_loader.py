import csv
import datetime
import os
from os.path import dirname
import sqlite3
import unicodecsv


def load_to_csv(data):
    
    file = get_file_path()
    status = define_status(data['guest_id'],data['temperature'])
    f = open(file,'ab')
    w = unicodecsv.writer(f, encoding='utf-8')

    w.writerow((
        data['date'],
        data['time'],
        data['guest_id'],
        data['temperature'],
        status
    ))
    f.close()    
    

def get_file_path():
    
    folder_location = os.path.dirname(dirname(__file__)) + '\\out\\'

    yyyy = datetime.date.today().year
    mm = datetime.date.today().month
    dd = datetime.date.today().day

    file_name = str(yyyy) + '_' + str(mm).zfill(2) + '_' + str(dd).zfill(2) + '.csv' 

    return folder_location + file_name


def define_status(guest_id, temperature):


    is_in = get_is_in(guest_id)
    
    if (is_in):
        status = 'выход'
        set_is_in_false(guest_id)
    else:
        if temperature < 37.0:
            status = 'проход'
            set_is_in_true(guest_id)
        else:
            status = 'запрет'
    
    return status


def get_is_in(guest_id):

    db_location = dirname(dirname(dirname(__file__))) + '\\' + 'db.sqlite3'
    with sqlite3.connect(db_location) as conn:
        c = conn.cursor()
        c.execute(''' select is_in from guests where guest_id = ? ''',(guest_id,))
        return c.fetchone()[0]


def set_is_in_true(guest_id):
    db_location = dirname(dirname(dirname(__file__))) + '\\' + 'db.sqlite3'
    with sqlite3.connect(db_location) as conn:
        c = conn.cursor()
        c.execute(''' update guests set is_in = 1 where guest_id = ? ''',(guest_id,))
        conn.commit()


def set_is_in_false(guest_id):
    db_location = dirname(dirname(dirname(__file__))) + '\\' + 'db.sqlite3'
    with sqlite3.connect(db_location) as conn:
        c = conn.cursor()
        c.execute(''' update guests set is_in = 0 where guest_id = ? ''',(guest_id,))
        conn.commit()