from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    ticket_type = models.CharField(max_length=100)

    class Meta:
        app_label = 'Event_Booking_System'

