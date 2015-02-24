import base64
import uuid

from board.models import Audition, UserLFG
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_GET
from django.views.generic.edit import DeleteView
from django.shortcuts import render
from board.models import Audition, UserLFG
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
def view_member_by_verification(request, verification_id):
  try:
    m = UserLFG.objects.get(verification_id=verification_id)
  except UserLFG.DoesNotExist:
    raise Http404('Member does not exist.')

  if not m.is_verified:
    m.is_verified = True
    m.save()

  return render(request, 'view_member.html',
                dictionary={'section': 'members', 'member': m,
                            'maps_key': settings.GOOGLE_MAPS_API_KEY,
                            'verification_id': verification_id})

@require_GET
def edit_member(request, verification_id):
  pass

class DeleteMember(DeleteView):
  model = UserLFG
  success_url = '/members'
  slug_field = 'verification_id'
  slug_url_kwarg = 'verification_id'

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, 'Successfully deleted member listing')
    return super(DeleteMember, self).delete(request, *args, **kwargs)

@require_GET
def member_list(request):
  paginator = Paginator(UserLFG.objects.filter(is_public=True), 20)
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
def view_audition_by_verification(request, verification_id):
  try:
    audition = Audition.objects.get(verification_id=verification_id)
  except Audition.DoesNotExist:
    raise Http404('Audition does not exist.')

  if not audition.is_verified:
    audition.is_verified = True
    audition.save()

  return render(request, 'view_audition.html',
                dictionary={'section': 'auditions',
                            'audition': audition,
                            'maps_key': settings.GOOGLE_MAPS_API_KEY,
                            'verification_id': verification_id})

@require_GET
def edit_audition(request, verification_id):
  pass

class DeleteAudition(DeleteView):
  model = Audition
  success_url = '/auditions'
  slug_field = 'verification_id'
  slug_url_kwarg = 'verification_id'

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, 'Successfully deleted audition listing')
    return super(DeleteAudition, self).delete(request, *args, **kwargs)

@require_GET
def audition_list(request):
  paginator = Paginator(Audition.objects.filter(is_public=True), 20)
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
        _add_userlfg(lfg_form)
        return render(request, 'new_success.html')
    elif form_type == 'audition':
      audition_form = AuditionForm(request.POST)
      if audition_form.is_valid():
        _add_audition(audition_form)
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
                  'form_type': form_type,
                  'section': 'new'})

def _add_userlfg(form):
  data = form.cleaned_data
  user = UserLFG()
  user.name = data['name']
  user.location = data['location']
  user.description = data['description']
  user.email = data['email']
  user.new_group_ok = data['new_group_ok']
  user.verification_id = _get_verification_id()
  user.save()
  user.voice_parts.add(*data['voice_parts'])


def _add_audition(form):
  data = form.cleaned_data
  audition = Audition()
  audition.group = data['group_name']
  audition.location = data['location']
  audition.description = data['description']
  audition.verification_id = _get_verification_id()
  audition.save()
  audition.voice_parts.add(*data['voice_parts'])

def _get_verification_id():
  return base64.urlsafe_b64encode(uuid.uuid4().bytes).strip('=')
