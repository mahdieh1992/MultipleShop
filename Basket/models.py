from django.db import models
from account.models import CustomUser
from product.models import product


class Discount(models.Model):
    DiscountName=models.CharField(max_length=10,unique=True)
    DiscountPercent=models.SmallIntegerField()
    Expiredate=models.DateTimeField(auto_now_add=False)
    Quantity=models.SmallIntegerField()

    def __str__(self):
        return f"{self.DiscountName}-{self.Quantity}"


class OrderUser(models.Model):
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Orderid')
    createDate=models.DateTimeField(auto_now_add=True)
    total=models.IntegerField()

    def __str__(self):
        return f"{self.userid.email}-{self.total}"


class Orderdetailuser(models.Model):
    orderid=models.ForeignKey(OrderUser,on_delete=models.CASCADE,related_name='OrderDtailid')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='OrderDtailid')
    productid=models.ForeignKey(product,on_delete=models.CASCADE,related_name='OrderDtailid')
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    price = models.IntegerField()
    total=models.IntegerField()
    createDate=models.DateField(auto_now_add=False,null=True)

    def __str__(self):

        return f"{self.user.email}{self.productid.title}"


