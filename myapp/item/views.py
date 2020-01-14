from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import ItemSerializer, RecommendSerializer
from .models import Item

# Create your views here.
@api_view(['GET'])
def item_list(request):
    base_url = 'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/'
    
    items = Item.objects.all()
    skin_type = request.query_params.get('skin_type')
    category = request.query_params.get('category')
    exclude_ingredient = request.query_params.get('exclude_ingredient')
    include_ingredient = request.query_params.get('include_ingredient')

    if category:
        items = items.filter(category=category)
    if include_ingredient:
        include_ingredient = include_ingredient.split(',')
        for i in include_ingredient:
            items = items.filter(ingredients__contains=i)
    if exclude_ingredient:
        exclude_ingredient = exclude_ingredient.split(',')
        tmp = items.values('id', 'ingredients')
        for row in tmp:
            for i in exclude_ingredient:
                if i in row['ingredients']:
                    items = items.exclude(id=row['id'])

    if skin_type:
        tmp_items = items.order_by(f'-{skin_type}_point', 'price')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(tmp_items, request)

        for row in result_page:
            row.imageId = base_url + 'image/' + row.imageId + '.jpg'
        serializer = ItemSerializer(result_page, many=True, context={'request': request})

        return Response(serializer.data)
    else:
        return Response({'message': 'skin_type을 고르시오.'})


@api_view(['GET'])
def item_detail(request, item_pk):
    skin_type = request.query_params.get('skin_type')
    base_url = 'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/'
    
    if skin_type:
        item = get_object_or_404(Item, pk=item_pk)
        item.imageId = base_url + 'image/' + item.imageId + '.jpg' 
        item_category = item.category
        item_serializer = ItemSerializer(item)

        recommend = Item.objects.filter(category=item_category).order_by(f'-{skin_type}_point', 'price')[:3]
        for row in recommend:
            row.imageId = base_url + 'thumbnail/' + row.imageId + '.jpg'
        recommend_serializer = RecommendSerializer(recommend, many=True)
        
        result = recommend_serializer.data
        result.insert(0, item_serializer.data)
        return Response(result)
    else:
        return Response({'message': 'skin_type을 고르시오.'})