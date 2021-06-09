# Countries dictionary 
countries = {"Iraq" : "Baghdad", "Egypt" : "Cairo", "Jordan" : "Amman", "Saudi Arabia" : "Riyadh"}

#1 Check if Lebanon exist in countries
print("Lebanon" in countries)

#2 Add Lebanon : Beirut to countries
countries["Lebanon"] = "Beirut"
print(countries)

#3 Delete Lebanon from countries
del(countries["Lebanon"])
print(countries)

#4 Edit Iraq capital (Basra instead of Baghdad)
countries["Iraq"] = "Basra"
print(countries)
