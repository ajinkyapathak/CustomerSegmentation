import csv


def weighted_algorithm():
    with open('dataset_with_cluters.csv') as csvfile, open('dataset_for_comparison_1.csv', 'wb') as outf:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Calculated.Segment']
        csvwriter = csv.DictWriter(outf, fieldnames)
        csvwriter.writeheader()

        for row in reader:
            net_order_score = get_net_order_score(row)
            total_revenue_score = get_total_revenue_score(row)
            return_percentage_score = get_return_percentage_score(row)
            days_since_last_active_score = get_days_since_last_active_score(row)
            total_score = net_order_score + total_revenue_score - (return_percentage_score + days_since_last_active_score)
            append_col = {'Calculated.Segment': segment(total_score)}
            new_row = dict(row.items() + append_col.items())
            csvwriter.writerow(new_row)


def get_net_order_score(row):
    net_orders_count = int(row['Net.Orders'])
    if net_orders_count >= 5:
        return 40
    elif net_orders_count >= 3:
        return 30
    elif net_orders_count >= 2:
        return 20
    elif net_orders_count >= 1:
        return 10
    else:
        return 0


def get_total_revenue_score(row):
    net_revenue = float(row['Net.Revenue'])
    if net_revenue >= 12500:
        return 40
    elif net_revenue >= 8000:
        return 30
    elif net_revenue >= 5000:
        return 20
    elif net_revenue >= 2500:
        return 10
    else:
        return 0


def get_return_percentage_score(row):
    return_percentage = float(row['Return.Percentage'])/100
    if return_percentage >= 0.75:
        return 40
    elif return_percentage >= 0.5:
        return 30
    elif return_percentage >= 0.25:
        return 20
    elif return_percentage >= 0.1:
        return 10
    else:
        return 0


def get_days_since_last_active_score(row):
    days_since_last_bought = int(row['Last.Bought.on'])
    if days_since_last_bought >= 750:
        return 40
    elif days_since_last_bought >= 550:
        return 30
    elif days_since_last_bought >= 365:
        return 20
    elif days_since_last_bought >= 180:
        return 10
    else:
        return 0


def segment(total_score):
    if total_score >= 40:
        return 1
    elif total_score >= 0:
        return 2
    elif total_score >= -40:
        return 3
    else:
        return 4


if __name__ == '__main__':
    weighted_algorithm()