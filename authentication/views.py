from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        fname = lname = email = password = cpassword = error = ""
        context = {
            'fname':fname,
            'lname':lname,
            'email':email,
            'password':password,
            'cpassword':cpassword,
            'error': error,
        }
        try:
            if request.method == 'POST':
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                password = request.POST['password']
                cpassword = request.POST['cpassword']
                context['fname'] = fname
                context['lname'] = lname
                context['email'] = email
                context['password'] = password
                context['cpassword'] = cpassword
                if fname != "" and lname != "" and email != "" and password != "" and cpassword != "":
                    if password == cpassword:
                        if User.objects.filter(email = email).exists():
                            error = "User already exists with the given email"
                            print(error)
                            context['error'] = error
                            return redirect('signup', context)
                        else:
                            username = email
                            user = User.objects.create_user(first_name = fname, last_name = lname, email = email, password = password, username = username)
                            user.save()
                            fname = lname = email = password = cpassword = error = ""
                            error = "User registration successful. Now login to your account"
                            print(error)
                            context['error'] = error
                            newUser = auth.authenticate(username = username, password = password)
                            auth.login(request, newUser)
                            return redirect('home')
                    else:
                        error = "Passwords do not match. please check them"
                        print(error)
                        context['error'] = error
                        return redirect('signup', context)
                else:
                    error = "All fields are required"
                    print(error)
                    context['error'] = error
                    return redirect('signup', context)
        except:
            pass
    return render(request, 'authentication/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        email = password = error = ""
        context = {
            'email':email,
            'password':password,
            'error': error,
        }
        try:
            if request.method == "POST":
                email = request.POST['email']
                password = request.POST['password']
                context['email'] = email
                context['password'] = password
                if email != "" and password != "":
                    username = email
                    user = auth.authenticate(username = username, password = password)
                    print(user)
                    if user is not None:
                        auth.login(request, user)
                        print("Login Successful")

                        if request.GET.get('next', None):
                            print(request.GET.get('next'))
                            return redirect(request.GET['next'])
                        else:
                            return redirect('home')
                    else:
                        error = "Invalid credentials"
                        print(error)
                        context['error'] = error
                        return redirect('login', context)
                else:
                    error = "All fields are required"
                    print(error)
                    context['error'] = error
                    return redirect('login', context)
        except:
            pass
    return render(request, 'authentication/login.html', context)


@login_required(login_url='/authentication/login/')
def logout(request):
    auth.logout(request)
    return redirect('home')