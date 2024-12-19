from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Admin, Question_designer, Student, Guest


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('code_meli', 'username', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    search_fields = ('code_meli', 'username', 'first_name', 'last_name', 'email')
    list_filter = ('role', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('code_meli', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'province',
                                         'city', 'county', 'landline_phone', 'bio', 'photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'role', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('code_meli', 'password1', 'password2', 'username', 'first_name', 'last_name', 'role'),
        }),
    )
    ordering = ('code_meli',)

    def save_model(self, request, obj, form, change):
        """
        Ensure the password is hashed when saving the CustomUser through the admin.
        """
        if not change or (change and 'password' in form.changed_data):
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin',)
    search_fields = ('admin__code_meli', 'admin__username', 'admin__first_name', 'admin__last_name')
    list_filter = ('admin__is_active',)


@admin.register(Question_designer)
class QuestionDesignerAdmin(admin.ModelAdmin):
    list_display = ('designer',)
    search_fields = ('designer__code_meli', 'designer__username', 'designer__first_name', 'designer__last_name')
    list_filter = ('designer__is_active',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student',)
    search_fields = ('student__code_meli', 'student__username', 'student__first_name', 'student__last_name')
    list_filter = ('student__is_active',)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest',)
    search_fields = ('guest__code_meli', 'guest__username', 'guest__first_name', 'guest__last_name')
    list_filter = ('guest__is_active',)
