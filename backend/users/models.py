from django.db import models
from django.utils import timezone


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BanStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Users(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=250)
    id_role = models.ForeignKey(Role, on_delete = models.CASCADE)
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    about_me = models.CharField(max_length=250)
    
    def __str__(self):
        return self.login


class BanList(models.Model):
    id_ban_status = models.ForeignKey(BanStatus, on_delete = models.CASCADE)
    id_user = models.ForeignKey(Users, on_delete = models.CASCADE)
    up_to_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id_ban_status





