# encoding:utf-8
from django import forms
from app.models import Publisher

from django.core.exceptions import ValidationError

# class PublisherForm(forms.Form):
# 	name = forms.CharField(label="名称")
# 	address = forms.CharField(label="地址")
# 	city = forms.CharField(label="城市")
# 	state_province = forms.CharField(label="省份")
# 	country = forms.CharField(label="国家")
# 	website = forms.URLField(label="网站")


# 一 表单验证器(回调函数)
# def validate_name(value):
# 	try:
# 		Publisher.objects.get(name=value)
# 		raise ValidationError("%s exist!" % value)
# 	except Publisher.DoesNotExist:
# 		pass


class PublisherForm(forms.ModelForm):
	# name = forms.CharField(label="名称", validators=[validate_name])

	# 二 clean_filedname 验证字段
	# def clean_name(self):
	# 	value = self.cleaned_data.get('name')
	# 	try:
	# 		Publisher.objects.get(name=value)
	# 		raise ValidationError("%s exist!" % value)
	# 	except Publisher.DoesNotExist:
	# 		pass
	# 	return value

	# 三 表单clean验证方法
	def clean(self):
		cleaned_data = super(PublisherForm, self).clean()
		value = cleaned_data.get('name')
		try:
			Publisher.objects.get(name=value)
			self._errors['name'] = self.error_class(["%s exist!" % value])
		except Publisher.DoesNotExist:
			pass
		return cleaned_data

	class Meta:
		model = Publisher
		exclude = ('id',)
