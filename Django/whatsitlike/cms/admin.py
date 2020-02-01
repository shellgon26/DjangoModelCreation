from django.contrib import admin
from .models import Customer, Content, Bundle, ContentViewer, ContentBundleLink, Progress, ViewerBundleLink

# Define admin classes.
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('customer_id', 'customer_name', 'customer_email')
class ContentAdmin(admin.ModelAdmin):
	list_display = ('content_id', 'content_name', 'customer_id')
class BundleAdmin(admin.ModelAdmin):
	list_display = ('bundle_id', 'bundle_name', 'bundle_description', 'customer_id')
class ContentBundleLinkAdmin(admin.ModelAdmin):
	list_display = ('link_id','content_id','bundle_id')
class ContentViewerAdmin(admin.ModelAdmin):
	list_display = ('content_viewer_id', 'content_viewer_first_name', 'content_viewer_last_name', 'content_viewer_email')
class ProgressAdmin(admin.ModelAdmin):
	list_display = ('progress_id', 'viewer_id','content_id','progress_value')
class ViewerBundleLinkAdmin(admin.ModelAdmin):
	list_display = ('link_id','viewer_id', 'bundle_id', 'percent_progress')
# Register models.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Bundle, BundleAdmin)
admin.site.register(ContentViewer, ContentViewerAdmin)
admin.site.register(ContentBundleLink, ContentBundleLinkAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(ViewerBundleLink, ViewerBundleLinkAdmin)