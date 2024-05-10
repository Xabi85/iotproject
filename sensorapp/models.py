from django.db import models

class TemperatureReading(models.Model):
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Temperature: {self.temperature} ºC'

class HumidityReading(models.Model):
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Humidity: {self.humidity} %'

        