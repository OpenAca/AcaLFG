from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from board.models import VoicePart

class LfgForm(forms.Form):
  helper = FormHelper()
  helper.form_tag = False
  helper.layout = Layout(
      'name',
      'location',
      'email',
      InlineCheckboxes('voice_parts'),
      'new_group_ok',
      'description')
  helper.add_input(Submit('submit', 'Submit'))

  name = forms.CharField(
      label='Name', max_length=100, required=True,
      help_text='Your name (first only is ok!)')
  location = forms.CharField(
      label='Location', max_length=255, required=True,
      help_text='"City, State" or "City, Country"')
  email = forms.EmailField(required=True)
  voice_parts = forms.ModelMultipleChoiceField(
      label='Voice part(s)',
      widget=forms.CheckboxSelectMultiple(),
      queryset=VoicePart.objects.all(),
      help_text='Select any and all that apply!')
  new_group_ok = forms.BooleanField(
      label='New group OK?',
      help_text='Would you be ok with helping to start a new group?')
  description = forms.CharField(
      widget=forms.Textarea(attrs={'rows': '4'}))

class AuditionForm(forms.Form):
  helper = FormHelper()
  helper.form_tag = False
  helper.layout = Layout(
      'group_name',
      'location',
      'contact_email',
      InlineCheckboxes('voice_parts'),
      'description')
  helper.add_input(Submit('submit', 'Submit'))

  group_name = forms.CharField(label='Group Name', max_length=100, required=True)
  location = forms.CharField(
      label='Location', max_length=255, required=True,
      help_text='"City, State" or "City, Country"')
  contact_email = forms.EmailField()
  voice_parts = forms.ModelMultipleChoiceField(
      label='Voice part(s)',
      widget=forms.CheckboxSelectMultiple(),
      queryset=VoicePart.objects.all())
  description = forms.CharField(
      widget=forms.Textarea(attrs={'rows': '4'}))
