import re

def split_alloy(alloy_name):
    assert type(alloy_name) == str
    element_split = re.findall('[A-Z][^A-Z]*', alloy_name)
    element_dict = {}
    for element in element_split:
        item = element
        match = re.match(r"([a-z]+)([0.-9.]+)", element, re.I)
        if match:
            item = match.groups()
            element_dict[item[0]] = float(item[1])
        else:
            element_dict[item] = 1
    return (element_dict)

def get_feature_set(element_dict, elm_data):
    # features to extract
    w_R = 0
    w_D = 0
    w_VEC = 0
    w_T = 0
    w_k = 0
    # get sum of composition values
    sum_comp = sum(list(element_dict.values()))

    for E in list(element_dict.keys()):
        #getting index of element from elm_data
        index_E = elm_data.Element[elm_data.Element == E].index[0]

        w_R += element_dict[E] * elm_data['At. rad. (pm)'][index_E]
        w_D += element_dict[E] * elm_data['dens (g/cc)'][index_E]
        w_VEC += element_dict[E] * elm_data['VEC'][index_E]
        w_T += element_dict[E] * elm_data['Tm(K)'][index_E]
        w_k += element_dict[E] * elm_data['K'][index_E]
    
    feature_set = [w_R, w_D, w_VEC, w_T, w_k]
    feature_set = [w/sum_comp for w in feature_set]
    return [feature_set]

'''Testing'''
# e_dict = split_alloy("Ni0.0Cr0.0Fe0.0Mo0.0W1.0")
# features = get_feature_set(e_dict, LoadData.element_data())
# print(features)


