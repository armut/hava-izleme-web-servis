from django.db import models

class ParserLog(models.Model):
    station = models.ForeignKey(Station, null=True))
    date = models.DatetimeField(null=True)



class Station(models.Model):
    name = models.CharField(max_length=60)
