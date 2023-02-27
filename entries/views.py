from django.shortcuts import render
from newsapi import NewsApiClient
from django.urls import reverse_lazy
from .forms import ImageForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Entry, Mylist, News, Base, Contacts


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(CreateView):
    model = Entry
    fields = ["title",
              "content"]
    success_url = reverse_lazy("entry-list")


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ["title",
              "content"]

    def get_success_url(
            self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")


class MylistListView(ListView):
    model = Mylist


class NewslistView(ListView):
    model = News


class BaselistView(ListView):
    model = Base

class ContactslistView(ListView):
    model = Contacts