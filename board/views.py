import base64
import uuid

from board.models import Audition, UserLFG
from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import render, redirect
from board.models import Audition, UserLFG
from board.forms import AuditionForm, LfgForm

VERIFICATION_MESSAGE = ('Thanks for verifying your email address! '
                        'From this page you can edit or delete your listing. '
                        'Don\'t give this link to anyone else, or else '
                        'they\'ll be able to edit your post!')
POST_MESSAGE = 'Successfully posted your listing!'

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
    messages.success(request, VERIFICATION_MESSAGE)

  return render(request, 'view_member.html',
                dictionary={'section': 'members', 'member': m,
                            'maps_key': settings.GOOGLE_MAPS_API_KEY,
                            'verification_id': verification_id})


@require_GET
def post_member(request, verification_id):
  try:
    m = UserLFG.objects.get(verification_id=verification_id)
  except UserLFG.DoesNotExist:
    raise Http404('Member does not exist.')

  m.is_public = True
  m.save()
  messages.success(request, POST_MESSAGE)
  return redirect('view-member-by-verification',
                  verification_id=verification_id)

class EditMember(SuccessMessageMixin, UpdateView):
  form_class = LfgForm
  model = UserLFG
  success_url = '/members/%(verification_id)s'
  slug_field = 'verification_id'
  slug_url_kwarg = 'verification_id'
  success_message = 'Successfully edited member listing!'

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
    messages.success(request, VERIFICATION_MESSAGE)

  return render(request, 'view_audition.html',
                dictionary={'section': 'auditions',
                            'audition': audition,
                            'maps_key': settings.GOOGLE_MAPS_API_KEY,
                            'verification_id': verification_id})

@require_GET
def post_audition(request, verification_id):
  try:
    audition = Audition.objects.get(verification_id=verification_id)
  except Audition.DoesNotExist:
    raise Http404('Audition does not exist.')

  audition.is_public = True
  audition.save()
  messages.success(request, POST_MESSAGE)
  return redirect('view-audition-by-verification',
                  verification_id=verification_id)

class EditAudition(SuccessMessageMixin, UpdateView):
  form_class = AuditionForm
  model = Audition
  success_url = '/auditions/%(verification_id)s'
  slug_field = 'verification_id'
  slug_url_kwarg = 'verification_id'
  success_message = 'Successfully edited audition listing!'

class DeleteAudition(DeleteView):
  model = Audition
  success_url = '/auditions'
  slug_field = 'verification_id'
  slug_url_kwarg = 'verification_id'

  def delete(self, request, *args, **kwargs):
    messages.success(self.request, 'Successfully deleted audition listing!')
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
  user = form.save(commit=False)
  user.verification_id = _get_verification_id()
  user.save()
  _send_verification_email('members', user.verification_id, user.email)

def _add_audition(form):
  audition = form.save(commit=False)
  audition.verification_id = _get_verification_id()
  audition.save()
  _send_verification_email('auditions', audition.verification_id, audition.email)

def _get_verification_id():
  return base64.urlsafe_b64encode(uuid.uuid4().bytes).strip('=')

def _send_verification_email(url_part, verification_id, to_email):
  email_text = render_to_string(
      'verification_email.txt',
      {'verification_link':
       'http://%s/%s/%s' % (settings.SITE_DOMAIN, url_part, verification_id)})
  send_mail('AcaLFG verification', email_text, 'acalfg@acalfg.com',
            [to_email], fail_silently=False,
            auth_user=settings.EMAIL_HOST_USER,
            auth_password=settings.EMAIL_HOST_PASSWORD)
