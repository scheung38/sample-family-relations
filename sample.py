from py2neo.data import Node, Relationship

a = Node("Person", name="Alice")
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)

print(ab)