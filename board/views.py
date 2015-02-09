from board.models import UserLFG
from django.http import Http404
from django.shortcuts import render

def home(request):
  return render(request, 'home.html', dictionary={'section': 'home'})

def view_member(request, member_id):
  try:
    m = UserLFG.objects.get(pk=member_id)
  except UserLFG.DoesNotExist:
    raise Http404('Member does not exist.')
  return render(request, 'view_member.html',
                dictionary={'section': 'members', 'member': m})
