from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Recipe

class ListRecipes(APIView):
  def get(self, request):
    try:
      recipes = Recipe.objects.all()
      res_list = [
        {
          'id': d.id,
          'title': d.title,
          'making_time': d.making_time,
          'serves': d.serves,
          'ingredients': d.ingredients,
          'cost': d.cost
        }
        for d in recipes
      ]
      return Response(res_list)
    except:
      return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DetailRecipes(APIView):
    def get(self, request, pk):
        try:
            try:
                recipe = Recipe.objects.get(id=pk)
            except:
                error_msg = "そんなidのレシピはないよ！"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            msg = 'Recipe details by id'
            res = {
                'id': recipe.id,
                'title': recipe.title,
                'making_time': recipe.making_time,
                'serves': recipe.serves,
                'ingredients': recipe.ingredients,
                'cost': recipe.cost,
            }
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)