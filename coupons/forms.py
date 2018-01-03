#coding=utf-8

from django import forms

class CouponApplyForm(forms.Form):
    code = forms.CharField()