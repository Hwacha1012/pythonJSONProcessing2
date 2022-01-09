# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import json
import ast
import collections;

#change if using a different number of questions
numQuestions = 10
#change if using for a different school
curr_School = 'Harvard'

with open('dm-users-21.json') as json_data:
    data_dict = json.load(json_data)
    #print(data_dict)
    print(type(data_dict))
    #data = data_dict.decode()
#test = ast.literal_eval(json.dumps(data_dict))

with open('dm-users-matches-21.json') as json_data2:
    data_dict2 = json.load(json_data2)
    #print(data_dict)
    print(type(data_dict2))
    #data = data_dict.decode()
#test = ast.literal_eval(json.dumps(data_dict))

def parse_webhook(webhook_data):

    """
    :param webhook_data: POST data from tradingview, as a string.
    :return: Dictionary version of string.
    """

    data = ast.literal_eval(str(webhook_data))
    return data
convertedUserData = parse_webhook(data_dict)
convertedMatchData = parse_webhook(data_dict2)



responses = [];
users = [];
matches = [];
#matchesAvg = [];
usersNew = [];
for key in convertedUserData:
    #print(key)
   if (convertedUserData.get(key).get('college') == curr_School and convertedUserData.get(key).get('responses') is not None):
       #responses.append(convertedUserData.get(key).get('responses'))
       users.append(key)
    #print(type(x))
    #if i.get('college') == 'Harvard':
     #   print(i)
print(len(users))
#print(len(responses))

#print(convertedMatchData).get('32411')
#print(convertedMatchData).get('32412')

for key in users:
    #print(key)
    #print(type(convertedMatchData.get(key2)))
    if convertedMatchData.get(key) is not None:
        temp = convertedMatchData.get(key).get('ratings')
        usersNew.append(key)
        if len(temp) > 0:
            matches.append((sum(temp) / len(temp)))
        else:
            matches.append(None)


print(len(matches))

#print(matches)

for key in usersNew:
    responses.append(convertedUserData.get(key).get('responses'))
    #users.append(key)

print(len(responses))
#print(matches)
#print(convertedData)
#print(type(test))


#rows, cols = (numQuestions, 0)
#questionAvgMatchScore = [[0] * cols] * rows
#print(questionAvgMatchScore)

#only way I could get this to work due to variables being linked in some way, resulting in the original 2D array only containing values for one question
questionResults1 = []
questionResults2 = []
questionResults3 = []
questionResults4 = []
questionResults5 = []
questionResults6 = []
questionResults7 = []
questionResults8 = []
questionResults9 = []
questionResults10 = []

#test2 = 2
#print(responses)
#for question in range(test2):
for question in range(numQuestions):

    rows2, cols2 = (5, 0)
    questionResponsesMatch = [[0] * cols2] * rows2
    print(questionResponsesMatch)

    array0 = []
    array1 = []
    array2 = []
    array3 = []
    array4 = []

    for index, user in enumerate(responses):
        if user is not None and type(user) is not dict:
            #print(type(user))
            print(user)
            if len(user) < question+1:
                print("user[question] is None")
            elif user[question] == 0:
                array0.append(matches[index])
            elif user[question] == 1:
                array1.append(matches[index])
            elif user[question] == 2:
                array2.append(matches[index])
            elif user[question] == 3:
                array3.append(matches[index])
            elif user[question] == 4:
                array4.append(matches[index])
                #questionResponsesMatch[user[question]].append(user[question])
                #print(user[question])


    array0 = list(filter(None, array0))
    array1 = list(filter(None, array1))
    array2 = list(filter(None, array2))
    array3 = list(filter(None, array3))
    array4 = list(filter(None, array4))

    print(array0)
    print(sum(array0)/len(array0))
    print(array1)
    print(sum(array1)/len(array1))
    if question == 0:
        questionResults1.append(sum(array0) / len(array0))
        questionResults1.append(sum(array1) / len(array1))
        questionResults1.append(sum(array2) / len(array2))
        questionResults1.append(sum(array3) / len(array3))
        questionResults1.append(sum(array4) / len(array4))
    elif question == 1:
        questionResults2.append(sum(array0) / len(array0))
        questionResults2.append(sum(array1) / len(array1))
        questionResults2.append(sum(array2) / len(array2))
        questionResults2.append(sum(array3) / len(array3))
        questionResults2.append(sum(array4) / len(array4))
    elif question == 2:
        questionResults3.append(sum(array0) / len(array0))
        questionResults3.append(sum(array1) / len(array1))
        questionResults3.append(sum(array2) / len(array2))
        questionResults3.append(sum(array3) / len(array3))
        questionResults3.append(sum(array4) / len(array4))
    elif question == 3:
        questionResults4.append(sum(array0) / len(array0))
        questionResults4.append(sum(array1) / len(array1))
        questionResults4.append(sum(array2) / len(array2))
        questionResults4.append(sum(array3) / len(array3))
        questionResults4.append(sum(array4) / len(array4))
    elif question == 4:
        questionResults5.append(sum(array0) / len(array0))
        questionResults5.append(sum(array1) / len(array1))
        questionResults5.append(sum(array2) / len(array2))
        questionResults5.append(sum(array3) / len(array3))
        questionResults5.append(sum(array4) / len(array4))
    elif question == 5:
        questionResults6.append(sum(array0) / len(array0))
        questionResults6.append(sum(array1) / len(array1))
        questionResults6.append(sum(array2) / len(array2))
        questionResults6.append(sum(array3) / len(array3))
        questionResults6.append(sum(array4) / len(array4))
    elif question == 6:
        questionResults7.append(sum(array0) / len(array0))
        questionResults7.append(sum(array1) / len(array1))
        questionResults7.append(sum(array2) / len(array2))
        questionResults7.append(sum(array3) / len(array3))
        questionResults7.append(sum(array4) / len(array4))
    elif question == 7:
        questionResults8.append(sum(array0) / len(array0))
        questionResults8.append(sum(array1) / len(array1))
        questionResults8.append(sum(array2) / len(array2))
        questionResults8.append(sum(array3) / len(array3))
        questionResults8.append(sum(array4) / len(array4))
    elif question == 8:
        questionResults9.append(sum(array0) / len(array0))
        questionResults9.append(sum(array1) / len(array1))
        questionResults9.append(sum(array2) / len(array2))
        questionResults9.append(sum(array3) / len(array3))
        questionResults9.append(sum(array4) / len(array4))
    elif question == 9:
        questionResults10.append(sum(array0) / len(array0))
        questionResults10.append(sum(array1) / len(array1))
        questionResults10.append(sum(array2) / len(array2))
        questionResults10.append(sum(array3) / len(array3))
        questionResults10.append(sum(array4) / len(array4))
'''
    for index, user in enumerate(responses):
        if user is not None and type(user) is not dict:
            #print(type(user))
            #print(user)
            if user[question] is not None:
                questionResponsesMatch[user[question]].append(matches[index])
                #questionResponsesMatch[user[question]].append(user[question])
                #print(user[question])
'''
        #else:
        #    print(usersNew[index])
        #if responses[index] is not None:
        #   questionResponsesMatch[responses[index][question]].append(matches[index])
        #else:
        #    print(index)

    #print(questionResponsesMatch[0])
    #print("Gap1")
    #print(questionResponsesMatch[1])
'''
  for i, val in enumerate(array0):
        if val is None:
            array0.pop(i)
    for j, val2 in enumerate(array1):
        if val2 is None:
            array1.pop(j)
    for k, val3 in enumerate(array2):
        if val3 is None:
            array2.pop(k)
    for l, val4 in enumerate(array3):
        if val4 is None:
            array3.pop(l)
    for o, val5 in enumerate(array4):
        if val5 is None:
            array4.pop(o)
'''


'''
    #should remove all Nones from list
    #print(len(questionResponsesMatch))
    for i in range(len(questionResponsesMatch)):
        for j, val in enumerate(questionResponsesMatch[i]):
            if val is None:
                questionResponsesMatch[i].pop(j)
'''
   # print(questionResponsesMatch[0])
    #print("Gap2")
   # print(questionResponsesMatch[1])

    #questionAvgMatchScore[question]
'''
    for x in range(len(questionResponsesMatch)):
        temp2 = (sum(questionResponsesMatch[x])/len(questionResponsesMatch[x]))
        questionAvgMatchScore[question][x] = temp2
        print(questionResponsesMatch[x])
        print(temp2)
        #if question > 1:
        #    print(question)
'''
print(questionResults1)
print(questionResults2)
print(questionResults3)
print(questionResults4)
print(questionResults5)
print(questionResults6)
print(questionResults7)
print(questionResults8)
print(questionResults9)
print(questionResults10)



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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
