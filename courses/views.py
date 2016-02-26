from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from .forms import LoginForm
from .models import Course, Module, Section, Question, Progress
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.db.models import Avg
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie

import random

#FUNCTIONALITY TO ADD
#Register
#Join a course
#Withdraw from a course
#SPECIFICALLY
#If not logged in,
#the welcome page contains a list of courses (and other information)
#It also contains links to login and register pages
#Subsequently use JS to create login and register modals 
#Course links:
#>Course description
#>Join course > Course welcome
#

#Change password



#Things to do

#Create the profile page

#Create a elementary get or post function for the 
#questions page
#What it should do is to update the 'completed' status 
#of each topic based on whether a box is checked
#It should also return a variable that indicates whether the module has been completed
#In case of the latter, the JavaScript should close the that tab
#ABOVE IS DONE

#NEXT:
#ADD USER AUTHENTICATION AND MODIFY THE URLS ONE AT A TIME




#Display progress and deadline on the questions page 

#Add more data to the database

#Incorporate login functionality

#Create welcome and course information pages 

#Add styling

#Add possibility of changing password

#Consider using JS libraries for views 

#Possibly incorporate a payments system


#SQL 
#Combine queries
#


#Create login page
#Apply authenticate_redirect to one view at a time (appropriately modifying url)

def test_ajax(request):
	return render(request,'courses/test_ajax_post.html',{})

#@ensure_csrf_cookie
def test_ajax_post(request):
	print('request', request)
	if request.method == "POST":
		print(request.POST)
		return JsonResponse({'it':'worked'})
	return HttpResponse('Got')

def user_login(request):
	if request.method == "POST":

		form = LoginForm()
		username = request.POST['uname']
		password = request.POST['pword']
		next = request.POST['next']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(next)
		return render(request,'courses/login.html',
								{'error' :'You have not correctly entered your email and/or password', 
								'next':next})
	else:
		next = reverse('welcome') 
		if 'next' in request.GET:
			next = (request.GET['next'])
		return render(request,'courses/login.html', {'error': '','next': next})

def user_logout(request):
	logout(request)
	print(request.user)
	return redirect('welcome')

def user_register(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			u = User.objects.create_user(username = username, password = password)
		 
			login(request, authenticate(username=username, password=password))
			return redirect('profile')
		return render(request,'courses/register.html',{'form': form})
	else:
		form = LoginForm()
		return render(request,'courses/register.html',{'form': form})
	return redirect('profile')

def welcome(request):
	return render(request,'courses/welcome.html',
		{'courses':Course.objects.all(), 'user':request.user})

def course_detail_page(request,course_id):
	#Default - go to first section
	#Otherwise go to last visited section (using cookies)
	user = request.user
	course = Course.objects.get(id = course_id)
	enrolled = course.students.filter(id = user.id)
	return render(request,'courses/course_detail.html',
					{'course':course, 'user':user, 
					'enrolled':enrolled})


def courses_page(request):
	user = request.user
	courses = Course.objects.all()
	course_data = [(course,len(course.students.filter(id = user.id))>0) for course in courses]
	return render(request,'courses/all_courses.html',
					{'course_data':course_data, 'user':user})

def authenticate_redirect(f):
	def _authenticate_redirect(request,**kwargs):
		if request.user.is_authenticated():
			return f(request,**kwargs)
		else:
			return redirect('%s?next=%s' % (reverse('login'), request.path))
	return _authenticate_redirect

@authenticate_redirect
def section_page(request,course_id,section_id):
	"""kwargs = {}
	kwargs['user'] = request.user
	modules = Module.objects.order_by('module_no')
	kwargs["sections"] = [(module,Progress.objects.filter(section__module = module, 
														student_id = kwargs['user'].id)) 
														for module in modules]
	kwargs["course"] = Course.objects.get(id = course_id)
	print(type(section_id)"""
	kwargs = get_course_links(request,course_id)
	if section_id:
		kwargs["this_section"] = Section.objects.get(id = section_id)
		kwargs["questions"] = Question.objects.filter(section = kwargs["this_section"])
	else:
		kwargs["this_section"] = kwargs["questions"] = None
	#completed = {module.id: Progress.objects.filter(module = module, student_id = user_id).aggregate(Avg('completed'))
	#print(completed) for module in modules}
	return render(request,'courses/questions.html',
				kwargs)

def get_course_links(request,course_id):
	kwargs = {}
	kwargs['user'] = request.user
	modules = Module.objects.order_by('module_no')
	sections = [Progress.objects.filter(section__module__course__id = course_id, section__module = module,
										student_id = kwargs['user'].id) for module in modules]
	if sum(len(i) for i in sections):
		kwargs["sections"] = [(modules[i], sections[i]) for i in range (len(modules))]
	else:
		kwargs["sections"] = []
	print(kwargs["sections"] )													
	kwargs["course"] = Course.objects.get(id = course_id)
	return kwargs




@authenticate_redirect
def section_completed(request, section_id):
	user = request.user	
	#sections = Progress.objects.filter(student_id = user_id)
	progress = Progress.objects.get(section_id = section_id, 
									student_id = user.id)	
	progress.completed = not(progress.completed)
	progress.save()
	module = progress.section.module
	completed = Progress.objects.filter(section__module = module, 
										student_id = user.id).aggregate(Avg('completed'))
	#print(completed)
	data = {"module_id": module.id, 
			"module_completed": completed['completed__avg'] == 1}
	return JsonResponse(data)

#View needs to get hold of the question corresponding to id and user_id
#Then needs to increment or decrement its rating based on whether or not question has 
#been flagged or not
#Need to have some way of indicating if the question has been flagged 

@authenticate_redirect
def test_yourself(request, course_id):
	kwargs = get_course_links(request,course_id)
	kwargs["this_section"] = kwargs["questions"] = None
	if request.method == "POST":
		print(request.POST)
		return HttpResponse(request.POST);
	print(request.GET)
	questions = {}
	this_module_no = -1
	kwargs['area'] = '> All topics'
	#weak_areas = False

	if request.GET:
		#num_req = int(request.GET['num_req'])
		questions = Question.objects.filter(section__module__course__id = course_id)
		if request.GET['module_no']:
			this_module_no = request.GET['module_no']
			questions = questions.filter(section__module__module_no = this_module_no)
			kwargs['area'] = '> Module %s'%(this_module_no,)
		"""if 'weak_areas' in request.GET:
			weak_areas = True
			#Get the num_req/max available most weak_areas
			num_req  = request.GET['num_req']
			questions = questions.filter"""
			#kwargs['areas'] += '(Weakest areas)'
		num_qs = len(questions)
		if num_qs > 10:
			#Get num_req random questions 
			q_inds = [i for i in range(0,num_qs)]
			print(q_inds)
			random.shuffle(q_inds)
			q_inds = q_inds[0:10]
			print(q_inds)
			questions = [questions[i] for i in q_inds]
		
	kwargs['questions'] = questions
	kwargs['this_section'] = 'test'
	kwargs['this_module_no']=int(this_module_no)

	
	#modules = Module.objects.filter(course__id = course_id)
	return render(request,'courses/questions.html',kwargs)
	"""return render(request,
				'courses/test_yourself.html', 
				{'modules':modules,
				'this_module_no':this_module_no,
				'num_req':num_req,
				#'weak_areas':weak_areas,
				'questions':questions,
				})"""
	


@authenticate_redirect
def progress_page(request, course_id):
	#Render the progress page template with just the user and course
	course = Course.objects.get(id = course_id)
	return render(request,
				'courses/progress.html',
				{'course':course})

@authenticate_redirect
def progress_data(request, course_id):
	#user = User.objects.get(id = user_id)
	user = request.user
	course = Course.objects.get(id = course_id)
	modules = Module.objects.all().order_by('module_no')
	user_progress = Progress.objects.filter(student = user,
											section__module__course = course).values(
											'section__module__name', 
											'section__module__module_no').annotate(
											progress = Avg('completed')).order_by('section__module__module_no')
	#test_urls = [reverse('test_yourself',kwargs={'course_id':course.id})+'?module_no=%s'%(m.module_no) for m in modules]										
	#data = serializers.serialize("json", Progress.objects.filter(student = user).values('module__name', 'module__module_no').annotate(progress = Avg('completed')))
	for i in range(len(user_progress)):

		user_progress[i].update({'test_url':reverse('test_yourself',
													kwargs={'course_id':course.id})+'?module_no=%s'%(modules[i].module_no)})

	user_progress_dict = {'user_progress_data': [i for i in user_progress],
							'root_url':reverse('test_yourself',kwargs={'course_id':course.id})+'?module_no=' }
	return JsonResponse(user_progress_dict)#safe = False)
	#return HttpResponse('Hello and welcome')=
	#Want equivalent of:
	"""'SELECT [all module attributes], AVG(completed) FROM progress, module WHERE progress.module = module.id GROUP BY module	ORDER BY module_no' """

	#Send a JSON response


#If new sections are added, all users in the course will be associated with the sections
#'behind the scenes'
#However users themselves can only join the course once 
@authenticate_redirect
def join_page(request, course_id):
	user = request.user
	course = Course.objects.get(id = course_id)
	if not course.students.filter(id = user.id): #ensures you can only enrol once
		sections = Section.objects.filter(module__course__id = course_id)
		for section in sections:
			p = Progress(student = user, section = section)
			p.save()
		course.students.add(user)
		return redirect('questions',course_id = course_id, section_id = '')
	else:
		return redirect('questions',course_id = course_id, section_id = '')

@authenticate_redirect
def withdraw_page(request, course_id):
	if request.method == 'POST':
		user = request.user
		course = Course.objects.get(id = course_id)
		if course.students.filter(id = user.id):
			sections = Section.objects.filter(module__course__id = course_id)
			for section in sections:
				p = Progress.objects.filter(student = user, section = section)
				p.delete()
			course.students.remove(user)
		return redirect('profile')
	else:
		return render(request,'courses/withdraw.html')



@authenticate_redirect
def profile_page(request):
	user = request.user
	error = ''
	if request.method=='POST':
		if user.check_password(request.POST['present-pword']):
			new = request.POST['new-pword']
			confirm = request.POST['confirm-pword']
			if new:
				if new == confirm:
					user.set_password(new)
					user.save()
				else:
					error = "Your passwords don't match"
			else:
				error = "Please enter a new password"
		else:
			error = "You have not entered the right password"
		
	#courses = Course.objects.filter(students = user)
	#completed = ([sum([Progress.objects.filter(
				#section__module__course = course, 
				#student = user).aggregate(
				#Avg('completed'))['completed__avg']])
				#for course in courses])
	#course_data = {(courses[i].name, courses[i].id, completed[i]*100) 
					#for i in range(0,len(courses))}
	return render(request,'courses/profile.html',
						{'user':user, #'course_data': course_data, 
						'error':error})

@authenticate_redirect
def forum_qs(request):
	return render(request,'courses/forum_qs.html',{'user':request.user})

@authenticate_redirect
def forum_ps(request):
	return render(request,'courses/forum_posts.html',{'user':request.user})