import pulp

problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

problem += lemonade + fruit_juice, "Total_Production"

problem.solve()

print(f"Статус: {pulp.LpStatus[problem.status]}")
print(f"Кількість вироблених одиниць 'Лимонаду': {lemonade.varValue}")
print(f"Кількість вироблених одиниць 'Фруктового соку': {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {pulp.value(problem.objective)}")