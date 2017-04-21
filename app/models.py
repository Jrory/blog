# encoding:utf-8
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class UserInfo(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)


class Publisher(models.Model):
	name = models.CharField(max_length=30, verbose_name="名称")
	address = models.CharField("地址", max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=20)
	website = models.URLField()

	class Meta:
		verbose_name = "出版商(Publisher)"
		verbose_name_plural = verbose_name
		ordering = ["id"]

	def __unicode__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		verbose_name = "作者(Author)"
		verbose_name_plural = verbose_name
		ordering = ["id"]

	def __unicode__(self):
		return self.name


class AuthorDetail(models.Model):
	sex = models.BooleanField(max_length=1, choices=((0, "男"), (1, "女")))
	email = models.EmailField()
	address = models.CharField(max_length=50)
	birthday = models.DateField()
	author = models.OneToOneField(Author)

	class Meta:
		verbose_name = "作者详情(AuthorDetail)"
		verbose_name_plural = verbose_name
		ordering = ["id"]

	def __unicode__(self):
		return self.author.name


class Book(models.Model):
	title = models.CharField(max_length=50)
	publisher_date = models.DateField()
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)

	class Meta:
		verbose_name = "书籍(Book)"
		verbose_name_plural = verbose_name
		ordering = ["id"]

	def __unicode__(self):
		return self.title
