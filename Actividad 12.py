def es_primo(n):
  """Función para verificar si un número es primo."""
  if n <= 1:
      return False
  for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
          return False
  return True

def suma_digitos(n):
  """Función para calcular la suma de los dígitos de un número."""
  return sum(int(d) for d in str(n))

def producto_digitos(a, b):
  """Función para calcular el producto de dos números."""
  return a * b

def mostrar_digitos_separados(n):
  """Función para mostrar los dígitos de un número por separado."""
  return ' '.join(str(n))

def main():
  # Leer dos números enteros
  a = int(input("Introduce el primer número: "))
  b = int(input("Introduce el segundo número: "))

  # Calcular la diferencia
  diferencia = abs(a - b)

  # Verificar condiciones y mostrar resultados
  if diferencia % 2 == 0:
      print(f"La suma de los dígitos de {a} y {b} es: {suma_digitos(a) + suma_digitos(b)}")
  elif es_primo(diferencia) and diferencia < 10:
      print(f"El producto de {a} y {b} es: {producto_digitos(a, b)}")
  elif str(diferencia).endswith('4'):
      print(f"Los dígitos de {a} por separado son: {mostrar_digitos_separados(a)}")
      print(f"Los dígitos de {b} por separado son: {mostrar_digitos_separados(b)}")

if __name__ == "__main__":
  main()
