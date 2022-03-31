from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from .models import User
from django.utils.translation import gettext_lazy as _

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character."))]
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'alias', 'password')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('email', 'alias', 'password', 'is_deactivated', 'is_active', 'is_staff', 'is_admin')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'alias', 'date_joined','last_login', 'is_superuser', 'is_admin', 'is_staff', 'is_active', 'is_deactivated')
    list_filter = ('is_admin', 'is_staff',)
    search_fields = ('email', 'alias',)
    readonly_fields = ('id', 'date_joined','last_login')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        ('Personal info', {'fields': ('id','email', 'alias',)}),
        ('Meta', {'fields': ('date_joined','last_login')}),
        ('Private', {'fields': ('password',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin', 'is_staff','is_active', 'is_deactivated')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )



# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)