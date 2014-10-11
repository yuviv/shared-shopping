from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Using Django's contrib.auth User model, adding shoppinglist to it
class Profile(models.Model):
	user = models.OneToOneField(User)
	shopping_list = models.ForeignKey('ShoppingList')

class ShoppingList(models.Model):
	name = models.CharField(max_length=200)
	num_of_people = models.IntegerField()

class Item(models.Model):
	name = models.CharField(max_length=200)
	quantity = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)

	#set appropriate choices for the status
	NEED = 'n'
	BOUGHT = 'b'
	STATUS_CHOICES = (
		(NEED, 'Need'),
		(BOUGHT, 'Bought')
	)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=NEED)

	num_people_split = models.IntegerField()
	shopping_list = models.ForeignKey('ShoppingList')
	bought_by = models.ForeignKey(User)

class IOU(models.Model):
	payer = models.ForeignKey(User, related_name='payer')
	receiver = models.ForeignKey(User, related_name='receiver')
	item = models.ForeignKey("Item")

	UNPAID = 'u'
	PAID = 'p'
	CONFIRMED = 'c'
	STATUS_CHOICES = (
		(UNPAID, 'Unpaid'),
		(PAID, 'Paid'),
		(CONFIRMED, 'Confirmed')
	)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=UNPAID)