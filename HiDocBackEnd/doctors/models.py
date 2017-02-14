""" Doctor models.

In this document we have the necesary models for the doctors info.

"""
from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
	""" This class is the base model for the doctor infromation.

	.. todo::
		We need to make the necesary changes for blocking and unbluquind the unpaid acounts.
	.. todo::
		Make support for aditional acounts pointing to the same doctor user?
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.IntegerField()
	
