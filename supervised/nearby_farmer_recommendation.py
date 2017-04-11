import csv


def nearby_farmers_list(farmer_taluka, farmer_crop, farmer_district):
    with open('customer_segmentation.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        response_for_same_crop = []
        response_for_other_crop = []
        response_for_district = []
        for row in reader:
            if str(row['Taluka']).lower() == farmer_taluka.lower() and int(row['Segment']) <= 2 and str(
                    row['Crop']).lower() == farmer_crop.lower():
                ans = str(row['Farmer'] + '\t' + row['Crop'])
                response_for_same_crop.append(ans)

            elif str(row['Taluka']).lower() == farmer_taluka.lower() and int(row['Segment']) <= 2 and str(
                    row['Crop']).lower() != farmer_crop.lower():
                ans = str(row['Farmer'] + '\t' + row['Crop'])
                response_for_other_crop.append(ans)

            elif str(row['Taluka']).lower() != farmer_taluka.lower() and str(
                    row['District']).lower() == farmer_district.lower() and int(row['Segment']) <= 2:
                ans = str(row['Farmer'] + '\t' + row['Crop'])
                response_for_district.append(ans)

    csvfile.close()

    return response_for_same_crop, response_for_other_crop, response_for_district


def get_farmer_taluka():
    farmer_taluka = str(raw_input('Input Taluka of Farmer: '))
    farmer_district = str(raw_input('Input District of Farmer: '))
    farmer_crop = str(raw_input('Input Crop of Farmer: '))
    return farmer_taluka, farmer_crop, farmer_district


if __name__ == '__main__':
    taluka, crop, district = get_farmer_taluka()
    responses, response_for_different_crops, response_for_district = nearby_farmers_list(taluka, crop, district)
    if not response_for_different_crops and not responses and not response_for_district:
        print 'No Recommendation For this Farmer.'
        exit(0)

    print 'Recommendation of farmers with same Crop.'
    print "Farmer" + "\t" + "Crop"
    for response in responses:
        print response

    print 'Recommendation of farmers with different Crop.'
    print "Farmer" + "\t" + "Crop"
    for response in response_for_different_crops:
        print response

    print 'Recommendation of farmers within District but Different Talukas.'
    print "Farmer" + "\t" + "Crop"
    for response in response_for_district:
        print response
