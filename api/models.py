from django.db import models

# Create your models here.
class Application(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        
    )
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.IntegerField()
    companyname = models.CharField(max_length=150)
    company_logo = models.ImageField(upload_to='companylogo/')
    team_background_details = models.TextField()
    company_and_product_details = models.TextField()
    problem = models.TextField()
    
    is_approved = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS, default='New')
    
    created_date    = models.DateTimeField(auto_now_add=True , null=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.companyname
    
    
    
    
