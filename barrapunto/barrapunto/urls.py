from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lista/', 'Cbarrapunto.views.listado'),
    url(r'^update', 'Cbarrapunto.views.update'),
    url(r'(\d+)','Cbarrapunto.views.pagina'),
    url(r'/?(.*)', 'Cbarrapunto.views.index'),
)
