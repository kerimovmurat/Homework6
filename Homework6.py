# Работа со словарями:
my_dict = {'Safia': 2013, 'Lilya': 1989, 'Murat': 1987, 'Sanie': 2021}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Safia'])
print('Not existing value: ', my_dict.get('Kamila'))
my_dict.update({'Zarema': 1965, 'Marlen': 1963})
a = my_dict.pop('Marlen')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
# Работа с множествами:
my_set = {1, 2, 4, 'Lilya', 1, 4, 6}
print('Set: ', my_set)
my_set.add (5)
my_set.add ((5, 6.17, 10))
my_set.discard('Lilya')
print('Modified set: ', my_set)