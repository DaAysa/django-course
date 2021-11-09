# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile

# @admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')

    # Campos que permiten clickear para ver el detalle
    list_display_links = ('pk', 'user')

    # Campos que se pueden editar desde la lista de elementos
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = ('user__email', 'user__first_name', 'user__last_name')

    # Campos que aparecen como filtros a la derecha
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    # Al momento de agregar o editar, se muestran solo ciertos campos
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            ),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            ),
        }),
    )

    readonly_fields = ('created', 'modified')

# Lo siguiente es para agregar un user y su profile en un único form
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)