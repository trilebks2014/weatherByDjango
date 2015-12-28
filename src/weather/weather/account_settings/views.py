from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def settings(request):
    return redirect('/settings/profile/')
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, u'Your profile were successfully edited.')
            return redirect(r('settings:profile'))
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'settings/profile.html', { 'form': form })
@login_required
def picture(request):
    uploaded_picture = False
    try:
        if request.GET['upload_picture'] == 'uploaded':
            uploaded_picture = True
    except Exception, e:
        uploaded_picture = False
    return render(request, 'settings/picture.html', { 'uploaded_picture': uploaded_picture })

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, u'Password changed successfully.')
            update_session_auth_hash(request, form.user)
        else:
            messages.error(request, u'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'settings/password.html', { 'form' : form })
    
@login_required
def upload_picture(request):
    try:
        f = request.FILES['picture']
        ext = os.path.splitext(f.name)[1].lower()
        valid_extensions = ['.gif', '.png', '.jpg', '.jpeg', '.bmp']
        if ext in valid_extensions:
            filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + request.user.username + '_tmp.jpg'
            with open(filename, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            im = Image.open(filename)
            width, height = im.size
            if width > 560:
                new_width = 560
                new_height = (height * 560) / width
                new_size = new_width, new_height
                im.thumbnail(new_size, Image.ANTIALIAS)
                im.save(filename)
            return redirect('/settings/picture/?upload_picture=uploaded')
        else:
            messages.error(request, u'Invalid file format.')
    except Exception, e:
        messages.error(request, u'An expected error occurred.')
    return redirect('/settings/picture/')

