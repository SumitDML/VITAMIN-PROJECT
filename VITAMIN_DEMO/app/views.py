from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.util import switch, switcher
from datetime import datetime


@api_view(['GET'])
def get_tabs(request):
    tabId = request.GET.get('tabId')
    try:

        if tabId is None or len(tabId) == 0:
            parents = Tabs.objects.all()
            if not parents.exists():
                return Response({
                    'status': False,
                    'message': "No Records Found!",
                }, status=status.HTTP_404_NOT_FOUND)
            serializer = TabSerializer(parents, many=True)
            return Response({
                'status': True,
                'message': "Data Fetched Successfully!",
                'data': serializer.data
            })

        else:
            parents = Tabs.objects.filter(tab_id=tabId)
            if not parents.exists():
                return Response({
                    'status': False,
                    'message': "No Records Found!",
                }, status=status.HTTP_404_NOT_FOUND)
            serializers1 = TabSerializer(parents, many=True)
            return Response({
                'status': True,
                'message': "Data Fetched Successfully!",
                'data': serializers1.data
            })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': "Some Error Occured!",
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_tab_childs(request):
    tabId = request.GET.get('tab_id')
    if tabId is None or len(tabId) == 0:
        return Response({
            'status': False,
            'message': "Tab Id is required!",
        }, status=status.HTTP_400_BAD_REQUEST)

    try:

        all_childs = TabChild.objects.filter(tab_id=tabId)
        if not all_childs.exists():
            return Response({
                'status': False,
                'message': "No Childs Found!",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = TabChildSerializer(all_childs, many=True, context={'request': request})
    except Exception as e:
        return Response({
            'status': False,
            'message': "Something went wrong!",
        }, status=status.HTTP_400_BAD_REQUEST)
    return Response({
        'status': True,
        'message': "Fetched Successfully!!",
        'data': serializer.data
    })


@api_view(['GET'])
def get_child_data(request):
    tabId = request.GET.get('tab_id')
    if tabId is None or len(tabId) == 0:
        return Response({
            'status': False,
            'message': "Tab Id is required!",
        }, status=status.HTTP_400_BAD_REQUEST)

    tabChildId = request.GET.get('tab_child_id')

    if tabChildId is None or len(tabChildId) == 0:
        return Response({
            'status': False,
            'message': "Tab_Child Id is required!",
        }, status=status.HTTP_400_BAD_REQUEST)

    page_number = request.GET.get('page_number')

    try:
        all_childs = TabChild.objects.filter(tab_id=tabId)

        if not all_childs.exists():
            return Response({
                'status': False,
                'message': "No Child Record Found!",
            }, status=status.HTTP_404_NOT_FOUND)
        result = all_childs.filter(tab_child_id=tabChildId)

        if not result.exists():
            return Response({
                'status': False,
                'message': "Invalid child Id!",
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = TabChildNameSerializer(result, many=True, context={'request': request})
        name = serializer.data[0].get('name')
        model = switch(name)
        serializer1 = getGenericSerializer(model)
        data = model.objects.all().order_by('id')
        p = Paginator(data, 25)
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger or EmptyPage:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        serialized_data = serializer1(page_obj, many=True, context={'request': request})
        totalPages = p.page_range.stop - 1
        return Response({
            'status': True,
            'message': "Fetched Successfully!!",
            'tab_id': tabId,
            'page_size': totalPages,
            'data': serialized_data.data

        })
    except AttributeError:
        return Response({
            'status': True,
            'message': "Child Module Not Found!",
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            'status': True,
            'message': "Something Went Wrong!",
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_data(request):
    tab_id = request.GET.get('tab_id')
    if tab_id is None or len(tab_id) == 0:
        return Response({
            'status': False,
            'message': "Tab Id is required!",
        }, status=status.HTTP_400_BAD_REQUEST)
    try:

        all_childs = TabChild.objects.filter(tab_id=tab_id)

        if not all_childs.exists():
            return Response({
                'status': False,
                'message': "No Child Record Found!",
            }, status=status.HTTP_404_NOT_FOUND)

        if int(tab_id) == 3:
            search = request.GET.get('search')
            nutrient_data = Nutrients.objects.filter(Nutrient__istartswith=search)
            if len(nutrient_data) == 0:
                return Response({
                    'status': False,
                    'message': "No data!",
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer3 = NutrientsSerializer(nutrient_data, many=True, context={'request': request})
            return Response({
                'status': True,
                'message': "Fetched Successfully!!",
                'data': serializer3.data,
            })

        elif int(tab_id) == 1:
            zip_code = request.GET.get('search')
            zone = all_childs.filter(name='Zones')
            serializer = TabChildNameSerializer(zone, many=True, context={'request': request})
            zone_name = serializer.data[0].get('name')
            latitude = ZipCodes.objects.get(zip_code=zip_code).latitude

            if latitude > 0:
                zone_data = switch(zone_name).objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude,
                                                             NorthSouth='N')
            else:
                zone_data = switch(zone_name).objects.filter(LatitudeMin__lte=latitude, LatitudeMax__gte=latitude,
                                                             NorthSouth='S')

            serializer1 = ZoneViewSerializer(zone_data, many=True, context={'request': request})
            result = serializer1.data
            today = datetime.now()
            for itr in result:
                sunshine_data = SunshineAvailability.objects.filter(ZoneID=itr['id']).filter(Month=today.month)
                serializer2 = SunshineAvailabilitySerializer(sunshine_data, many=True, context={'request': request})
            return Response({
                'status': True,
                'message': "Fetched Successfully!!",
                'zones': serializer1.data,
                'sunshine': serializer2.data
            })
        else:
            return Response({
                'status': False,
                'message': "Nothing to search!",
            }, status=status.HTTP_400_BAD_REQUEST)
    except ZipCodes.DoesNotExist:
        return Response({
            'status': False,
            'message': "Invalid Zip-Code!",
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': "Something went wrong!",
    }, status=status.HTTP_400_BAD_REQUEST)
