from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# CMS models.
class Customer(models.Model):
	customer_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=120)
	customer_email = models.CharField(max_length=128)
	customer_logo_URL = models.URLField(blank=True)
	css_title_colour = models.CharField(max_length=7, default = '#214192')
	css_subheading_colour = models.CharField(max_length=7, default = '#2A5EB2')
	css_icon_colour = models.CharField(max_length=7, default = '#3580D7')
	css_icon_hover_colour = models.CharField(max_length=7, default = '#4F9EE9')
	css_button_colour = models.CharField(max_length=7, default = '#F49D14')
	css_button_hover_colour = models.CharField(max_length=7, default = '#F26D0E')
	css_default_border_colour = models.CharField(max_length=7, default = '#214192')
	css_focus_border_colour = models.CharField(max_length=7, default = '#F6C532')
	customer_keyword=models.CharField(max_length=120)

	def _str_(self):
		return str(self.customer_id) + " " + self.customer_name + " " + self.customer_email + " " + self.customer_keyword

class Content(models.Model):
	content_id = models.AutoField(primary_key=True)
	content_type = models.CharField(max_length=128)
	content_name = models.CharField(max_length=128)
	store_location = models.URLField(blank=True)
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def _str_(self):
		return str(self.content_id + " " + self.content_type + " " + self.content_name + " " + self.customer_id)

class Bundle(models.Model):
	bundle_id = models.AutoField(primary_key=True)
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	bundle_name = models.CharField(max_length=120)
	bundle_description  = models.CharField(max_length=256)

	def _str_(self):
		return str(self.bundle_id + " " + self.bundle_name + " " + self.bundle_description + " "+ self.customer_id)

class ContentViewer(models.Model):
	content_viewer_id = models.AutoField(primary_key=True)
	content_viewer_first_name = models.CharField(max_length=120)
	content_viewer_last_name = models.CharField(max_length=120)
	content_viewer_email = models.CharField(max_length=120)
	content_viewer_key = models.CharField(max_length=256)

	def _str_(self):
		return str(self.content_viewer_id + " " + self.content_viewer_first_name + " " + self.content_viewer_last_name + " " + self.content_viewer_email)

class ContentBundleLink(models.Model):
	link_id = models.AutoField(primary_key=True)
	content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
	bundle_id = models.ForeignKey(Bundle,on_delete=models.CASCADE)

	def _str_(self):
		return str(self.link_id + " " + self.content_id + " "+ self.bundle_id)

class Progress(models.Model):
	progress_id = models.AutoField(primary_key=True)
	viewer_id = models.ForeignKey(ContentViewer, on_delete=models.CASCADE)
	content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
	progress_value = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

	def _str_(self):
		return str(self.progress_id + " " + self.viewer_id + " " + self.content_id + " "+ self.progress_value)

class ViewerBundleLink(models.Model):
	link_id = models.AutoField(primary_key=True)
	viewer_id = models.ForeignKey(ContentViewer, on_delete=models.CASCADE)
	bundle_id = models.ForeignKey(Bundle,on_delete=models.CASCADE)
	percent_progress = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

	def _str_(self):
		return str(self.link_id+ " " + self.viewer_id + " "+ self.bundle_id + " "+ self.percent_progress)
		