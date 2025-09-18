import pandas as pd

# DataFrame base
data = {
    'nombre': ['Ana', 'Luis', 'Carmen', 'José', 'María', 'Pedro', 'Laura', 'Miguel'],
    'departamento': ['Ventas', 'IT', 'RRHH', 'Ventas', 'IT', 'Marketing', 'RRHH', 'IT'],
    'salario': [45000, 65000, 50000, 48000, 70000, 55000, 52000, 68000],
    'edad': [28, 35, 42, 31, 29, 38, 45, 33]
}
df = pd.DataFrame(data)

print("\nEmpleados con salario > 50,000:")
print(df[df['salario'] > 50000])

print("\nEmpleados menores de 35 años:")
print(df[df['edad'] < 35])

print("\nEmpleados del departamento IT:")
print(df[df['departamento'] == 'IT'])
