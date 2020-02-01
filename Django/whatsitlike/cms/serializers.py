from rest_framework import serializers
from .models import Customer, Content, Bundle, ContentViewer, ContentBundleLink, Progress, ViewerBundleLink

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ('customer_id', 'customer_name', 'customer_email', 'customer_logo_URL', 'customer_primary_colour','customer_secondary_colour', 'customer_keyword')
class ContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Content
    fields = ('content_id', 'content_type', 'content_name', 'store_location','customer_id')
class BundleSerializer(serializers.ModelSerializer):
    model = Bundle
    fields = ('bundle_id', 'customer_id', 'bundle_name', 'bundle_description')
class ContentViewerSerializer(serializers.ModelSerializer):
	model = ContentViewer
	fields = ('content_viewer_id', 'content_viewer_first_name','content_viewer_last_name','content_viewer_email','content_viewer_key')
class ContentBundleLinkSerializer(serializers.ModelSerializer):
	model = ContentBundleLink
	fields = ('link_id','content_id','bundle_id')
class ProgressSerializer(serializers.ModelSerializer):
	model = Progress
	fields = ('progress_id','viewer_id','content_id','progress_value')
class ViewerBundleLinkSerializer(serializers.ModelSerializer):
	model = ViewerBundleLink
	fields = ('link_id','viewer_id','bundle_id','percent_progress')