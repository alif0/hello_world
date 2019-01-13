colors = ["red", "green", "blue", "yello"]

print(colors[0])
print(colors[-1])

print(colors)

for i in colors:
	print(i)

colors[3] = "yellow"
for i in colors:
	print(i)

print(colors[1:2])
print(colors[1:])
print(colors[:4])
colors.reverse()   #does not return!
print(colors)
colors.sort()
print(colors)


leapyear = []
for year in range (1900, 1940):
  if (year % 4 == 0 and year % 100 !=0 ) or (year % 400 == 0):
    leapyear.append(year)

print(leapyear)

#list comprehension - expression and loop
leapyear2 = [x for x in range(1900, 1940)]
print (leapyear2)

#list comprehension - expression and loop with condition
leapyear2 = [x for x in range(1900, 1940) if (x % 4 == 0 and x % 100 !=0 ) or (x % 400 == 0)]
print (leapyear2)
