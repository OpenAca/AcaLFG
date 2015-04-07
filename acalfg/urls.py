from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views import generic
from board.views import DeleteAudition, DeleteMember, EditAudition, EditMember

admin.autodiscover()

urlpatterns = patterns("",
    # Admin URLs.
    url(r"^admin/", include(admin.site.urls)),
    # There's no favicon here!
    url(r"^favicon.ico$", generic.RedirectView.as_view()),
    url('^$', 'board.views.home'),
    url('^members/?$', 'board.views.member_list'),
    url('^members/(?P<member_id>\d+)/?$', 'board.views.view_member'),
    url('^members/(?P<verification_id>[a-zA-Z0-9_-]+)/?$',
        'board.views.view_member_by_verification',
        name='view-member-by-verification'),
    url('^members/(?P<verification_id>[a-zA-Z0-9_-]+)/edit/?$', EditMember.as_view()),
    url('^members/(?P<verification_id>[a-zA-Z0-9_-]+)/delete/?$', DeleteMember.as_view()),
    url('^members/(?P<verification_id>[a-zA-Z0-9_-]+)/post/?$', 'board.views.post_member'),
    url('^auditions/?$', 'board.views.audition_list'),
    url('^auditions/(?P<audition_id>\d+)/?$', 'board.views.view_audition'),
    url('^auditions/(?P<verification_id>[a-zA-Z0-9_-]+)/?$',
        'board.views.view_audition_by_verification',
        name='view-audition-by-verification'),
    url('^auditions/(?P<verification_id>[a-zA-Z0-9_-]+)/edit/?$', EditAudition.as_view()),
    url('^auditions/(?P<verification_id>[a-zA-Z0-9_-]+)/delete/?$', DeleteAudition.as_view()),
    url('^auditions/(?P<verification_id>[a-zA-Z0-9_-]+)/post/?$', 'board.views.post_audition'),
    url('^new/?$', 'board.views.new_listing'),
)
