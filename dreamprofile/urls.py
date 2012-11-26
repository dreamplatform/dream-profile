
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from dreamprofile.views import AvatarFormView, ContactFormView, GroupsFormView, RolesFormView

urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name='dreamprofile/main.html')), name='dreamprofile_main'),
    url(r'^avatar/$', login_required(AvatarFormView.as_view()), name='dreamprofile_avatar'),
    url(r'^contact/$', login_required(ContactFormView.as_view()), name='dreamprofile_contact'),
    url(r'^groups/$', login_required(GroupsFormView.as_view()), name='dreamprofile_groups'),
    url(r'^roles/$', login_required(RolesFormView.as_view()), name='dreamprofile_roles'),
)

