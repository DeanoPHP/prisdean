from django import forms
from django.contrib.auth import get_user_model
from userprofile.models import UserProfile

User = get_user_model()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'address_line_1', 'address_line_2', 'city', 'county', 'postcode']


class CombinedUserProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop('user_instance')
        self.profile_instance = kwargs.pop('profile_instance')
        super().__init__(*args, **kwargs)

        # Create the individual forms once
        self.user_form = UserForm(instance=self.user_instance)
        self.profile_form = UserProfileForm(instance=self.profile_instance)

        # Combine fields from both forms
        self.fields.update(self.user_form.fields)
        self.fields.update(self.profile_form.fields)

        # Set initial values so form is prefilled
        self.initial.update(self.user_form.initial)
        self.initial.update(self.profile_form.initial)

    def save(self, commit=True):
        user_form = UserForm(self.data, instance=self.user_instance)
        profile_form = UserProfileForm(self.data, self.files, instance=self.profile_instance)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return self.profile_instance

