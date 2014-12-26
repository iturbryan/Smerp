from django.db import models
from core.models import User

# Create your models here.

class ChartClass(models.Model):
  name = models.CharField(max_length = 255)
  description = models.CharField(max_length = 255)
  
  def __unicode__(self):
    return self.name
  

class FiscalYear(models.Model):
  name = models.CharField(max_length = 255)
  code = models.CharField(max_length = 255)
  start_date = models.DateField()
  end_date = models.DateField()
  open = models.BooleanField(default = False)
  
  def __unicode__(self):
    return self.name
  
class Period(models.Model):
  fiscal_year = models.ForeignKey(FiscalYear)
  name = models.CharField(max_length = 255)
  code = models.CharField(max_length = 255)
  start_date = models.DateField()
  end_date = models.DateField()
  open = models.BooleanField(default = False)
  
  def __unicode__(self):
    return self.name
  
  
class Currency(models.Model):
  name = models.CharField(max_length = 255)
  code = models.CharField(max_length = 255)
  
  def __unicode__(self):
    return self.name
  
  
class ChartType(models.Model):
  chart_class = models.ForeignKey(ChartClass)
  chart_type = models.ForeignKey('self', null = True)
  name = models.CharField(max_length = 255)
  description = models.CharField(max_length = 255)
  
  def __unicode__(self):
    return self.name
  
  
class Account(models.Model):
  chart_type = models.ForeignKey(ChartType)
  code = models.CharField(max_length = 255)
  name = models.CharField(max_length = 255)
  
  def __unicode__(self):
    return "%s - %s" % (self.code, self.name)
 
    
class JournalType(models.Model):
  name = models.CharField(max_length = 255)
  description = models.TextField()
  
  def __unicode__(self):
    return self.name
  

class Journal(models.Model):
  journal_type = models.ForeignKey(JournalType)
  name = models.CharField(max_length = 255)
  code = models.CharField(max_length = 255)
  
  def __unicode__(self):
    return self.name
  
    
class Transaction(models.Model):
  datetime = models.DateTimeField(auto_now = True, auto_now_add = True)
  account = models.ForeignKey(Account)
  amount = models.DecimalField(max_digits = 1000, decimal_places = 4, default = 0)
  particulars = models.TextField()
  posted = models.BooleanField(default = False)
  debit = models.BooleanField(default = True)
  user = models.ForeignKey(User, default = 0)
  
  def __unicode__(self):
    return "%s %s %f" % (self.datetime, self.account, self.amount)