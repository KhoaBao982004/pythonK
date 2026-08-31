houses = {"Harry": "Grynffindor", "Draco": "Slytherin"}


houses["Hermione"] = "Grynffindor"
print(houses["Harry"])

print(houses)


#items() function gives you both the key (name) and value (house)
for name, house in houses.items():
  print(f"{name}: {house}")