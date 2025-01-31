from django.shortcuts import render
from party.models import Party
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def partyregisteration(request):
    if request.method == 'POST':
        name = request.POST['uname'] 
        fs = FileSystemStorage()
        rimage = request.FILES['profile_pic']
        filename1 = fs.save(rimage.name, rimage)
        uploaded_file_url1 = fs.url(filename1)

        leader = request.POST['lname']
        foundation_date = request.POST['calendar']
        email = request.POST['email'] 
        password = request.POST['password'] 
        phone = request.POST['phone'] 
        print(name, uploaded_file_url1, leader, foundation_date, email, password, phone)
        Party.objects.create(name=name, symbol=uploaded_file_url1, leader=leader, foundation_date=foundation_date, email=email, password=password, status='waiting', phone=phone)
        messages.success(request, 'Registered successfully')
        return render(request, "party/partyregister.html")
    else:
        messages.success(request, 'Registered Un-successfully')
        return render(request, "party/partyregister.html")
    
def partyregister(request):
    return render(request, "party/partyregister.html")

def partyloginaction(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        spasswd = request.POST.get('password')
        try:
            check = Party.objects.get(email=sname, password=spasswd)
            status = check.status
            if status == 'Activated':
                messages.success(request, 'Login Successful')
                return render(request, "party/partyhome.html")
            else:
                return render(request, "voterloginpage.html")
        except:
            return render(request, "voterloginpage.html")
    else:
        return render(request, "voterloginpage.html")