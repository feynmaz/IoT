import datetime
from os.path import dirname
import sqlite3

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS



def load_to_influx(data):

    # You can generate a Token from the "Tokens Tab" in the UI
    token = "fwxYihpHF05NDe6NYfw8ohZnGN9n-YWCjhW2wI8dDvr35dyYYtTdzk2CCYxNjmZgPmNbujXrlPWmxNc9PWd3JA=="
    org = "iotdb182@gmail.com"
    bucket = "iotdb182"
    client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token)
    write_api = client.write_api(write_options=SYNCHRONOUS)


    guest_id = data['guest_id']
    temperature = data['temperature']
    dt = datetime.datetime.utcnow()
    

    temperature_entry = Point("guests"
    ).tag("guest_id", f"{guest_id}"
    ).field("temperature", temperature
    ).time(dt,WritePrecision.NS)
    write_api.write(bucket, org, temperature_entry)

    return {
        'date': dt.date(),
        'time': dt.time(),
        'guest_id': guest_id,
        'temperature': temperature
    }
