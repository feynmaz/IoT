from django.shortcuts import render
from django.http import HttpResponse
import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision

from .libs import source_emulator,csv_loader,influx_loader


# Create your views here.
def index(request):
    context = {}
    return render(request, template_name='index.html', context=context)


def process_a_guest(request):
    data_for_influx = source_emulator.get_data()
    data_for_csv = influx_loader.load_to_influx(data_for_influx)
    csv_loader.load_to_csv(data_for_csv)

    return HttpResponse('Success')


