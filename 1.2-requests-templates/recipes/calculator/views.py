from django.shortcuts import render
from django.http import HttpResponse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recepts(request,name_dishes,number_dishes=1) :
    dish = DATA.get(name_dishes,{})
    context = {}
    if dish :
        calculate_recipe = {}
        for ingredient,amount in dish.items() :
            calculate_recipe[ingredient] = amount * int(number_dishes)
        context['recipe'] = calculate_recipe
        return render(request,'calculator/index.html',context)
    else :
        return HttpResponse('Рецепт не найден')
    