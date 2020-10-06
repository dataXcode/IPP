# Areas list
areas = [ "hallway", 14.35,
          "kitchen", 15.0, 
          "living room", 19.0,
          "bedroom", 12.5,
          "bathroom", 8.75 ]

# Create areas_copy
areas_copy = list(areas)

# Change 8.75 to 10.0 in areas_copy
areas_copy[-1] = 10.0

# Print out areas_copy
print(areas_copy)
# Print out areas
print(areas)