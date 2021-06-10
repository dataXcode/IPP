s = ["Sara", 90, ["Waleed", 70], {"Ahmed" : 86.5, "Ali": 95}]

#1 Convert s list to t tuple
t = tuple(s)

# Print out t and t type
print(t)
print(type(t))

#2 Print out Ali grade 95
print(t[3]["Ali"])
