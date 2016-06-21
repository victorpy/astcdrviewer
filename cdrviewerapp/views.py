from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from tables import TrunksAccountcodesTable,PaymentsTable,RateTable,CdrTable,RatedCdrTable
from models import TrunksAccountcodes,Payments,Rate,Accounts,Cdr,RatedCdr
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

#add_to_builtins('eztables.templatetags.eztables')

def hello(request):
	return HttpResponse('Hello world')

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)		
                return HttpResponseRedirect('/index/')
	else:
	     state = "Usuario o clave incorrecto."

    return render_to_response('login.html', {'state':state, 'username': username} ,context_instance=RequestContext(request))

def logout_user(request):
	state = "Usuario deslogueado del sistema..."
	logout(request)
	return render_to_response('login.html', {'state':state}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def index(request):
	#t_array = Ticket.objects.filter(token=request.POST['typed_id']).order_by('-start_date')
	accounts = Accounts.objects.filter(username=request.user.username)
	
	if len(accounts) >= 1:
                account = accounts[0]
        else:
                return render(request, 'accounterror.html')

	credit = account.credit
	extension = account.extension

        return render(request,'index.html', {'username':request.user.username, 'credit': credit, 'email':request.user.email, 'extension': extension})

def cdtime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})

@login_required(login_url='/login/')
def incalls(request):
	accounts = Accounts.objects.filter(username=request.user.username)
        if len(accounts) >= 1:
                account = accounts[0]
        else:
                return render(request, 'accounterror.html')

	extension = account.extension	
	
	calls = CdrTable(Cdr.objects.filter(dst=extension).order_by('-calldate'))
	return render(request,'incalls.html',{'calls': calls});

@login_required(login_url='/login/')
def outcalls(request):
        accounts = Accounts.objects.filter(username=request.user.username)
        if len(accounts) >= 1:
                account = accounts[0]
        else:
                return render(request, 'accounterror.html')

        acode = account.account_code

        calls = CdrTable(Cdr.objects.filter(accountcode=acode).order_by('-calldate'))
        return render(request,'outcalls.html',{'calls': calls});

@login_required(login_url='/login/')
def payments(request):
	accounts = Accounts.objects.filter(username=request.user.username)
	if len(accounts) >= 1:
                account = accounts[0]
        else:
                return render(request, 'accounterror.html')

	id_account = account.id_account		

	payments = PaymentsTable(Payments.objects.filter(id_account = id_account))
	return render(request,'payments.html',{'payments': payments});

@login_required(login_url='/login/')
def ratedcdrs(request):
        accounts = Accounts.objects.filter(username=request.user.username)
        if len(accounts) >= 1:
                account = accounts[0]
        else:
                return render(request, 'accounterror.html')

        accountcode = account.account_code
	extension = account.extension

        ratedcdrs = RatedCdrTable(RatedCdr.objects.filter(accountcode = accountcode).order_by('-calldate') | RatedCdr.objects.filter(dst = extension).order_by('-calldate')) 
        return render(request,'ratedcdrs.html',{'ratedcdrs': ratedcdrs});


@login_required(login_url='/login/')
def rates(request):

	accounts = Accounts.objects.filter(username=request.user.username)

        if len(accounts) >= 1:
                account = accounts[0]
        else:
                return render(request, 'accounterror.html')

	id_rate_group = account.id_rate_group
	
        rates = RateTable(Rate.objects.filter(id_rate_group=id_rate_group))

        return render(request,'rates.html',{'rates': rates});

