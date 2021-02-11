from django.db import models

# Create your models here.


class Groups(models.Model):
    Name = models.CharField('Name of group', max_length=15)
    Description = models.CharField('Description', max_length=30)

    def __str__(self):
        return self.Name


class Users(models.Model):
    username = models.CharField('User nickname', max_length=25)
    created = models.DateTimeField('Date')
    group = models.ForeignKey('Groups',  on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.username

