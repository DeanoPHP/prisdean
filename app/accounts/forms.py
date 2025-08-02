from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=15, required=True)
    address_line_1 = forms.CharField(max_length=255, required=True)
    address_line_2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=True)
    county = forms.CharField(max_length=100, required=False)
    postcode = forms.CharField(max_length=10, required=True)

    def save(self, request):
        user = super().save(request)
        user.phone = self.cleaned_data['phone']
        user.address_line_1 = self.cleaned_data['address_line_1']
        user.address_line_2 = self.cleaned_data.get('address_line_2')
        user.city = self.cleaned_data['city']
        user.county = self.cleaned_data.get('county')
        user.postcode = self.cleaned_data['postcode']
        user.save()
        return user