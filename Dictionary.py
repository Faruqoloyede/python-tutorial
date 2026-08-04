states = {"Abia":"Umaya",
          "Adamawa":"Yola",
          "Kwara": "Ilorin",
          "Lagos":"Ikeja",
          "Oyo":"Ibadan"}

# print(states.get("Lagos"))
# states.update({"osun": "osogbo"})
# states.update({"Abia": "Delta"})
# states.pop("Adamawa")
# states.popitem()
# states.clear()
# keys = states.keys()
# for key in keys:
#     print(key)
# values = states.values()
# for value in values:
#     print(value)
for key, value in states.items():
    print(f"{key} : {value}")