from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples: Check out the game.py file to find the "%_view" methods
    #url(r'^$', 'searchApp.game.home_view'),
    url(r'^help/$', 'searchApp.game.help_view'),
    url(r'^stats/$', 'searchApp.game.stats_view'),
    url(r'^results/$', 'searchApp.game.results_view'),
    url(r'^game/$', 'searchApp.game.game_view'),
    # url(r'^SearchHero/', include('SearchHero.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	#authentication apps:
	url(r'^login/$', 'authentication.views.login_page'),
	url(r'^login_auth/$', 'authentication.views.auth_login'),
	url(r'^logout/$', 'authentication.views.auth_logout'),
	url(r'^register/$', 'authentication.views.register'),
	url(r'^$', 'authentication.views.home'),
)
