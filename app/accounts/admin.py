from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from userprofile.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('email', 'is_staff', 'is_active', 'city', 'postcode')  # Add custom fields here
    search_fields = ('email', 'city', 'postcode')
    ordering = ('email',)

    # Add custom fields to the edit form
    fieldsets = UserAdmin.fieldsets + (
        ('Address Info', {
            'fields': (
                'phone',
                'address_line_1',
                'address_line_2',
                'city',
                'county',
                'postcode',
            ),
        }),
    )

    # Add custom fields to the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone',
                'address_line_1',
                'address_line_2',
                'city',
                'county',
                'postcode',
            ),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
