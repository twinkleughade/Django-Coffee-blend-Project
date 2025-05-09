from django.shortcuts import render
from .models import student,Items


# Create your views here.
def base(request):
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def home1(request,pk):
    userdata=student.objects.get(id=pk)
    userdata={
        "id":userdata.id,
        "name":userdata.stu_name,
        "contact":userdata.stu_contact,
        "email":userdata.stu_email,
        "dob":userdata.stu_dob,
        "gender":userdata.stu_gender,
        "pass":userdata.stu_pass, 
    }
    return render(request,'home.html',{'userdata':userdata})

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def service(request):
    return render(request,'service.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def order_online(request):
    return render(request,'menu.html')

def registration(request):
    print('registration page')
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    username=request.POST.get('username')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    print(username,email,phone,dob,gender,password,cpassword)

    user=student.objects.filter(stu_email=email)
    if user:
        msg="Email already exist"
        return render(request,'register.html',{'key':msg})
    else:
        if password==cpassword:
            student.objects.create(stu_name=username,stu_email=email,stu_contact=phone,stu_dob=dob,stu_gender=gender,stu_pass=password)
            msg="Registration done"
            return render(request,'login.html',{'key1':msg})
        else:
            msg1="password and confirm password not matched"
            return render(request,'register.html',{'key':msg1})
        

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user=student.objects.filter(stu_email=email)
        if user:
            userdata=student.objects.get(stu_email=email)
            # print(userdata.stu_name)
            # print(userdata.stu_email)
            pass1=userdata.stu_pass
            if passw==pass1:
                dmsg="Welcome to Dashboard"
                userdata={
                    "id":userdata.id,
                    "name":userdata.stu_name,
                    "contact":userdata.stu_contact,
                    "email":userdata.stu_email,
                    "dob":userdata.stu_dob,
                    "gender":userdata.stu_gender,
                    "pass":userdata.stu_pass, 
    }
                return render(request,'dashboard.html',{"userdata":userdata})
            else:
                msg="email and password not matched"
                return render(request,'login.html',{'msg':msg,'email':email})
        else:
            msg="email not registered"
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
# def dashboard_view(request):
#     table_data = [
#         {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
#         {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'},
#     ]
#     return render(request, 'dashboard/dashboard.html', {'table_data': table_data})




def dashboard(request):
    return render(request,'dashboard.html')

def first(request):
    data=Items.objects.all()[0:5]
    return render(request,'dashboard.html',{'data':data})

def asc(request):
    data=Items.objects.order_by('name')
    return render(request,'dashboard.html',{'data':data})

def last_5(request):
    data=Items.objects.order_by('-name')[0:5]
    return render(request,'dashboard.html',{'data':data})

def desc(request):
    data=Items.objects.order_by('-name')
    return render(request,'dashboard.html',{'data':data})

def all(request):
    data=Items.objects.all()
    return render(request,'dashboard.html',{'data':data})





   

