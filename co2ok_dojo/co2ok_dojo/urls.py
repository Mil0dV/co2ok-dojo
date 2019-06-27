from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
#from django.contrib.auth import views as auth_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from cuser.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.i18n import i18n_patterns
# from django.contrib.auth.views import RegisterView

from search import views as search_views
from users import views as users_views
from welcome import views as welcome_views
from home import views as home_views
from ninja_partner_stores import views as ninja_partner_stores_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^signup/$', users_views.signup, name='signup'),
    # url(r'^signup/$', SignupView.as_view(authentication_form=UserCreationForm), name='signup'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # deze werkt gek genoeg niet:
    # url(r'^login/$', auth_views.LoginView, name='login'),
    url(r'^login/$', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
    # url( r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    # url(r'^(?P<id>\d+)/$', users_views.profil, name='profil'),
     url(r'^accounts/profile/$', users_views.profile, name='profile'),
     url(r'^picked_cause/$', users_views.picked_cause, name='picked_cause'),

    url(r'^(?P<user_id>\d+)/$', users_views.invited_sign, name='invitation_page'),

    url(r'^partner-stores/$', ninja_partner_stores_views.partner_stores, name='partner-stores'),
    url(r'^partner-stores-cat/$', ninja_partner_stores_views.partner_stores_cat, name='partner-stores-cat'),
    url(r'^partner-stores-all/$', ninja_partner_stores_views.partner_stores_all, name='partner_stores_all'),
    url(r'^partner-stores-search/$', ninja_partner_stores_views.partner_stores_search, name='partner_stores_search'),
    url(r'^partner-stores-category/$', ninja_partner_stores_views.partner_stores_category, name='partner-stores-category'),
    url(r'^welcome/$', welcome_views.welcome, name='welcome'),
    url(r'^mission/$', home_views.mission, name='mission'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
    url('', include('pwa.urls')),

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
