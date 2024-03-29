# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Deadlines(models.Model):
    dl_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=20)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deadlines'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    userlastname = models.CharField(max_length=20)
    deadline = models.ForeignKey(Deadlines, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users'
