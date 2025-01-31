from django.shortcuts import render
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import re
from django.http import HttpResponse

from user.models import userregistermodel
from party.models import Party, BallotBox

def index(request):
    return render(request, "index.html")

def home(request):
    return index(request)

def userloginpage(request):
    return render(request, "userloginpage.html")

def userregister(request):
    return render(request, "userregisterpage.html")

def voterloginpage(request):
    return render(request, "voterloginpage.html")

def adminloginpage(request):
    return render(request, "adminloginpage.html")

def adminloginaction(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['password']
        if uname == 'Admin' and passwd == 'Admin':
            data = userregistermodel.objects.all() 
            return render(request, "admin/adminhome.html", {'data': data})
        else:
            messages.success(request, 'Incorrect Details')
            return render(request, "adminloginpage.html")
    else:
        return render(request, "adminloginpage.html")
    
def validate_voter_id(voter_id):
    pattern = r'^[A-Z]{2}\d{10}$'
    if re.match(pattern, voter_id):
        return True
    else:
        return False
    
def userregisteraction(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        voter_id = request.POST.get('voter_id')
        if not validate_voter_id(voter_id):
            return HttpResponse("Invalid Voter ID")

        fs = FileSystemStorage()
        rimage = request.FILES['profile_pic']
        filename1 = fs.save(rimage.name, rimage)
        uploaded_file_url1 = fs.url(filename1)

        print(uname, passwd, email, phone, uploaded_file_url1)
        userregistermodel.objects.create(username=uname, email=email, password=passwd, phone=phone, profile_pic=uploaded_file_url1, voter_id=voter_id, status='waiting')
        return render(request, "userloginpage.html")
    else:
        return render(request, "userregisterpage.html")
    
def adminlogout(request):
    return render(request, "adminloginpage.html")

def adminvoterdetails(request):
    data = Party.objects.all()
    return render(request, "admin/adminvoterdetails.html", {'data': data})

def adminuserdetails(request):
    data = userregistermodel.objects.all() 
    return render(request, "admin/adminhome.html", {'data': data})

def AdminActiveUsers(request):
    uid = request.GET.get('uid')
    userregistermodel.objects.filter(id=uid).update(status='Activated')
    data = userregistermodel.objects.all() 
    return render(request, "admin/adminhome.html", {'data': data})

def AdminActiveparty(request):
    uid = request.GET.get('uid')
    Party.objects.filter(id=uid).update(status='Activated')
    data = Party.objects.all()
    return render(request, "admin/adminvoterdetails.html", {'data': data})

def adminviewvotes(request):
    uid = request.GET.get('uid')
    print(uid)
    total_votes = BallotBox.objects.filter(partyleader=uid).count()
    data = BallotBox.objects.get(partyleader=uid)
    data1 = Party.objects.get(leader=uid)
    return render(request, "admin/adminviewvotes.html", {'data': data, 'data1': data1, 'total_votes': total_votes})