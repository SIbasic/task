import json
with open("tests.json") as tests:
    test= json.load(tests)
with open("values.json") as values:
    value= json.load(values)

dicWith=[]
dicWithOut=[]
updateddic=[]

def updater():
    for dic in dicWithOut:
        for dic2 in value['values']:
           if dic['id'] == dic2['id']:
               dic['value'] = dic2['value']
        updateddic.append(dic)

for dic in test['tests']:
    if 'values' in list(dic.keys()):
        dicWith.append(dic)
        for dic2 in dic['values']:
            if 'values' in list(dic2.keys()):
                dicWith.append(dic2)
                for dic3 in dic2['values']:
                    if 'values' in list(dic3.keys()):
                        dicWith.append(dic3)
                        for dic4 in dic3['values']:
                            if 'values' in list(dic4.keys()):
                                dicWith.append(dic4)
                                for dic5 in dic4['values']:
                                    if 'values' in list(dic5.keys()):
                                        dicWith.append(dic5)
                                        for dic6 in dic5['values']:
                                            if 'values' in list(dic6.keys()):
                                                dicWith.append(dic6)
                                                for dic7 in dic6['values']:
                                                    if 'values' in list(dic7.keys()):
                                                        dicWith.append(dic7)
                                                    else:
                                                        dicWithOut.append(dic7)
                                            else:
                                                dicWithOut.append(dic6)
                                    else:
                                        dicWithOut.append(dic5)
                            else:
                                dicWithOut.append(dic4)
                    else:
                        dicWithOut.append(dic3)
            else:
                dicWithOut.append(dic2)
    else:
        dicWithOut.append(dic)

updater()
print(updateddic)

