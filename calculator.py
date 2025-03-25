class Calculator:
    """
    Una calculadora básica que realiza operaciones aritméticas simples.
    """

    def add(self, a, b):
        """
        Suma dos números.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: La suma de a y b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Resta dos números.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: La diferencia entre a y b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplica dos números.

        Args:
            a (float): El primer número.
            b (float): El segundo número.

        Returns:
            float: El producto de a y b.
        """
        return a * b

    def divide(self, a, b):
        """
        Divide dos números.

        Args:
            a (float): El numerador.
            b (float): El denominador.

        Returns:
            float: El cociente de a y b.

        Raises:
            ValueError: Si b es 0.
        """
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b


# Ejemplo de uso
if __name__ == "__main__":
    calc = Calculator()

    print("Suma: ", calc.add(10, 5))
    print("Resta: ", calc.subtract(10, 5))
    print("Multiplicación: ", calc.multiply(10, 5))
    print("División: ", calc.divide(10, 5))