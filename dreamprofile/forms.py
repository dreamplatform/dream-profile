
from django import forms


class AvatarForm(forms.Form):
  url = forms.CharField(max_length=2048, required=False)

class ContactForm(forms.Form):
  phone_number = forms.CharField(max_length=100, required=False)
  email = forms.EmailField(max_length=2048)

class MultiselectForm(forms.Form):
  def __init__(self, *args, **kwargs):
    qs = kwargs.pop('queryset')
    iqs = kwargs.pop('initial_queryset')
    super(MultiselectForm, self).__init__(*args, **kwargs)
    for obj in qs:
      initial = bool(obj in iqs) or False
      field = forms.BooleanField(label=obj.title, initial=initial, required=False)
      setattr(field, 'object', obj)
      self.fields['obj%s'%obj.pk] = field


class GroupsForm(MultiselectForm):
  pass

class RolesForm(MultiselectForm):
  pass

