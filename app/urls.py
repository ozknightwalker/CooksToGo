from django.conf.urls import url

from app import views

urlpatterns = [
    url(
        r'^get_all_recipes/$',
        views.RecipesView.as_view(),
        name='get_all_recipes'
    ),
]
