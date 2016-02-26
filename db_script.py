from courses.models import Course, Module, Section, Progress, Question
from django.contrib.auth.models import User

"""modules = ['Allocation of business between courts, overriding objective, duty of court to manage cases',
'Limitation',
'Pre-action Conduct',
'Commencing Proceedings',
'Parties',
'Statements of Case']"""

no = [i for i in range(7,12)]

"""sections = [['the allocation of business between the High Court and County Courts',
'the overriding objective',
'the duty of the court to manage cases'
],
['accrual of causes of action',limitation periods in cases of tort, latent damage,
personal injury, fatal accident, contract, and contribution claims],
['the Practice Direction (Pre-Action Conduct)','consequences of non-compliance'],
['the Part 7 procedure',
'validity, extension and service of claim forms',
'service of other court documents within the jurisdiction',
'the Part 8 procedure' ],
['partnerships, sole traders, LLPs and companies, trusts and deceased persons',
'children and persons suffering from mental incapacity'
],
['claim forms and particulars of claim',
'acknowledgement of service, defences, replies, counterclaims',
'the effect of not responding to an allegation in a statement of case'
]
]"""

modules = [
'Claiming remedies in contract and tort',
'Multiple Causes of Action, Counterclaims and Other Additional Claims',
'Amendment',
'Further Information',
'Default Judgment and Summary Judgment'
]

no = [i for i in range(7,12)]

sections = [
['claiming damages for breach of contract and in tort',
'claiming equitable remedies',
'claims for misrepresentation',
'claiming interest on money remedies up to judgment'],
['multiple causes of action and multiple parties','counterclaims against the claimant or an additional party',
'contribution notices and claims against third parties and fourth parties'],
['permission or consent to amend','costs consequences of amendment'],
['requests for further information',
'responding to a request for further information' ],
['default judgments',
'applications to set aside',
'summary judgments'
]
]
#Module.objects.all().delete()
#Progress.objects.all().delete()

civil = Course.objects.get(id=2)
users = User.objects.all()

def save_modules():
	for m in range(len(modules)):
		ml = Module(name = modules[m],module_no = no[m],course = civil)
		ml.save()
		for s in sections[m]:
			print(s)
			sc = Section(name=s.capitalize(),module=ml)
			sc.save()


	for s in sections:
		for j in s:
			print(j)
			sc = Section.objects.get(name = j.capitalize())
			for u in users:
				p = Progress(section = sc, student = u)
				p.save()

question = 'Module %s, section %s. This is some long text that aims to represent a the typical length of a question. However some questions might be longer and others might be shorter'

answer = 'This is some long text that aims to represent a the typical length of an answer. Answers are generally somewhat longer than questions. In this particular course, however, most of the answers are fairly brief. But if a detailed explanation appears, then it will be longer. Actually this answer is probably not very long. Often answer is 5 or more times the length of the question, if not a great deal more.'

def add_questions(delete_all = False):
	if delete_all:
		Question.objects.all().delete()
	import random
	sections = Section.objects.all()
	for i in range(0,200):
		s = random.randint(0,len(sections)-1)
		mn = sections[s].module.module_no
		q_text = ''
		q = Question(question = question%(str(s),str(mn)), answer = answer, section = sections[s])	
		q.save()



