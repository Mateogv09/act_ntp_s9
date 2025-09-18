import pandas as pd

data = {...}
df = pd.DataFrame(data)

print("\nEmpleados cuyos nombres empiezan con 'M':")
print(df[df['nombre'].str.startswith('M')])

print("\nDepartamentos que contienen 'R':")
print(df[df['departamento'].str.contains('R')])
