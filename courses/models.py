from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Please understand properly the following:
##The User field
##What on_delete=models.CASCADE does
##The ForeignKey relationship
##Please write brief summary of the findings below for future reference

"""
Remember to use the set_password() for setting password after creating
the user

The primary attributes of the default user are:

username
password
email
first_name
last_name


username
	Required. 30 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.

email
	Optional. Email address.


password
	Required. A hash of, and metadata about, the password. (Django doesn’t store the raw password.) Raw passwords can be arbitrarily long and can contain any character. See the password documentation.

date_joined
	A datetime designating when the account was created. Is set to the current date/time by default when the account is created.


on_delete=models.CASCADE is one of the possible results when the ForeignKey row is deleted. What this does is 

"""

class Course(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	students = models.ManyToManyField(User)


		#At point of enrolment all sections should be incomplete



#class Enrolment(models.Model):
	#course = models.ForeignKey(Course,on_delete=models.CASCADE)
	#student = models.ForeignKey(User,on_delete=models.CASCADE)"""


class Module(models.Model):
	name = models.CharField(max_length = 100)
	course = models.ForeignKey(Course,on_delete=models.CASCADE)
	module_no = models.IntegerField()

class Section(models.Model):
	name = models.TextField()
	module = models.ForeignKey(Module,on_delete=models.CASCADE)

class Question(models.Model): 
	question = models.TextField()
	answer = models.TextField()
	section = models.ForeignKey(Section,on_delete=models.CASCADE)
	
class Progress (models.Model):
	student = models.ForeignKey(User,on_delete=models.CASCADE)
	section = models.ForeignKey(Section,on_delete=models.CASCADE)
	completed =  models.BooleanField(default = False)



#When a section is marked complete by a student:
	#You get hold of that section's module
	#You add the student to its completed_by 
	#You get hold of all the sections which share that module 
	#and in whose completed_by this student appears. 

# Allocation of business between the HC & CC, the OO of the CPR & the duty of the ct to manage cases
	