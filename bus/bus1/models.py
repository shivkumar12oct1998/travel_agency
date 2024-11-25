from django.db import models

class adminsidedetail(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    activities = models.CharField(max_length=100)
    guide_name = models.CharField(max_length=100)
    days = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class usersideinfo(models.Model):
    customer_name = models.CharField(max_length=100)
    image1 = models.ImageField()
    travel_date = models.DateField()
    package = models.ForeignKey('adminsidedetail', on_delete=models.CASCADE)  # Remove null=True
    number_of_people = models.IntegerField(default=0)
    mobile_number = models.IntegerField(default=0)
    customer_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.customer_name


    def __str__(self):
        return self.customer_name

