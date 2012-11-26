
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from dreamuserdb.models import Group, Role
from dreamprofile.forms import AvatarForm, ContactForm, GroupsForm, RolesForm

class AvatarFormView(FormView):
  form_class = AvatarForm
  template_name = 'dreamprofile/avatar.html'
  success_url = reverse_lazy('dreamprofile_avatar')

  def get_initial(self):
    user = self.request.user
    return {
      'url': user.picture_url,
      }

  def form_valid(self, form):
    user = self.request.user
    user.picture_url = form.cleaned_data['url']
    user.save()
    return super(AvatarFormView, self).form_valid(form)


class ContactFormView(FormView):
  form_class = ContactForm
  template_name = 'dreamprofile/contact.html'
  success_url = reverse_lazy('dreamprofile_contact')

  def get_initial(self):
    user = self.request.user
    return {
      'phone_number': user.phone_number,
      'email': user.email,
      }

  def form_valid(self, form):
    user = self.request.user
    user.phone_number = form.cleaned_data['phone_number']
    user.email = form.cleaned_data['email']
    user.save()
    return super(ContactFormView, self).form_valid(form)


class GroupsFormView(FormView):
  form_class = GroupsForm
  template_name = 'dreamprofile/groups.html'
  success_url = reverse_lazy('dreamprofile_groups')

  def get_queryset(self):
    return Group.objects.filter(organisation__in=self.request.user.organisations.all).order_by('organisation__id', 'title')

  def get_form_kwargs(self):
    kwargs = super(GroupsFormView, self).get_form_kwargs()
    kwargs['queryset'] = self.get_queryset()
    kwargs['initial_queryset'] = self.request.user.user_groups.all()
    return kwargs

  def get_context_data(self, **kwargs):
    kwargs['has_many_organisations'] = self.request.user.organisations.count() > 1
    kwargs['organisations'] = self.request.user.organisations.all()
    return super(GroupsFormView, self).get_context_data(**kwargs)

  def form_valid(self, form):
    qs = self.get_queryset()
    usergroups = self.request.user.user_groups
    for k in form.cleaned_data:
      v = form.cleaned_data[k]
      pk = k.replace('obj', '')
      try:
        obj = qs.get(pk=pk, official=False)
        if v:
          usergroups.add(obj)
        else:
          usergroups.remove(obj)
      except Group.DoesNotExist:
        pass
    return super(GroupsFormView, self).form_valid(form)

class RolesFormView(FormView):
  form_class = RolesForm
  template_name = 'dreamprofile/roles.html'
  success_url = reverse_lazy('dreamprofile_roles')

  def get_queryset(self):
    return Role.objects.filter(organisation__in=self.request.user.organisations.all).order_by('organisation__id', 'title')

  def get_form_kwargs(self):
    kwargs = super(RolesFormView, self).get_form_kwargs()
    kwargs['queryset'] = self.get_queryset()
    kwargs['initial_queryset'] = self.request.user.roles.all()
    return kwargs

  def get_context_data(self, **kwargs):
    kwargs['has_many_organisations'] = self.request.user.organisations.count() > 1
    kwargs['organisations'] = self.request.user.organisations.all()
    return super(RolesFormView, self).get_context_data(**kwargs)

