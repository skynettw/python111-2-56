from django.db import models

class HBicycleData(models.Model):
    sna = models.CharField(max_length=100)
    sbi = models.IntegerField(default=0)
    tot = models.IntegerField(default=0)
    class Meta:
        ordering = ('-sbi',)
    def __str__(self):
        return self.sna

class NKUSTnews(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
