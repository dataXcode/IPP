# Areas list
areas = [ "hallway", 14.35,
          "kitchen", 15.0, 
          "living room", 19.0,
          "bedroom", 12.5,
          "bathroom", 8.75 ]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)