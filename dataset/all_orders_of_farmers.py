import csv

import django
from agro_db.csr.models import Farmer, CropInformation, ProfileAddress
from agro_db.order_management.models import Order
from django.db.models import Q
from datetime import datetime

django.setup()


def gather_information():
    farmers = Farmer.objects.all().values_list('farmer_id', 'first_name', 'middle_name', 'last_name',
                                               'language', 'birth_date', 'app_enabled', 'mobile_1',
                                               'creation_source', 'irrigation_type',
                                               'irrigation_source')[300000:]
    rows = [[
        'Farmer Id',
        'First Name',
        'Middle Name',
        'Last Name',
        'Village',
        'Taluka',
        'District',
        'State',
        'Pincode',
        'Language',
        'Date Of Birth',
        'Android User',
        'Mobile Number',
        'Created at',
        'Crop',
        'Irrigation Type',
        'Irrigation Source',
        'Total Orders',
        'Net Orders',
        'Net Revenue',
        'Return Percentage',
        'Last Bought on'
    ]]

    for farmer in farmers:
        row = []
        id = farmer[0] if farmer[0] else None
        row.append(str(id))
        fname = farmer[1] if farmer[1] else " "
        row.append(fname.encode('utf-8'))
        mname = farmer[2] if farmer[2] else " "
        row.append(mname.encode('utf-8'))
        lname = farmer[3] if farmer[3] else " "
        row.append(lname.encode('utf-8'))

        addresses = ProfileAddress.objects.filter(farmer=id)
        address_list = list(addresses)
        if address_list:
            address = address_list[0]
            village = address.village if address.village else ''
            row.append(village)
            taluka = address.taluka if address.taluka else ''
            row.append(taluka)
            district = address.district if address.district else ''
            row.append(district)
            state = address.state if address.state else ''
            row.append(state)
            pin_code = address.pin_code if address.pin_code else ''
            row.append(pin_code)
        else:
            row.append('')
            row.append('')
            row.append('')
            row.append('')
            row.append('')

        lang = farmer[4] if farmer[4] else " "
        row.append(lang.encode('utf-8'))
        dob = farmer[5] if farmer[5] else " "
        row.append(str(dob))
        android = farmer[6] if farmer[6] else " "
        row.append(str(android))
        phn = farmer[7] if farmer[7] else " "
        row.append(phn.encode('utf-8'))
        created = farmer[8] if farmer[8] else " "
        row.append(str(created))
        crops = CropInformation.objects.filter(farmer=id).values_list('crop', flat=True)
        if crops:
            crop = crops[0] if crops[0] is not None else " "
            row.append(crop.encode('utf-8'))
        else:
            row.append(" ")
        ir_type = farmer[9] if farmer[9] else " "
        row.append(ir_type)
        ir_source = farmer[10] if farmer[10] else " "
        row.append(ir_source)

        orders = Order.objects.filter(~Q(unicommerce_status__in=["CANCELLED", "ERROR"]), owner=id)
        total_orders = orders.count()
        orders = orders.order_by('-created_on')
        return_count = Order.objects.filter(Q(unicommerce_status="RETURNED") | Q(status="RETURNED"), owner=id).count()
        orders = list(orders)
        if orders:
            row.append(total_orders)
            net_orders = total_orders - return_count
            row.append(net_orders)
            net_revenue = 0
            for order in orders:
                if order.unicommerce_status != 'RETURNED':
                    net_revenue += order.grand_total
            row.append(net_revenue)

            return_percentage = (float(return_count) / total_orders) * 100 if total_orders > 0 else 0
            row.append(return_percentage)
            last_order = orders[0]
            if last_order.created_on is not None:
                last_active = datetime.today().date() - last_order.created_on.date()
                last_active = last_active.days
            else:
                last_active = None
            row.append(last_active)

            rows.append(row)

    write_to_csv(rows)

def write_to_csv(rows):
    f = open('/tmp/dataset.csv','wb')
    w = csv.writer(f)
    w.writerows(rows)
    f.close()


if __name__ == '__main__':
    gather_information()
