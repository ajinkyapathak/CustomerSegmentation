from agro_db.order_management.models import CallTagMapping
from agro_db.csr.models import Farmer
from agro_db.ticketing.models import Ticket
from datetime import datetime
import math
import django
django.setup()
from django.db.models import Q


def get_last_active_info(farmer_id):
    tags = CallTagMapping.objects.filter(farmer=farmer_id).order_by('-created_on').values_list('created_on', flat=True)
    if not tags:
        return None
    else:
        tag = tags[0]
        days = (datetime.today().date() - tag.date()).days
        weeks = int(math.ceil(float(days) / 7))
        if days < 7:
            if days == 1:
                return 'Yesterday'
            else:
                return '{} days ago'.format(days)
        elif weeks == 1:
            return '{} week ago'.format(weeks)
        else:
            return '{} weeks ago'.format(weeks)


def get_farmer_joined_year(farmer_id):
    farmer = Farmer.objects.filter(farmer_id=farmer_id)
    farmer = list(farmer)
    year = farmer[0].created_on.year
    return year


def get_open_tickets_info(farmer_id):
    open_tickets = Ticket.objects.filter(farmer_id=farmer_id).exclude(Q(status='closed') | Q(status='resolved')).count()
    return open_tickets


def handle_request(request):
    farmer_id = request['farmerId']
    last_tag = get_last_active_info(farmer_id)
    open_tickets = get_open_tickets_info(farmer_id)
    joined_agrostar = get_farmer_joined_year(farmer_id)
    print 'last active {}'.format(last_tag)
    print 'open tickets {}'.format(open_tickets)
    print 'joined agrostar {}'.format(joined_agrostar)


if __name__ == '__main__':
    request = {
        'farmerId': 541526
    }
    handle_request(request)
