from django.db import models

line_of_cars = {'change_oil': [], 'inflate_tires': [], 'diagnostic': []}
ticket_no = 0
customers_served = 0
curr_customer = None


def pop_next_ticket_num():
    global customers_served, curr_customer
    if get_oil_tickets() > 0:
        customers_served += 1
        curr_customer = line_of_cars.get('change_oil')[0]
        line_of_cars.get('change_oil').remove(line_of_cars.get('change_oil')[0])
    elif get_inflate_tires_tickets() > 0:
        customers_served += 1
        curr_customer = line_of_cars.get('inflate_tires')[0]
        line_of_cars.get('inflate_tires').remove(line_of_cars.get('inflate_tires')[0])
    elif get_diagnostic_tickets() > 0:
        customers_served += 1
        curr_customer = line_of_cars.get('diagnostic')[0]
        line_of_cars.get('diagnostic').remove(line_of_cars.get('diagnostic')[0])


def peek_next_ticket_num():
    return curr_customer


def add_ticket(service):
    global ticket_no
    wait_time = calc_wait_time(service)
    ticket_no += 1
    line_of_cars.get(service).append(ticket_no)
    return ticket_no, wait_time


def get_oil_tickets():
    return len(line_of_cars.get('change_oil'))


def get_inflate_tires_tickets():
    return len(line_of_cars.get('inflate_tires'))


def get_diagnostic_tickets():
    return len(line_of_cars.get('diagnostic'))


def get_service_tickets_list(service):
    return line_of_cars.get(service)


def is_service_available(service):
    return service in line_of_cars.keys()


def calc_wait_time(service):
    if service == "change_oil":
        return get_oil_tickets() * 2
    elif service == "inflate_tires":
        return get_oil_tickets() * 2 +\
               get_inflate_tires_tickets() * 5
    elif service == "diagnostic":
        return get_oil_tickets() * 2 +\
               get_inflate_tires_tickets() * 5 +\
               get_diagnostic_tickets() * 30
