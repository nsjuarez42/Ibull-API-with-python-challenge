from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse,JsonResponse
from trades.models import Trade
from trades.serializers import TradeSerializer
import json

# Create your views here.
def tradesAPI(request):

    if request.method == 'POST':
      trade = json.loads(request.body)

      if ((trade["shares"] in range(1,100)) and (trade['type'] == "buy") or (trade["type"] == "sell")):

       trade_data = JSONParser().parse(request)
       trades_serializer = TradeSerializer(data=trade_data)
       if trades_serializer.is_valid():
           trades_serializer.save()
           return JsonResponse(trades_serializer.data,status=201)
       else:
          print(trades_serializer.errors)
          return HttpResponse(status =400)    

      else:
       return HttpResponse(status=400)
   
    if request.method == 'GET':
        
       try: 
        if ("user_id" in request.GET) and ('type' in request.GET):
            user_id = request.GET.get('user_id')
            trade_type = request.GET.get('type')
            trades = Trade.objects.filter(user_id=user_id).filter(type=trade_type)
            trades_serializer = TradeSerializer(trades,many=True)
            return JsonResponse(trades_serializer.data,safe=False)         

        if 'type' in request.GET:
         trade_type = request.GET.get('type')
         trade = Trade.objects.filter(type=trade_type)
         trades_serializer = TradeSerializer(trade,many=True)
         return JsonResponse(trades_serializer.data,safe=False)

        if 'user_id' in request.GET:
         trade_user_id = request.GET.get("user_id")   
         trade= Trade.objects.filter(user_id=trade_user_id)
         trades_serializer = TradeSerializer(trade,many=True)
         return JsonResponse(trades_serializer.data,safe=False)
 

        else:    
         trades = Trade.objects.all()
         trades_serializer = TradeSerializer(trades,many=True)
         return JsonResponse(trades_serializer.data,safe=False)
       except Trade.DoesNotExist:  
        return HttpResponse(status=404)   

    else:
        return HttpResponse(status=405)

def tradesById(request,id):

    id = int(id)

    if request.method == 'GET':
     try:
      trade = Trade.objects.get(id=id)
      trades_serializer = TradeSerializer(trade,many=False)
      return JsonResponse(trades_serializer.data,safe=False)
     except Trade.DoesNotExist:
         return HttpResponse(status=404)

    if (request.method == 'DELETE'):
      try:  
       trade = Trade.objects.get(id=id)
       trade.delete()
       return HttpResponse(status=204)
      except Trade.DoesNotExist:
          return HttpResponse(status=404) 

    else:
        return HttpResponse(status=405) 

        