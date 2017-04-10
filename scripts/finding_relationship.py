import csv


def relate():
    with open('dataset_for_comparison_1.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        total = 62929
        for i in range(1,5):

            for j in range(1,5):
                cnt_i = 0
                cnt_j = 0
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if int(row['result$cluster']) == i:
                        cnt_i += 1
                        if int(row['Calculated.Segment']) == j:
                            cnt_j += 1
                csvfile.seek(0)
                support = (float(cnt_i) / total) * 100
                print 'Support of {} {}: {}'.format(i, j, support)
                confidence = (float(cnt_j) / cnt_i) * 100
                print 'Confidence of {} {}: {}'.format(i, j, confidence)


if __name__ == '__main__':
    relate()