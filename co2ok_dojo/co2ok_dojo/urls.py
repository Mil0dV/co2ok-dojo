from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from users import views as users_views
from ninja_partner_stores import views as ninja_partner_stores_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^login/$', users_views.register, name='login'),
<<<<<<< HEAD
    url(r'^(?P<id>\d+)/$', users_views.profil, name='profil'),
    url(r'^(?P<user_id>\d+)/$', users_views.invited_sign, name='invitation_page'),
    #path('profil', users_views.profil, name='profil'),
=======
    url(r'^profile/$', users_views.profile, name='profile'),
    url(r'^ninja-partner-stores/$', ninja_partner_stores_views.ninja_partner_stores, name='ninja-partner-stores'),
>>>>>>> afafad3b6d973e256e3d774366f6d0e61cb3d2c8

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
