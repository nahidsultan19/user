from django.db import models
from phone_field import PhoneField


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


GENDER = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
)


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    phone = PhoneField(
        blank=True, help_text='Contact phone number', unique=True)
    gender = models.CharField(choices=GENDER, max_length=6)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
