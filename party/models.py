from django.db import models

class Party(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Name of the party')
    symbol = models.ImageField(upload_to='party_symbols/', help_text='Email address of the party')
    leader = models.CharField(max_length=100, help_text='Leader of the party')
    foundation_date = models.DateField(help_text='Foundation date of the party')
    email = models.EmailField(max_length=100, blank=True, null=True, help_text='Email address of the party')
    password = models.CharField(max_length=100, blank=True, null=True, help_text='Password of the party')
    status = models.CharField(max_length=100, help_text='Status of the party')
    phone = models.CharField(max_length=100, help_text='Phone number of the party')

class BallotBox(models.Model):
    partyleader = models.CharField(max_length=100)
    partyname = models.CharField(max_length=100)
    voter = models.CharField(max_length=100)