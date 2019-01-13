## First program

name = "Welcome to Python!"
print(name)


name = """Welcome to Python!\
          Welcome to DevOps
		  Welcome to DataScience with Mohammed Ali!!!
      """
print(name)

name = "Welcome to Python!" + "\nWelcome to Devops" + "\nWelcome to DataScience with Mohammed Ali!!!"
print(name)


x = 10
y = str(x)
print(x)
print(type(x))
print(id(x))
print(y)
print(type(y))
print(id(y))


#print("hello", "{name}".format(name=name))

#name = input("Enter your name:")

#print("hello", "{name}".format(name=name))

cost = 99.0934

print("Cost of pen is :"+"cost".format(cost=cost))
print("Cost of pen is :"+"{cost:0.02f}".format(cost=cost))
