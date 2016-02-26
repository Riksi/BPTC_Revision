from education.courses.models import Course, Module, Section, Progress
from django.contrib.auth.models import User

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

civil = Course.objects.get(id=2)
users = User.objects.all()

def db_write():
	for m in range(len(modules)):
		ml = Module(name = modules[m],module_no = no[m],course = civil)
		ml.save()
		for s in sections[m]:
			sc = Section(name=s,module=m)
			sc.save()


	for s in sections:
		sc = Section.objects.get(name = s)
		for u in users:
			p = Progress(section = sc, student = u)
			p.save()
db_write()