# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Payment(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Payment"
        verbose_name_plural  = u"Payments"
        
class Software(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Software"
        verbose_name_plural  = u"Softwares"
        
class Currency(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name  = u"Currency"
        verbose_name_plural  = u"Currency"

class Casino(models.Model):
    name =  models.CharField(u'Title', max_length=50)
    rating = models.FloatField(u'Rating %')
    trust_score = models.IntegerField(u'Trust & Fairness Score', default=5)
    games_score = models.IntegerField(u'Games & Software Score', default=5)
    bonus_score = models.IntegerField(u'Bonuses & Promo Score', default=5)
    support_score = models.IntegerField(u'Customer Support Score', default=5)
    logo = ThumbnailerImageField(u'Casino Logo', upload_to="upload/img/logos/")
    image = ThumbnailerImageField(u'Gif Image', upload_to="upload/img/gifs/")
    link = models.CharField(u'Link', max_length=180)
    ankor = models.CharField(u'Anchor', max_length=50)
    adv1 = models.CharField(u'Promo1', max_length=50, blank=True, null=True)
    adv2 = models.CharField(u'Promo2', max_length=50, blank=True, null=True)
    adv3 = models.CharField(u'Promo3', max_length=50, blank=True, null=True)
    adv4 = models.CharField(u'Promo4', max_length=50, blank=True, null=True)
    description = models.TextField(u'Short description', max_length=300, blank=True, null=True)
    review = models.TextField(u'Review', max_length=3000, blank=True, null=True)
    bonus = models.IntegerField(u'Welcome bonus')
    limit = models.IntegerField(u'Bonus limit', null=True)
    mobile = models.BooleanField(u'Mobile', blank=True, null=True)
    live = models.BooleanField(u'Live chat', blank=True, null=True)
    fun = models.BooleanField(u'Free games', blank=True, null=True)
    games = models.IntegerField(u'Games count', blank=True, null=True)
    currency = models.ManyToManyField(Currency)
    soft = models.ManyToManyField(Software)
    pay = models.ManyToManyField(Payment, related_name='pays')
    withdraw = models.ManyToManyField(Payment, related_name='payout')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-rating']
        verbose_name  = u"Casino"
        verbose_name_plural  = u"Casinos"