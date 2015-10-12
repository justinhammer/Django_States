from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from main.models import State, City, StateCapital
from django.template import RequestContext
from main.forms import ContactForm, CityEditForm, StateCreateForm, StateEditForm, CityCreateForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# list views
# detail views
# create view
# edit view
# delete view
# make the view --> make the url


def state_list(request):

    context = {}

    states = State.objects.all().order_by('name')

    context['states'] = states

    # template -> context dictionary -> context_instance variable
    return render_to_response('state_list.html', context, context_instance=RequestContext(request))


def state_detail(request, pk):
    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))


def state_search(request):

    context = {}

    context['request'] = request

    state = request.GET.get('name', None)

    if state != None:
        states = State.objects.filter(name__icontains=state)

        context['states'] = states

    return render_to_response('state_search.html', context, context_instance=RequestContext(request))


def state_create(request):

    context = {}

    form = StateCreateForm()

    context['form'] = form

    if request.method == 'POST':
        form = StateCreateForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            abbrev = form.cleaned_data['abbrev']

            form.save()
            return redirect('/state_list/')

        else:
            context['name'] = form.errors
    elif request.method == 'GET':
        form = StateCreateForm()
        context['form'] = form

    return render_to_response('state_create.html', context, context_instance=RequestContext(request))


def state_edit(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    form = StateEditForm(request.POST or None, instance=state)

    context['state'] = state
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('state_edit.html', context, context_instance=RequestContext(request))


def state_capital_detail(request, pk):

    context = {}

    statecapital = StateCapital.objects.get(pk=pk)

    context['statecapital'] = statecapital

    return render_to_response('state_capital_detail.html', context, context_instance=RequestContext(request))


def city_list(request):

    context = {}

    cities = City.objects.all()

    context['cities'] = cities

    return render_to_response('city_list.html', context, context_instance=RequestContext(request))


def city_detail(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city

    return render_to_response('city_detail.html', context, context_instance=RequestContext(request))


def city_search(request):

    context = {}

    context['request'] = request

    city = request.GET.get('city', None)

    if city != None:
        cities = City.objects.filter(city__contains=city)

        context['cities'] = cities

    return render_to_response('city_search.html', context, context_instance=RequestContext(request))


def city_edit(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    form = CityEditForm(request.POST or None, instance=city)

    context['city'] = city
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirct('/city_list/')

    return render_to_response('city_edit.html', context, context_instance=RequestContext(request))


def city_create(request):

    context = {}

    form = StateCreateForm()

    context['form'] = form

    if request.method == 'POST':
        form = CityCreateForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            county = form.cleaned_data['county']
            latitude = form.cleaned_data['lat']
            longitude = form.cleaned_data['lon']
            state_id = form.cleaned_data['state']

            form.save()
            return redirect('/city_search/')

        else:
            context['city'] = form.errors
    elif request.method == 'GET':
        form = CityCreateForm()
        context['form'] = form

    return render_to_response('city_create.html', context, context_instance=RequestContext(request))

    # if request.method == 'POST':
    #     city = request.POST.get('city', None)
    #     zip_code = request.POST.get('zip_code', None)
    #     county = request.POST.get('county', None)
    #     latitude = request.POST.get('latitude', None)
    #     longitude = request.POST.get('longitude', None)
    #     state_id = request.POST.get('state', None)

    #     if state_id != None:
    #         state = State.objects.get(pk=state_id)
    #     else:
    #         state = State.objects.get(name='Texas')

    #     the_city, created = City.objects.get_or_create(city=city)
    #     the_city.county = county
    #     the_city.zip_code = zip_code
    #     the_city.latitude = latitude
    #     the_city.longitude = longitude
    #     the_city.state = state

    #     the_city.save()


    #     context['created'] = 'Operation Successful'

    # elif request.method == 'GET':
    #     print "it was a GET request"


    # return render_to_response('city_create.html', context, context_instance=RequestContext(request))


def contact_view(request):

    context = {}

    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('STATES SITE MESSAGE FROM %s' % name,
                    message,
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False)
            context['message'] = "email sent"

        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form

    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))



