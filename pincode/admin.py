from __future__ import unicode_literals
from django.contrib import admin
from pincode.models import Pincode, APIRequest


@admin.register(Pincode)
class PincodeAdmin(admin.ModelAdmin):
    """Display all the fields related to
    User class on Admin Panel, Can be seen
    only by Developers.
    """
    list_display = ('pincode', 'city', 'distict', 'state')
    search_fields = ('pincode', 'city', 'state')
    list_filter = ('state', 'city', 'distict')
    # TODOS: Put some actions syntax: ['download']
    # Then define a sub function for the that field.

@admin.register(APIRequest)
class APIRequestAdmin(admin.ModelAdmin):
	"""docstring for APIRequestAdmin"""
	list_display = ('ip', 'pincode', 'query', 'created')
	search_fields = ('ip', 'pincode')
	raw_id_fields = ('pincode',)
		

# This is used to register the function on
# Admin panel.
admin.site.index_title = 'Ziptracker'
