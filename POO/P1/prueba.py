class Calculadora:
    def __init__(self, numero1, numero2):
        """Constructor con atributos privados"""
        self.__numero1 = numero1
        self.__numero2 = numero2

    # Getter y Setter para numero1
    @property
    def numero1(self):
        return self.__numero1

    @numero1.setter
    def numero1(self, valor):
        if isinstance(valor, (int, float)):
            self.__numero1 = valor
        else:
            raise ValueError("El valor debe ser numérico")

    # Getter y Setter para numero2
    @property
    def numero2(self):
        return self.__numero2

    @numero2.setter
    def numero2(self, valor):
        if isinstance(valor, (int, float)):
            self.__numero2 = valor
        else:
            raise ValueError("El valor debe ser numérico")

    # Métodos de operaciones
    def sumar(self):
        return self.__numero1 + self.__numero2

    def restar(self):
        return self.__numero1 - self.__numero2

    def multiplicar(self):
        return self.__numero1 * self.__numero2

    def dividir(self):
        if self.__numero2 != 0:
            return self.__numero1 / self.__numero2
        else:
            return "Error: división entre cero"


# --- Programa principal con inputs ---
print("=== Calculadora POO ===")

# Pedir valores al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Crear objeto calculadora
calc = Calculadora(num1, num2)

# Menú de opciones
print("\nSeleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Opción: ")

if opcion == "1":
    print("Resultado:", calc.sumar())
elif opcion == "2":
    print("Resultado:", calc.restar())
elif opcion == "3":
    print("Resultado:", calc.multiplicar())
elif opcion == "4":
    print("Resultado:", calc.dividir())
else:
    print("Opción no válida")
