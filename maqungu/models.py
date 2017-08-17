from __future__ import unicode_literals
from django.core.validators import RegexValidator

from django.db import models

# Create your models here.

class Client(models.Model):
	Name = models.CharField(max_length=50)
	Surname = models.CharField(max_length=50)
	Id_Number = models.CharField(primary_key=True, max_length=13, validators=[RegexValidator(r'^\d{1,13}$')])
	Employer = models.CharField(max_length=50, default="")
	Employee_Number = models.CharField(max_length=20, default=00000000000, validators=[RegexValidator(r'^\d{1,20}$')])
	Income = models.DecimalField(max_digits=8, default=00.00, decimal_places=2)
	Premium = models.DecimalField(max_digits=8, default=00.00, decimal_places=2)
	Policy_Chooses = (
		('Investment', 'investment'), 
		('retirement', 'retirement'),
		('funeral cover', 'funeral cover'),

	)	
	Policy_type = models.CharField(max_length=99, default="", choices = Policy_Chooses)
	Street = models.CharField(max_length=50)
	City = models.CharField(max_length=50)
	Postal_Code = models.CharField(max_length=50)
	Cell_Number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
	Created = models.DateTimeField(auto_now_add=True)

    
