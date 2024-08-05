# color = {'red', 'blue', 'pink'}
# color.remove('red')
# print(color)
# color.discard('red')
# print(color)
# color.clear()
# print(color)
# people = {'hi', 'hello', 'hey'}
# udate = color.union(people)
# print(udate)
color = {'red', 'blue', 'pink'}
people = {'hi', 'hello', 'hey', 'red'}
# color.intersection_update(people)
# print(color)
# x= color.intersection(people)
# print(x)
color.difference_update(people)
print(color)