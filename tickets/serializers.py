from rest_framework import serializers
from .models import Ticket, Person
from .email import notify_ticket_to_admin
PRICE = 12

class TicketSerializer(serializers.ModelSerializer):
    companions = serializers.ListField(child=serializers.CharField(), write_only=True,  required=False)
    class Meta:
        model = Ticket
        fields = '__all__'
        depth = 1       

    def create(self, validated_data):
        companions_data = validated_data.pop('companions', [])  # Extrae la lista de acompañantes
        validated_data['price'] = PRICE + len(companions_data) * PRICE
        ticket = Ticket.objects.create(**validated_data)
        ticket.save()
        
        Person.objects.create(name=validated_data['titular'], ticket=ticket)
        # Crea un número de acompañantes igual a la longitud de la lista de acompañantes
        for companion_name in companions_data:
            Person.objects.create(name=companion_name, ticket=ticket)
        notify_ticket_to_admin(ticket)
        return ticket


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

