import pulp

problem = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40


problem += (2 * lemonade + 1 * fruit_juice <= water, "Water_Constraint")
problem += (1 * lemonade <= sugar, "Sugar_Constraint")
problem += (1 * lemonade <= lemon_juice, "Lemon_Juice_Constraint")
problem += (2 * fruit_juice <= fruit_puree, "Fruit_Puree_Constraint")

problem += lemonade + fruit_juice, "Total_Production"

problem.solve()

print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Optimal number of Lemonades to produce: {lemonade.varValue}")
print(f"Optimal number of Fruit Juices to produce: {fruit_juice.varValue}")

print(f"Total number of products: {pulp.value(problem.objective)}")
