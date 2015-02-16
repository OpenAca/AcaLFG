from board.models import Audition, UserLFG
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.views.decorators.http import require_GET
from django.shortcuts import render
from board.models import UserLFG
from board.forms import LfgForm

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

def new_member(request):
  lfg_form = LfgForm()
  return render(request, 'new_member.html', {'lfg_form': lfg_form})

def new_audition(request):
  audition_form = AuditionForm()
  return render(request, 'new_audition.html', {'audition_form': audition_form})
