from django.urls import path
from . import views
from users.views import RegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry-list"),
    path("entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail" ),
    path("create", views.EntryCreateView.as_view(), name="entry-create"),
    path("entry/<int:pk>/update", views.EntryUpdateView.as_view(), name="entry-update"),
    path("entry/<int:pk>/delete", views.EntryDeleteView.as_view(), name="entry-delete"),
    #users
    path("users/create/", RegistrationView.as_view(), name="registration"),
    path("users/login/", UserLoginView.as_view(), name="login"),
    path("users/logout/", UserLogoutView.as_view(), name="logout"),
]