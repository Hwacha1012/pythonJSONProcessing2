# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import json
import ast
import collections;
with open('dm-users-21.json') as json_data:
    data_dict = json.load(json_data)
    #print(data_dict)
    print(type(data_dict))
    #data = data_dict.decode()
#test = ast.literal_eval(json.dumps(data_dict))

def parse_webhook(webhook_data):

    """
    :param webhook_data: POST data from tradingview, as a string.
    :return: Dictionary version of string.
    """

    data = ast.literal_eval(str(webhook_data))
    return data
convertedData = parse_webhook(data_dict)
#print(convertedData)
#print(type(test))



'''
def convert(data):
    if isinstance(data, basestring):

        return data.encode('utf-8')
    elif isinstance(data, collections.Mapping):
        print("b")
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        print("c")
        return type(data)(map(convert, data))
    else:
        print("d")
        return data

def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v))
        for k, v in dictionary.items())
'''
#convertedData = dict([(str(k), v) for k, v in data_dict.items()])

#print DATA
#convertedData = convert_keys_to_string(data_dict)
#print(convertedData)
#cData2 = json.loads(convertedData)
#convertedData = json.loads(data_dict.replace("'", "\""))

#convertedData = ast.literal_eval(data_dict)

test = [];
for key in convertedData:
    #print(key)
   if (convertedData.get(key).get('college') == 'Harvard'):
       test.append(key)
    #print(type(x))
    #if i.get('college') == 'Harvard':
     #   print(i)
print(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
