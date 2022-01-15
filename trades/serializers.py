from rest_framework import serializers
from trades.models import Trade

class TradeSerializer(serializers.ModelSerializer):
 class Meta:
     model=Trade
     fields=("id","type","user_id","symbol","shares","price","timestamp")
     
