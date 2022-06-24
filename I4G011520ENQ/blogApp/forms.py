from socket import fromshare
from attr import fields
from django import froms
from matplotlib.pyplot import title
from .models import blogApp
class blogAppForm(forms):
    class meta:
        model = blogApp 
        fields = [
            "title",
            "description"
        ]