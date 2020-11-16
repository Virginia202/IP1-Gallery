from django.db import models
from _datetime import datetime
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()  

    def delete_editor(self):
        self.delete() 

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =90)
    post = models.TextField()
    editor = models.ForeignKey('Editor',on_delete=models.CASCADE,)
    editor = models.ForeignKey('Editor',on_delete=models.CASCADE,)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(default=datetime.now,blank=True)
    article_image = models.ImageField(upload_to = 'articles/')
    
    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        diorama = cls.objects.filter(pub_date__date = today)
        return diorama 
    
    @classmethod
    def days_gallery(cls,date):
        diorama = cls.objects.filter(pub_date__date = date)
        return diorama   
    
    @classmethod
    def search_by_title(cls,search_term):
        diorama = cls.objects.filter(title__icontains= search_term)
        return diorama