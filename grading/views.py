from django.shortcuts import render
from .models import Enrollement, Session
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def search_form(request):
    sessions = Session.objects.all()
    
    return render(request, 'search_form.html', {'sessions':sessions})

@login_required      
def search(request):
        semester = request.GET['semester']
        session = request.GET['session']
        
        _session = Session.objects.get(tag__iexact=session)
        
        enrollement = Enrollement.objects.filter(session=_session).filter(semester=semester).filter(student=request.user)
        tcu = enrollement.aggregate(Sum('course__units'))

        tgp = 0
        for enroll in enrollement:
                tgp += enroll.grade_point()

        gpa = tgp/tcu['course__units__sum']

        return render(request, 'search_results.html', 
                      {'enrollement': enrollement, 'session':session, 'semester':semester, 'tgp':tgp, 'gpa':gpa, 'tcu':tcu['course__units__sum']})