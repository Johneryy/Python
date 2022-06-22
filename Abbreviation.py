def abbrevation(name):
    return '.'.join(w[0] for w in name.split()).upper()

Name = input("Enter your full name-> ")
print(abbrevation(Name))