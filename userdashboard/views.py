from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from userdashboard.models import Profile, Referral, User, Verification
# Create your views here.
price_for_referral = 25
@login_required(login_url='/accounts/login')
def dashboard (request):
    user = User.objects.get(username = request.user.username)
    
    if not Profile.objects.filter(user= user.id):
        return redirect('/user/general')
    
    profile = Profile.objects.get(user=user)
    kyc_verified = 1
    if not Verification.objects.filter(user= user.id):
        kyc_verified = 0
    
    context = {
        'kyc_verified': kyc_verified,
        'profile':profile,
        'user':user
    } 
    return render(request, 'users/dashboard.html',context)

@login_required(login_url='/accounts/login')
def general (request):
    user = User.objects.get(username = request.user.username)
    profile = None
    if Profile.objects.filter(user= user.id):
        profile = Profile.objects.get(user=user.id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        image = request.FILES.get('image')
        
        referred_by = request.POST['referred_by']
        try:
            referred_user = User.objects.get(username=referred_by)
        except User.DoesNotExist:
            referred_user = None
        profile = Profile.objects.create(user=user,first_name=first_name,last_name=last_name,profile_image=image)
        profile.save()
        
        if referred_user:
            profile = Profile.objects.get(user=referred_user)
            referral = Referral.objects.create(profile=profile,username=request.user.username)
            
            profile.referral_people += 1
            profile.referral_price = price_for_referral * profile.referral_people
            profile.save()
            referral.save()
    return render(request, 'users/general.html',{'profile':profile})

@login_required(login_url='/accounts/login')
def mywallet (request):
    user = User.objects.get(username = request.user.username)
    
    if not Profile.objects.filter(user= user.id):
        return redirect('/user/general')
    
    profile = Profile.objects.get(user=user)
    context = {
        'profile':profile
    }
    
    return render(request, 'users/mywallet.html',context)

@login_required(login_url='/accounts/login')
def verification (request):
    user = User.objects.get(username = request.user.username)
    
    if not Profile.objects.filter(user= user.id):
        return redirect('/user/general')
    
    profile = Profile.objects.get(user=user)
    context = {
        'profile':profile
    }
    if request.method == 'POST':
        user =  User.objects.get(username = request.user.username)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        phone_number =request.POST['phone_number']
        day_of_birth  = request.POST['day']
        month_of_birth = request.POST['month']
        year_of_birth = request.POST['year']
        document_uploaded = request.POST['document_uploaded']
        serial_number  = request.POST['serial_number']
        year_issued = request.POST['year_issued']
        verify_document = request.FILES.get('upload_document')
        
        verify = Verification.objects.create(user=user,first_name=first_name,last_name=last_name,country=country,phone_number=phone_number,day_of_birth=day_of_birth,month_of_birth=month_of_birth,year_of_birth=year_of_birth,year_issued=year_issued,verify_document=verify_document,serial_number=serial_number,document_uploaded=document_uploaded)
        
        verify.save()
        
        return redirect('/user/dashboard')
    return render(request, 'users/verification.html',context)

@login_required(login_url='/accounts/login')
def spotTrading (request):
    user = User.objects.get(username = request.user.username)
    
    if not Profile.objects.filter(user= user.id):
        return redirect('/user/general')
    
    profile = Profile.objects.get(user=user)
    context = {
        'profile':profile
    }
    return render(request, 'users/spottrading.html',context)

@login_required(login_url='/accounts/login')
def contractTrading (request):
    user = User.objects.get(username = request.user.username)
    
    if not Profile.objects.filter(user= user.id):
        return redirect('/user/general')
    profile = Profile.objects.get(user=user)
    context = {
        'profile':profile
    }
    return render(request, 'users/contracttrading.html',context)

@login_required(login_url='/accounts/login')
def security (request):
    user = User.objects.get(username = request.user.username)
    
    if not Profile.objects.filter(user= user.id):
        return redirect('/user/general')
    profile = Profile.objects.get(user=user)
    context = {
        'profile':profile
    }
    return render(request, 'users/security.html',context)

@login_required(login_url='/accounts/login')
def general_update(request):
    if request.method == 'POST':
        user = User.objects.get(username = request.user.username)
        
        if not Profile.objects.filter(user= user.id):
            return redirect('/user/general')
        
        profile = Profile.objects.get(user=user)
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        image = request.FILES.get('image')
    
        profile.first_name = first_name
        profile.last_name = last_name
        profile.profile_image = image
        
        profile.save()
        
        return redirect('/user/general')
    return redirect('/user/general')