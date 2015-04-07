from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from board.models import Audition, UserLFG

class LfgForm(forms.ModelForm):
    class Meta(object):
        model = UserLFG
        fields = ['name', 'location', 'email', 'voice_parts',
                  'new_group_ok', 'description']
        widgets = {'voice_parts': forms.CheckboxSelectMultiple(),
                   'description': forms.Textarea(attrs={'rows': '4'}),
                   'location': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super(LfgForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'name',
            'location',
            'email',
            InlineCheckboxes('voice_parts'),
            'new_group_ok',
            'description')
        self.helper.add_input(Submit('submit', 'Submit'))


class AuditionForm(forms.ModelForm):
    class Meta(object):
        model = Audition
        fields = ['group', 'location', 'email', 'voice_parts',
                  'description']
        widgets = {'voice_parts': forms.CheckboxSelectMultiple(),
                   'description': forms.Textarea(attrs={'rows': '4'}),
                   'location': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super(AuditionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'group',
            'location',
            'email',
            InlineCheckboxes('voice_parts'),
            'description')
        self.helper.add_input(Submit('submit', 'Submit'))
