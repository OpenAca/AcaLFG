from django import forms
from board.models import VoicePart

class LfgForm(forms.Form):
  name = forms.CharField(
      label='Name', max_length=100, required=True,
      help_text='Your name (first only is ok!)')
  email = forms.EmailField(required=True)
  voice_parts = forms.ModelMultipleChoiceField(
      label='Voice part(s)',
      widget=forms.CheckboxSelectMultiple(),
      queryset=VoicePart.objects.all())
  description = forms.CharField(widget=forms.Textarea())

class AuditionForm(forms.Form):
  group_name = forms.CharField(label='Group Name', max_length=100, required=True)
  contact_email = forms.EmailField()
  voice_parts = forms.ModelMultipleChoiceField(
      label='Voice part(s)',
      widget=forms.CheckboxSelectMultiple(),
      queryset=VoicePart.objects.all())
  description = forms.CharField(widget=forms.Textarea())
