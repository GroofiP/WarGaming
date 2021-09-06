from math import log10

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from viewdowapp.forms import TextDownloadForm
from viewdowapp.models import FormDownload, WordAnalysis


def render_data():
    txt = FormDownload.objects.last()
    if txt:
        with open(f"media/{txt.text_file}", "r", encoding="UTF-8") as file_r:
            f = file_r.read().split(" ")
            all_word = len(f)
            for a in f:
                a = a.upper()
                item = WordAnalysis.objects.filter(word=a)
                if item:
                    item = item[0]
                    item.texts.add(txt)
                    item.save()
                    item.int_word += 1
                    item.tf = item.int_word / all_word
                    item.idf = log10(item.texts.count() / item.int_word)
                else:
                    item = WordAnalysis.objects.create(int_word=1, word=a, tf=1 / all_word,
                                                       idf=log10(len(FormDownload.objects.all()) / 1))
                    item.save()
                    item.texts.add(txt)
                item.save()


class IndexForm(CreateView, ListView):
    template_name = "index.html"
    form_class = TextDownloadForm
    model = FormDownload
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        render_data()
        form = TextDownloadForm
        words = WordAnalysis.objects.order_by('idf')[:50]
        context = {"words": words, "form": form}
        return render(request, "index.html", context=context)
