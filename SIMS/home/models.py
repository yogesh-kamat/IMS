from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Supplier(models.Model):
	sname			= models.CharField(max_length=255, unique=True)
	contact			= models.CharField(max_length=255)
	address			= models.TextField(max_length=255)

	def __str__(self):
		return self.sname


class Inventory(models.Model):
	pname			= models.CharField(max_length=255)
	quantity		= models.PositiveIntegerField()
	measurement		= models.CharField(max_length=255)
	orginal_price	= models.PositiveIntegerField()
	profit			= models.PositiveIntegerField()
	selling_price	= models.PositiveIntegerField()
	supplier 		= models.ForeignKey(Supplier, on_delete=models.CASCADE)

	def __str__(self):
		return self.pname


class Transaction(models.Model):
	cust_name		= models.CharField(max_length=255)
	pid 			= models.ForeignKey(Inventory, on_delete=models.CASCADE)
	quantity_r		= models.PositiveIntegerField()
	success			= models.BooleanField(default=False)
	uid				= models.ForeignKey(User, on_delete=models.CASCADE)

	def actual_price(self):
		return int(self.quantity_r) * int(self.pid.selling_price)


class SupplierProductCostView(models.Model):
	id				= models.PositiveIntegerField(primary_key=True)
	sname		 	= models.CharField(max_length=255)
	price    		= models.PositiveIntegerField()

	class Meta:
		db_table 	= 'home_supplierproductcostview'
		managed 	= False
	
	def __str__(self):
		return str(self.id) + ' ' + self.sname + ' ' + str(self.price)