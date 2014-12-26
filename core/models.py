from django.db import models
# Create your models here.
 

class PartnerType(models.Model):
  name = models.CharField(max_length = 255)
  description = models.CharField(max_length = 255)
  
  def __unicode__(self):
    return self.name
  
  
class Partner(models.Model):
  partner_type = models.ForeignKey(PartnerType)
  name = models.CharField(max_length = 255)
  id_number = models.CharField(max_length = 255)
  insurance_number = models.CharField(max_length = 255)
  city = models.CharField(max_length = 255)
  address = models.CharField(max_length = 255)
  state = models.CharField(max_length = 255)
  zip = models.CharField(max_length = 255)
  phone = models.CharField(max_length = 255)
  fax = models.CharField(max_length = 255)
  email = models.CharField(max_length = 255)
  
  def __unicode__(self):
    return self.name
  

class User(models.Model):
  partner = models.ForeignKey(Partner)
  username = models.CharField(max_length = 255)
  password = models.CharField(max_length = 255)
  active = models.BooleanField(default = True)

  def __unicode__(self):
    return self.username