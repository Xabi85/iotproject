from django.shortcuts import render

from .models import TemperatureReading, HumidityReading

def latest_temperature(request):
    latest_temperature_reading = TemperatureReading.objects.latest('timestamp')
    context = {'temperature': latest_temperature_reading.temperature}
    return render(request, 'temperature.html', context)

def latest_humidity(request):
    latest_humidity:reading = HumidityReading.objects.latest('timestamp')
    context = {'humidity': latest_humidity_reading.humidity}
    return render(request, 'humidity.html',context)

    
