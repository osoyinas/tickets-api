from django.contrib import admin
from tickets.models import Ticket,Person
from .email import send_ticket_to_titular
# Register your models here.


def action_send_ticket(modeladmin, request, queryset):


    for ticket in queryset:
        # Mensaje específico para cada usuario\
        ticket.paid = True
        ticket.save()
        send_ticket_to_titular(ticket)



action_send_ticket.short_description = "Establecer como pagado y enviar entrada"
send_ticket_to_titular.short_description = "Enviar entrada"

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'titular','companions_count', 'paid','formatted_price', 'number', 'email', 'date']
    def formatted_price(self, obj):
        # Formatea el precio con un símbolo de dólar ($) y dos decimales
        return f"{obj.price:.2f}Є"
    
    def companions_count(self, obj):
        return obj.persons.count()
    companions_count.short_description = 'Personas'
    formatted_price.short_description = 'Precio'  # Define un encabezado personalizado para la columna
    search_fields = ['titular', 'email'] 
    list_filter = ['paid']
    sortable_by = ['price']
    actions= [action_send_ticket]

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'ticket_number', 'ticket_paid', 'ticket_contact', 'is_titular', 'checked')  # Añade los atributos de Ticket que quieras mostrar

    def ticket_number(self, obj):
        return obj.ticket.id  # Reemplaza 'number' con el nombre del atributo en el modelo Ticket
    ticket_number.short_description = 'Ticket ID'  # Etiqueta que se mostrará en la columna
    search_fields = ['name'] 

    def ticket_paid(self, obj):
        return "si" if obj.ticket.paid else "no"  # Reemplaza 'description' con el nombre del atributo en el modelo Ticket
    ticket_paid.short_description = 'Pagado'  # Etiqueta que se mostrará en la columna

    def ticket_contact(self, obj):
        return obj.ticket.number
    ticket_contact.short_description = 'Contacto'  # Etiqueta que se mostrará en la columna
    def is_titular(self,obj):
        return  "Titular" if obj.name == obj.ticket.titular else f"Acompañante de {obj.ticket.titular}"
    
    list_filter = ('ticket__paid',)
    sortable_by = ('ticket__date',)

    is_titular.short_description = 'titular'  # Etiqueta que se mostrará en la columna

            
