my_dict = {'Gusya': 2021, 'Dasha': 2018}
print(my_dict) #{'Gusya': 2021, 'Dasha': 2018}
print(my_dict['Gusya']) #2021
print(my_dict.get('Bekki')) #None
my_dict.update({'Pipin': 2010,
                'Popug': 2011})
a = my_dict.pop('Popug')
print(a) #2011
print(my_dict) #{'Gusya': 2021, 'Dasha': 2018, 'Pipin': 2010}
my_set = {1, 2, 2, True, 9, (5, 6, 6), 'Hi', 'Hello', 'Hi'}
print(my_set) #{'Hello', 1, 2, 9, 'Hi', (5, 6, 6)}
print(my_set.add(7)) #None
print(my_set.add(8)) #None
print(my_set.discard(1)) #None
print(my_set) #{2, 'Hello', 8, 7, 'Hi', 9, (5, 6, 6)}