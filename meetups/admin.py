from django.contrib import admin

from .models import Meetup, Location, Participant


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "date", "location")
    list_filter = ("title", "location", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
