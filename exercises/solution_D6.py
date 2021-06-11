school_friends = {"Ali", "Sara", "Waleed", "Yasser"}
best_friends = {"Waleed", "Khaled", "Nor", "Ali"}

#1 Add Ahmed to best_friends
best_friends.add("Ahmed")
print(best_friends)

#2 Discard Yasser from school_friends 
school_friends.discard("Yasser")
print(school_friends)

#3 Intersection of school_friends and best_friends
int_friends = school_friends & best_friends
print(int_friends)

#4 Union of school_friends and best_friends
un_friends = school_friends | best_friends
print(un_friends)
