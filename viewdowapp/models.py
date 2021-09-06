from django.db import models


class FormDownload(models.Model):
    text_file = models.FileField(upload_to="upload_txt", verbose_name="Файл")



class WordAnalysis(models.Model):
    texts = models.ManyToManyField(FormDownload)
    word = models.CharField(max_length=64)
    tf = models.FloatField(blank=True, null=True)
    idf = models.FloatField(blank=True, null=True)
    int_word = models.IntegerField()

    def __str__(self):
        return self.word
