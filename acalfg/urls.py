from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views import generic

admin.autodiscover()

urlpatterns = patterns("",
  # Admin URLs.
  url(r"^admin/", include(admin.site.urls)),
  # There's no favicon here!
  url(r"^favicon.ico$", generic.RedirectView.as_view()),
  url('^$', 'board.views.home'),
  url('^members/?$', 'board.views.member_list'),
  url('^members/(?P<member_id>\d+)/?$', 'board.views.view_member'),
  url('^auditions/?$', 'board.views.audition_list'),
  url('^auditions/(?P<audition_id>\d+)/?$', 'board.views.view_audition'),
  url('^new/?$', 'board.views.new_listing'),
)
