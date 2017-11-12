from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.create_pdf, name="create_pdf"),
    url(r"^(?P<pk>\d+)$", views.view_pdf, name="view_pdf"),
]
