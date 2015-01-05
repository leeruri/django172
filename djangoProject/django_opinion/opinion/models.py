#-*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.forms.fields import CharField
from django.forms.widgets import HiddenInput, TextInput

class OpinionUser(models.Model):
    AREA = (
        ('K', '국내'),
        ('O', '해외'),
        ('N', '기타'),
        )

    user_email = models.EmailField(unique=True, help_text="your email adress") 
    user_nickname =  models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_url = models.URLField(blank=True, null=True)
    user_area = models.CharField(max_length=1, choices=AREA, blank=True)

    ip_address = models.GenericIPAddressField(unpack_ipv4=True, blank=True, null=True)
    reg_date = models.DateTimeField(default=None)

    def save(self, *args, **kwargs):
        if self.reg_date is None:
            self.reg_date = timezone.now() 
        super(OpinionUser, self).save(*args, **kwargs)
 
    def __unicode__(self):           
        return self.user_nickname

    def getLinkText(self):
        return "<a href=''>"+self.user_nickname+"</a>"

    class Meta:
        ordering = ["-id"]

class OpinionUserForm(ModelForm):
    class Meta:
        model = OpinionUser
        fields = ['user_email', 'user_nickname', 'user_pwd', 'user_url', 'user_area']

class OpinionUserLoginForm(ModelForm):
    class Meta:
        model = OpinionUser
        fields = ['user_email', 'user_pwd']

class Tag(models.Model): #수정한 내용에 대하여 이력을 모두 표시한다.
    tag_name = models.CharField(primary_key=True, max_length=250)
    reg_date = models.DateTimeField(default=None)
  
    def save(self, *args, **kwargs):
        if self.reg_date is None:
            self.reg_date = timezone.now() 
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):           
        return self.tag_name

    class Meta:
        ordering = ["-reg_date"]


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']


class Opinion(models.Model): #수정한 내용에 대하여 이력을 모두 표시한다.
    opinion_title =  models.CharField(max_length=250)
    opinion_contents = models.TextField()
    writer_id = models.CharField(max_length=10, blank=True) #ForienKey OpinionUser
    linked_opinion_id = models.CharField(max_length=10, blank=True, null=True) #ForienKey Opinion
    tag_name = models.CharField(max_length=20, blank=True, null=True)

    ip_address = models.GenericIPAddressField(unpack_ipv4=True, blank=True, null=True)
    reg_date = models.DateTimeField(default=None)
  
    def save(self, *args, **kwargs):
        if self.reg_date is None:
            self.reg_date = timezone.now() 
        super(Opinion, self).save(*args, **kwargs)

    def __unicode__(self):           
        return self.opinion_title

    def getLinkText(self):
        return "<a href='/view/no/"+self.id+"'>"+self.opinion_title+"</a>"

    class Meta:
        ordering = ["-id"]


class OpinionForm(ModelForm): 
    writer_id = CharField(widget=HiddenInput) 
    linked_opinion_id = CharField(widget=HiddenInput, required=False) 
    tag_name = CharField(widget=TextInput)

    class Meta:
        model = Opinion
        fields = ['opinion_title', 'opinion_contents', 'writer_id', 'linked_opinion_id', 'tag_name'] 

class Comment(models.Model): #수정한 내용에 대하여 이력을 모두 표시한다.
    comment_contents = models.TextField()
    writer_id = models.CharField(max_length=10, blank=True) #ForienKey OpinionUser
    opinion_id = models.CharField(max_length=10, blank=True) #ForienKey Opinion
     
    ip_address = models.GenericIPAddressField(unpack_ipv4=True, blank=True, null=True)
    reg_date = models.DateTimeField(default=None)
  
    def save(self, *args, **kwargs):
        if self.reg_date is None:
            self.reg_date = timezone.now() 
        super(Comment, self).save(*args, **kwargs)

    def __unicode__(self):           
        return self.comment_contents

    class Meta:
        ordering = ["-id"]
 
class CommentForm(ModelForm):
    writer_id = CharField(widget=HiddenInput) 
    opinion_id = CharField(widget=HiddenInput)  
    class Meta:
        model = Comment
        fields = ['comment_contents', 'writer_id', 'opinion_id']