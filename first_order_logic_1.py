from z3 import * 


# define domain:
Person = DeclareSort("Person")

# Predicated:
Parent = Function('Parent',Person,Person,BoolSort())
Grandparent = Function('Grandparent',Person,Person,BoolSort())

#constant:
Jhon = Const('Jhon',Person)
Mary = Const('Mary',Person)
Joe = Const('Joe',Person)

# solver:
s = Solver()

# variables for rules:
x = Const('x',Person)
y = Const('y',Person)
z = Const('z',Person)


#rules: Parent(x,y) and parent(y,z) -> Grandfather(x,z)
s.add(ForAll([x,y,z],Implies(And(Parent(x,y),Parent(y,z)),Grandparent(x,z))))


#Facts:
s.add(Parent(Jhon,Mary))
s.add(Parent(Mary,Joe))


# Query: prove Grandparent(John, Joe)
s.push()
s.add(Not(Grandparent(Jhon, Joe)))
res = s.check()
print("Result:", res)   

if res == unsat:
    print("✅ Grandparent(John, Joe) is proved.")
else:
    print("❌ Cannot prove Grandparent(John, Joe).")