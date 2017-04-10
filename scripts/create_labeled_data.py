from agro_db.csr.models import FarmerSegment, ProfileAddress, CropInformation
import csv
import django
django.setup()

segment_map = {
    'Diamond': 1,
    'Gold': 2,
    'Silver': 3,
    'Bronze': 4
}


def generate():
    farmers = FarmerSegment.objects.all()
    address = ProfileAddress.objects.all()
    crop = CropInformation.objects.all()
    print farmers.count()
    print address.count()
    print crop.count()
    rows = [[
        'Farmer Id',
        'Village',
        'Taluka',
        'District',
        'State',
        'Crop',
        'Area',
        'App Customer',
        'Orders Count',
        'Net Orders Count',
        'Net Revenue',
        'Return Percentage',
        'Days Since Last Bought',
        'Segment'
    ]]
    for farmer in farmers:
        row = []
        fid = farmer.farmer_id if farmer.farmer_id else ""
        row.append(str(fid))
        if fid:
            farmer_address = address.filter(farmer=fid)
            print fid
            if farmer_address:
                farmer_address = farmer_address[0]
                village = farmer_address.village if farmer_address.village else ''
                row.append(str(village.encode('utf-8')))
                taluka = farmer_address.taluka if farmer_address.taluka else ''
                row.append(str(taluka.encode('utf-8')))
                district = farmer_address.district if farmer_address.district else ''
                row.append(str(district.encode('utf-8')))
                state = farmer_address.state if farmer_address.state else ''
                row.append(str(state.encode('utf-8')))
            else:
                row.append('')
                row.append('')
                row.append('')
                row.append('')

            farmer_crop = crop.filter(farmer=fid)
            if farmer_crop:
                farmer_crop = farmer_crop[0]
                fcrop = farmer_crop.crop if farmer_crop.crop else ''
                row.append(str(fcrop.encode('utf-8')))
                area = farmer_crop.area if farmer_crop.area else ''
                row.append(str(area))
            else:
                row.append('')
                row.append('')
        else:
            row.append('')
            row.append('')
            row.append('')
            row.append('')
            row.append('')
            row.append('')

        app_score = 1 if farmer.app_customer_score else 0
        row.append(str(app_score))
        order_count = farmer.orders_count if farmer.orders_count else 0
        row.append(str(order_count))
        net_orders = farmer.net_orders_count if farmer.net_orders_count else 0
        row.append(str(net_orders))
        net_revenue = farmer.net_revenue if farmer.net_revenue else 0
        row.append(str(net_revenue))
        return_percentage = farmer.return_percentage if farmer.return_percentage else 0
        row.append(return_percentage)
        days_since_last_bought = farmer.days_since_last_bought if farmer.days_since_last_bought else 1500
        row.append(days_since_last_bought)
        segment = farmer.segment if farmer.segment else ''
        segment_label = segment_map[str(segment)]
        row.append(str(segment_label))
        rows.append(row)

    f = open('customer_segmentation.csv', 'wb')
    w = csv.writer(f)
    w.writerows(rows)
    f.close()


if __name__ == '__main__':
    generate()
