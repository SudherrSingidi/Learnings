
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
# extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']


def extract_full_name(names):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']),names))
print(extract_full_name(names))