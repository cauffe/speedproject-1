from django.shortcuts import render, render_to_response

# Create your views here.
from main.models import SpeedModel, CustomUser
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


#pagination
from django.core.paginator import Paginator, InvalidPage, EmptyPage


from main.forms import SpeedModelForm, SpeedModelForm2, SpeedModelUpdateForm, UserSignUp, UserLogIn

def detail_view(request, pk):

    speed_object = SpeedModel.objects.get(pk=pk)

    context = {}

    context['speed_object'] = speed_object

    return render_to_response('detail_view.html', context, context_instance=RequestContext(request))


def list_view(request):

    context = {}

    speed_objects = SpeedModel.objects.all()
    paginator = Paginator(speed_objects, 4)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        speed_objects = paginator.page(page)
    except (InvalidPage, EmptyPage):
        speed_objects = paginator.page(paginator.num_pages)

    
    context['speed_objects'] = speed_objects

    return render_to_response('list_view.html', context, context_instance=RequestContext(request))

@login_required
def create_view1(request):

    context = {}

    form = SpeedModelForm()
    context['form'] = form

    if request.method == 'POST':
        form = SpeedModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/list_view/')

        else:
            context['errors'] = form.errors

    return render_to_response('create_view1.html', context, context_instance=RequestContext(request))

@login_required
def create_view2(request):

    context = {}

    form = SpeedModelForm2()
    context['form'] = form

    if request.method == 'POST':
        form = SpeedModelForm2(request.POST, request.FILES)

        if form.is_valid():

            print form.cleaned_data

            title = form.cleaned_data['title']
            info = form.cleaned_data['info']
            image = form.cleaned_data['image']
            user = CustomUser.objects.get(pk=request.user.pk)

            new_object = SpeedModel()

            new_object.title = title
            new_object.info = info
            new_object.image = image
            new_object.user = user

            new_object.save()

            return HttpResponseRedirect('/list_view/')
        else:
            context['errors'] = form.errors

    return render_to_response('create_view2.html', context, context_instance=RequestContext(request))


@login_required
def update_view(request, pk):

    context = {}

    speed_object = SpeedModel.objects.get(pk=pk)

    if request.user.pk != speed_object.user.pk:
        return HttpResponseRedirect('/list_view')

    context['speed_object'] = speed_object

    form = SpeedModelForm2()

    context['form'] = form

    if request.method == 'POST':
        form = SpeedModelUpdateForm(request.POST, request.FILES)
        print "request is post"

        if form.is_valid():
            print "form is valid"

            speed_object.title = form.cleaned_data['title']
            speed_object.info = form.cleaned_data['info']

            print form.cleaned_data['image']

            if form.cleaned_data['image'] != None:
                speed_object.image = form.cleaned_data['image']
            
            speed_object.save()

            return HttpResponseRedirect('/update_view/%s/' % pk)

        else:
            context['errors'] = form.errors

    return render_to_response('update_view.html', context, context_instance=RequestContext(request))

@login_required
def delete_view(request, pk):

    speed_object = SpeedModel.objects.get(pk=pk)

    if speed_object.user.pk != request.user.pk:
        return HttpResponseRedirect('/list_view/')
    else:
        speed_object.delete()

    return HttpResponseRedirect('/list_view/')


def signup(request):

    context = {} 

    form = UserSignUp()

    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            email = None

            new_user = CustomUser.objects.create_user(username, email, password)

            auth_user = authenticate(username=username, password=password)


            login(request, auth_user)

            return HttpResponseRedirect('/list_view/')

    return render_to_response('signup.html', context, context_instance=RequestContext(request))

@login_required
def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/list_view/')


def login_view(request):

    context = {}

    form = UserLogIn()

    context['form'] = form

    if request.method == 'POST':
        form = UserLogIn(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)

            login(request, auth_user)

            return HttpResponseRedirect('/list_view/')

    return render_to_response('login.html', context, context_instance=RequestContext(request))


def vote(request, pk):

    user = CustomUser.objects.get(pk=request.user.pk)

    vote_type = request.GET.get('vote_type', None)

    speed_object = SpeedModel.objects.get(pk=pk)

    print speed_object.up_votes.count()

    print speed_object.down_votes.count()

    print vote_type

    if vote_type == 'up':
        speed_object.up_votes.add(user)
        
        try:
            speed_object.down_votes.get(pk=request.user.pk)
            speed_object.down_votes.remove(user)
        except Exception, e:
            print e

        speed_object.save()

    elif vote_type == 'down':
        speed_object.down_votes.add(user)
        try:
            speed_object.up_votes.get(pk=request.user.pk)
            speed_object.up_votes.remove(user)
        except Exception, e:
            print e

        speed_object.save()

    return HttpResponseRedirect('/list_view/')

    return HttpResponse("%s, %s" % (speed_object.up_votes, speed_object.down_votes))




