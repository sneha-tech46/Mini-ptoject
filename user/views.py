from django.shortcuts import render
from django.contrib import messages
from user.models import userregistermodel
from party.models import Party, BallotBox
from django.http import HttpResponse

import face_recognition
import cv2
cv2.useOpenVX()
import numpy
import re
from django.http import HttpResponse
import random
import yagmail

# Create your views here.
def userloginaction(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        spasswd = request.POST.get('password')
        print(sname, spasswd)
        try:
            check = userregistermodel.objects.get(email=sname, password=spasswd)
            status = check.status
            if status == 'Activated':
                request.session['user_id'] = check.id
                request.session['user_email'] = check.email
                request.session['user_voter_id'] = check.voter_id
                return render(request, "user/userfacedetect.html")
            else:
                return render(request, "userloginpage.html")
        except:
            return render(request, "userloginpage.html")
    else:
        return render(request, "userloginpage.html")

def userfacedetect(request):
    return render(request, "userfacedetect.html")

def facedetect(request):
    # Load images
    print("[INFO] quantifying faces...")
    image_1 = face_recognition.load_image_file("media/dataset/Akbar/pass photo.JPG")
    image_1_face_encoding = face_recognition.face_encodings(image_1)[0]
    print("read image successfully")

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        image_1_face_encoding,
    ]
    known_face_names = [
        "Akbar",
    ]

    # Initialize variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    match = 0  # Initialize match to ensure it exists before the comparison

    # Get a reference to webcam #0 (the default one)
    print("[INFO] starting video stream...")
    video_capture = cv2.VideoCapture(0)

    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = numpy.ascontiguousarray(small_frame[:, :, ::-1])

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        print("hi")
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        print("hi1")
        if True in matches:
            match = 1
            print("hi2")

    # Release the video capture when done
    video_capture.release()

    # Check for match and render the appropriate page
    if match == 1:
        print("detect")
        return render(request, "user/userhome.html")
    else:
        print("not detect")
        return render(request, "user/userfacedetect.html")


def validate_voter_id(voter_id):
    pattern = r'^[A-Z]{2}\d{10}$'
    if re.match(pattern, voter_id):
        return True
    else:
        return False

def uservoteridaction(request):
    global random_number
    if request.method == 'POST':
        voter_id = request.POST.get('voter_id')
        email = request.session['user_email']
        if not validate_voter_id(voter_id):
            return HttpResponse("Invalid Voter ID")
        else:
            ts = userregistermodel.objects.get(voter_id=voter_id, email=email)
            ts1 = ts.username
            try:
                random_number = random.randint(1000, 9999)
                print(random_number)
                user = "backendthe8@gmail.com"
                app_password = "rznx emrl sovz xefp"
                to = email
                subject = "One-Time-Password"
                content = f'''
                            <p>Dear {ts1},</p>
                            <p>Thank you for using our service Blockchain-Based E-Voting System.</p>
                            <p>Your one-time password {random_number}</p>
                            <p>Regards,</p>
                            <p>Team Blockchain-Based E-Voting System</p>
                            </table>
                            '''
                with yagmail.SMTP(user, app_password) as yag:
                    yag.send(to, subject, content)
                print("otp sent successfully")
                return render(request, "user/userotp.html")
            except:
                return render(request, "user/userotp.html")
    else:
        return render(request, "user/userotp.html")

def userotpaction(request):
    if request.method == 'POST':
        otp1 = int(request.POST.get('otp'))
        if otp1 == random_number:
            email = request.session['user_email']
            user = userregistermodel.objects.get(email=email)
            return render(request, "user/userhome.html", {'user': user})
        else:
            return render(request, "user/userotp.html")
    else: 
        return render(request, "user/userotp.html")

def userlogout(request):
    return render(request, "userloginpage.html")

def userpartiesselection(request):
    parties = Party.objects.all()
    return render(request, "user/userpartiesselection.html", {'data': parties})

def userprofile(request):
    email = request.session['user_email']
    user = userregistermodel.objects.get(email=email)
    return render(request, "user/userhome.html", {'user': user})


def uservoteparty(request):
    uid = request.GET.get('uid')
    parco = Party.objects.get(id=uid)
    partyleader = parco.leader
    partyname = parco.name

    voter = request.session['user_voter_id']

    if BallotBox.objects.filter(voter=voter).exists():
        message = "You have already voted."
        parties = Party.objects.all()
        return render(request, "user/userpartiesselection.html", {'data': parties, 'message': message})

    print(partyleader, partyname, voter)
    ballot_entry = BallotBox.objects.create(partyleader=partyleader, partyname=partyname, voter=voter)
    ballot_entry.save()

    parties = Party.objects.all()
    return render(request, "user/userpartiesselection.html", {'data': parties})
