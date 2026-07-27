states = ["Lagos", "Oyo", "osun", "kwara"]
capital = ["ikeja", "ibadan", "osogbo", "ilorin"]
local_gov = ["Agege", "Ibadan west", "Ibrapa", "Ofa"]

Nigeria = [states, capital, local_gov]

for state in Nigeria:
    for city in state:
     print(city, end=" ")
    print()


