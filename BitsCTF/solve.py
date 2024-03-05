from z3 import *

# Define the bounds for each variable
bounds = [
    (2008, 67434882),
    (5828, 35387831),
    (2933, 30133881),
    (411, 63609725),
    (4223, 18566959),
    (1614, 25526751),
    (5679, 44298843),
    (6349, 26793895),
    (117, 40292840),
    (2321, 42293336),
    (2281, 26301527),
    (1939, 50793633),
    (6273, 51546489),
    (1477, 36871159),
    (800, 65314188),
    (4727, 15882817),
    (2828, 40562779),
    (1782, 48186923),
    (1744, 37382713),
    (2486, 56149154),
    (6312, 18170199),
    (2188, 63940428),
    (5380, 58244044),
    (1772, 29193116),
    (2708, 22309445),
    (1528, 40848052)
]

# Create 26 integer variables
x = [Int(f'x{i+1}') for i in range(26)]

# Create the solver
solver = Solver()

# Add the constraints for each variable
for i in range(26):
    solver.add(bounds[i][0] <= x[i])
    solver.add(x[i] < bounds[i][1])

# Add the equation constraint
solver.add(sum(x) == 69696969)

# Count the number of solutions
count = 0
while solver.check() == sat:
    count += 1
    model = solver.model()
    solver.add(Or([x[i] != model[x[i]] for i in range(26)]))

# Calculate the flag
flag = count % 69696969

# Wrap the flag in BITSCTF{}
flag = f'BITSCTF{{{flag}}}'

print(flag)
