from django.conf.urls import url

from . import views

app_name = 'post'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_pk>[0-9]+)/$', views.post_delete, name='post_delete'),
]

# url = post_delete 라는 아파트에
# post_pk = i.pk post_pk라는 호수에 i.pk라는 택배를 보낸다.
