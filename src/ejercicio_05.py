import pandas as pd

data = {...}
df = pd.DataFrame(data)

print("\nEmpleados de IT con más de 30 años Y salario > 60,000:")
print(df[(df['departamento'] == 'IT') & (df['edad'] > 30) & (df['salario'] > 60000)])

print("\nEmpleados cuyo nombre empieza con 'L' O son de RRHH:")
print(df[(df['nombre'].str.startswith('L')) | (df['departamento'] == 'RRHH')])
