import pandas as pd

data = {...}  # mismo diccionario
df = pd.DataFrame(data)

print("\nEmpleados de IT Y salario > 60,000:")
print(df[(df['departamento'] == 'IT') & (df['salario'] > 60000)])

print("\nEmpleados de Ventas O mayores de 40 años:")
print(df[(df['departamento'] == 'Ventas') | (df['edad'] > 40)])

print("\nEmpleados que NO son de Marketing:")
print(df[df['departamento'] != 'Marketing'])
