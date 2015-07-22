from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import generic

from models import Recipe


class RecipesView(generic.View):

    def get(self, request):
        recipes = Recipe.objects.all()
        return HttpResponse(str(recipes))
