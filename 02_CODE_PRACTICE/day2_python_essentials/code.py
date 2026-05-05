def washim(name):
    return f"Name: {name}"

print("AI Engineer:\n")
print(washim("Washim Akram"))    



#dictionaries

washim={
    "Age":25,
    "ID":1134,
    "NickName":"Akram",
    "homeTown":"Tangail",
    "AVG_study_hour":1.5,
    "is_healthy":True
}
print(washim["Age"])
for key, value in washim.items():
    print(key, ":", value)