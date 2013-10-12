from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from notification.views import IndexView, MessagesView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^messages', MessagesView.as_view(), name='messages'),
    # url(r'^notification_example/', include('notification_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
