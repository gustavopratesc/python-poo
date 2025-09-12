temperaturas_celsius = [0, 20, 30, 40]

temperatura_fahrenheint = map(lambda t: t * (9/5) + 32, temperaturas_celsius)

print(list(temperatura_fahrenheint))