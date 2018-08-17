
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv]]

house.extend([["bedroom",bed],["bathroom",bath]])
# Print out house

print(house)

# Print out the type of house
print(type(house))


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
area_liv = [areas.index(x) + 1  for x in areas if x == "living room"]
print(areas[area_liv[0]])

## print area of kitchen and bedroom
eat_sleep_area = []

# eat_sleep_area = [eat_sleep_area.append([areas.index(x) + 1]) for x in areas if x == 'kitchen' or x == 'bedrrom']
eat_sleep_area = [areas.index(x) + 1 for x in areas if x == 'kitchen' or x == 'bedroom']
print(areas[eat_sleep_area[0]] + areas[eat_sleep_area[1]])

print(eat_sleep_area)

# Use slicing to create downstairs
downstairs = areas[0:7]

# Use slicing to create upstairs
upstairs = areas[-5:-1]


print(downstairs)
print(upstairs)


# Correct the bathroom area
bath_area = [areas.index(x) + 1 for x in areas if x == 'bathroom']
print(bath_area)
areas[bath_area[0]] = 10.50
print(areas)


# Change "living room" to "chill zone"

chill_area = [areas.index(x) for x in areas if x == 'living room']
print(chill_area)
areas[chill_area[0]] = 'chill zone'
print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas[0:]
areas_1.extend(['poolhouse',24.5])
print(areas_1)
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1[:]
areas_2.extend(['garage',15.45])
print(areas_2)




















































