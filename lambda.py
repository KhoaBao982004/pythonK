people = [
  {"name": "Harry", "house": "Grynffindor"},
  {"name": "Cho", "house": "Ravenclaw"},
  {"name": "Draco", "house": "Slytherin"}
]
#def lambda
'''
def f(person):
  return person["name"]

people.sort(key=f)

'''

#one-line lambda
people.sort(key=lambda person: person["name"])

print(people)


