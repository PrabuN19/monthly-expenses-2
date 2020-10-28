from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class months(models.Model):
	name=models.CharField(max_length=100,unique=True)
	slug=models.SlugField(max_length=100,blank=True)
	customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)


	def save(self,*args,**kwargs):
		self.slug=slugify(self.name)
		super(months,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

	def total(self):
		price_list=item.objects.filter(month=self)
		total_price=0
		for prices in price_list:
			total_price+=prices.price
		return total_price




class item(models.Model):
	customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
	month=models.ForeignKey(months,on_delete=models.CASCADE,related_name='item')
	itemname=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	price=models.IntegerField()
	date=models.DateField()


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
