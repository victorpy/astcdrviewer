# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cdr(models.Model):
    acctid = models.BigIntegerField(primary_key=True)
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    did = models.CharField(max_length=50)
    recordingfile = models.CharField(max_length=255)
    cnum = models.CharField(max_length=40)
    cnam = models.CharField(max_length=40)
    outbound_cnum = models.CharField(max_length=40)
    outbound_cnam = models.CharField(max_length=40)
    dst_cnam = models.CharField(max_length=40)

    def __str__(self):
        return str(self.acctid)

    class Meta:
        managed = False
        db_table = 'cdr'


class Cel(models.Model):
    eventtype = models.CharField(max_length=30)
    eventtime = models.DateTimeField()
    cid_name = models.CharField(max_length=80)
    cid_num = models.CharField(max_length=80)
    cid_ani = models.CharField(max_length=80)
    cid_rdnis = models.CharField(max_length=80)
    cid_dnid = models.CharField(max_length=80)
    exten = models.CharField(max_length=80)
    context = models.CharField(max_length=80)
    channame = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    appname = models.CharField(max_length=80)
    appdata = models.CharField(max_length=80)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    linkedid = models.CharField(max_length=32)
    peer = models.CharField(max_length=80)
    userdeftype = models.CharField(max_length=255)
    eventextra = models.CharField(max_length=255)
    userfield = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cel'


class GatewayCodes(models.Model):
    id = models.IntegerField(primary_key=True)
    gwcode = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'gateway_codes'


class TrunksAccountcodes(models.Model):
    accountcode = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'trunks_accountcodes'

class Accounts(models.Model):
    id_account = models.AutoField(primary_key=True)
    account_code = models.IntegerField()
    credit = models.FloatField()
    extension = models.CharField(max_length=32)
    username = models.CharField(max_length=30)
    id_rate_group = models.IntegerField()
    prefix = models.CharField(max_length=4)

    def __str__(self):
        return str(self.id_account)

    class Meta:
        managed = False
        db_table = 'accounts'



class Payments(models.Model):
    id_payment = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    id_account = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return str(self.id_payment)

    class Meta:
        managed = False
        db_table = 'payments'


class Rate(models.Model):
    id_rate = models.AutoField(primary_key=True)
    id_rate_group = models.IntegerField()
    destination = models.CharField(max_length=64)
    description = models.CharField(max_length=64, blank=True, null=True)
    amount1 = models.FloatField()
    cadence1 = models.IntegerField()
    cadence2 = models.IntegerField()
    amount2 = models.FloatField()

    def __str__(self):
        return str(self.id_rate)

    class Meta:
        managed = False
        db_table = 'rate'


class RateGroup(models.Model):
    id_rate_group = models.AutoField(primary_key=True)
    description = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id_rate_group)


    class Meta:
        managed = False
        db_table = 'rate_group'

class RatedCdr(models.Model):
    id_rated_cdr = models.AutoField(primary_key=True)
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    amount = models.FloatField()
    accountcode = models.IntegerField()
    billsec = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rated_cdr'

