from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="static/img")

class Invoice(models.Model):
    cust_name = models.CharField(max_length=110, default="")
    cust_no = models.CharField(max_length=13, unique=True, default="")
    addr = models.TextField(max_length=500,default="")
    del_addr = models.TextField(max_length=500,default="")
    tot_amt = models.IntegerField(blank=True, default=0)
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('notpaid', 'Not Paid')
    )
    pay_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='paid')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.cust_name


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='inv_dtl', default="")
    product = models.CharField(max_length=110, default="")
    quty = models.IntegerField(blank=True, default=0)
    price = models.IntegerField(blank=True, default=0)
    net_amt = models.IntegerField(blank=True, default=0)
