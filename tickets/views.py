from django.views import View
from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import  add_ticket, is_service_available, pop_next_ticket_num, \
                    get_oil_tickets, get_inflate_tires_tickets, get_diagnostic_tickets, peek_next_ticket_num


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, f"tickets/index.html")


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, f"tickets/menu.html")


class TicketView(View):
    def get(self, request, service, *args, **kwargs):
        if not is_service_available(service.lower()):
            raise Http404
        ticket_no, wait_time = add_ticket(service)
        return render(request, f"tickets/ticket.html", context={'ticket_no':ticket_no,
                                                                'wait_time':wait_time})


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        change_oil_num = get_oil_tickets()
        inflate_tires_num = get_inflate_tires_tickets()
        diagnostic_num = get_diagnostic_tickets()
        next_ticket_num = peek_next_ticket_num()
        return render(request, f"tickets/operatormenu.html", context={'change_oil_num': change_oil_num,
                                                                      'inflate_tires_num': inflate_tires_num,
                                                                      'diagnostic_num': diagnostic_num,
                                                                      'next_ticket_num': next_ticket_num})

    def post(self, request, *args, **wargs):
        pop_next_ticket_num()
        return redirect("/next/")


class NextView(View):
    def get(self, request, *args, **kwargs):
        return render(request, f"tickets/next.html", context={'next_ticket_num': peek_next_ticket_num()})

