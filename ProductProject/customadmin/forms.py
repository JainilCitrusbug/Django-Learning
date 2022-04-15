# -*- coding: utf-8 -*-

from django import forms

from application.models import *


# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

class UserCreationForm(forms.ModelForm):
    """Custom User"""

    class Meta():
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )
        if not last_name :
            raise forms.ValidationError(
                "Please add last name."
            )
        if not first_name :
            raise forms.ValidationError(
                "Please add first name."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class UserChangeForm(forms.ModelForm):
    """Custom form to change User"""

    class Meta():
        model = User

        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
            "is_active",
            "is_staff",
            "is_superuser",
        ]

    def clean(self):
        cleaned_data = super(UserChangeForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )
        if not last_name :
            raise forms.ValidationError(
                "Please add last name."
            )
        if not first_name :
            raise forms.ValidationError(
                "Please add first name."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance

# -----------------------------------------------------------------------------
# category
# -----------------------------------------------------------------------------

class CategoryForm(forms.ModelForm):
    """Custom User"""

    class Meta():
        model = Category
        fields = [
            "category_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CategoryForm, self).clean()
        category = cleaned_data.get("category_name")

        if not category :
            raise forms.ValidationError(
                "Please add category."
            )
       
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class ProductForm(forms.ModelForm):
    """Custom User"""

    class Meta():
        model = Product
        fields = [
            "product_name",
            "product_description",
            "product_price",
            "product_image",
            "product_category",
            "user",
            "soft_delete",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        product_name = cleaned_data.get("product_name")
        product_description = cleaned_data.get("product_description")
        product_price = cleaned_data.get("product_price")
        product_image = cleaned_data.get("product_image")
        product_category = cleaned_data.get("product_category")
        user = cleaned_data.get("user")


        if not product_name :
            raise forms.ValidationError(
                "Please add product."
            )
        if not product_description :
            raise forms.ValidationError(
                "Please add description."
            )
        if not product_price :
            raise forms.ValidationError(
                "Please add price."
            )
        if not product_image :
            raise forms.ValidationError(
                "Please add image."
            )
        if not product_category :
            raise forms.ValidationError(
                "Please add category."
            )
        if not user :
            raise forms.ValidationError(
                "Please add user."
            )
       
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance
