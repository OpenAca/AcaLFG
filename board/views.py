from board.models import Audition, UserLFG
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from board.models import UserLFG
from board.forms import AuditionForm, LfgForm

@require_GET
def home(request):
  return render(request, 'home.html', dictionary={'section': 'home'})

@require_GET
def view_member(request, member_id):
  try:
    m = UserLFG.objects.get(pk=member_id)
  except UserLFG.DoesNotExist:
    raise Http404('Member does not exist.')
  return render(request, 'view_member.html',
                dictionary={'section': 'members', 'member': m,
                            'maps_key': settings.GOOGLE_MAPS_API_KEY})

@require_GET
def member_list(request):
  paginator = Paginator(UserLFG.objects.all(), 20)
  page = request.GET.get('page')
  try:
    members = paginator.page(page)
  except PageNotAnInteger:
    members = paginator.page(1)
  except EmptyPage:
    members = paginator.page(paginator.num_pages)

  return render(request, 'member_list.html',
                dictionary={'members': members, 'section': 'members'})

@require_GET
def view_audition(request, audition_id):
  try:
    audition = Audition.objects.get(pk=audition_id)
  except Audition.DoesNotExist:
    raise Http404('Audition does not exist.')
  return render(request, 'view_audition.html',
                dictionary={'section': 'auditions',
                            'audition': audition,
                            'maps_key': settings.GOOGLE_MAPS_API_KEY})

@require_GET
def audition_list(request):
  paginator = Paginator(Audition.objects.all(), 20)
  page = request.GET.get('page')
  try:
    auditions = paginator.page(page)
  except PageNotAnInteger:
    auditions = paginator.page(1)
  except EmptyPage:
    auditions = paginator.page(paginator.num_pages)

  return render(request, 'audition_list.html',
                dictionary={'auditions': auditions,
                            'section': 'auditions'})

def new_listing(request):
  audition_form = None
  lfg_form = None
  if request.method == 'POST':
    form_type = request.POST.get('type')
    if form_type == 'lfg':
      lfg_form = LfgForm(request.POST)
      if lfg_form.is_valid():
        return render(request, 'new_success.html')
    elif form_type == 'audition':
      audition_form = AuditionForm(request.POST)
      if audition_form.is_valid():
        return render(request, 'new_success.html')
  else:
    form_type = None

  if not audition_form:
    audition_form = AuditionForm()
  if not lfg_form:
    lfg_form = LfgForm()
  return render(request, 'new_listing.html',
      dictionary={'audition_form': audition_form,
                  'lfg_form': lfg_form,
                  'form_type': form_type})
