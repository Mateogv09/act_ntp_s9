import pandas as pd

data = {...}
df = pd.DataFrame(data)

print("\nEmpleados de IT o Ventas:")
print(df[df['departamento'].isin(['IT', 'Ventas'])])

print("\nEmpleados con edad 28, 35 o 42:")
print(df[df['edad'].isin([28, 35, 42])])
