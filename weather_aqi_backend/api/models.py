from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather in {self.city.name} at {self.date}"

class AQI(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    aqi = models.IntegerField()
    so2 = models.FloatField()
    no2 = models.FloatField()
    pm10 = models.FloatField()
    pm2_5 = models.FloatField()
    o3 = models.FloatField()
    co = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AQI in {self.city.name} at {self.date}"
