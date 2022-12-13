

def find(business_of_interest_id, positive_reviews):
    dict_result = {}
    for i in positive_reviews:
        if i.business_id in dict_result:
            dict_result[i.business_id].add(i.user_id)
        elif i.business_id not in dict_result:
            dict_result[i.business_id] = {i.user_id}

    result = dict_result[business_of_interest_id]
    counter = 0
    target = ""
    for business in dict_result.keys():
        users = dict_result[business]
        if business_of_interest_id == business:
            continue
        comparison = len(result.intersection(users))/len(result.union(users))
        if comparison > counter:
            counter = comparison
            target = business
    return target

