class SimpleLinearRegression:
    def __init__(self):
        # Hardcoded dataset
        self.advertising = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sales = [2, 4, 6, 8, 10, 12, 14, 16, 18]
        self.beta_0 = 0
        self.beta_1 = 0

    def calcular_coeficientes(self):
        n = len(self.sales)
        sum_x = sum(self.advertising)
        sum_y = sum(self.sales)
        sum_x_squared = sum(x ** 2 for x in self.advertising)
        sum_xy = sum(x * y for x, y in zip(self.advertising, self.sales))

        # Fórmulas para calcular beta_0 y beta_1
        self.beta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
        self.beta_0 = (sum_y - self.beta_1 * sum_x) / n

    def imprimir_ecuacion(self):
        print(f"Ecuación de regresión: y = {self.beta_0:.2f} + {self.beta_1:.2f} * x")

    def predecir(self, x):
        return self.beta_0 + self.beta_1 * x

# Clase para ejecución del programa
class Main:
    @staticmethod
    def main():
        modelo = SimpleLinearRegression()
        modelo.calcular_coeficientes()
        modelo.imprimir_ecuacion()
        
        # Inyección de valores desde la terminal
        while True:
            x = float(input("Ingrese el valor de publicidad (Advertising) para predecir ventas (Sales): "))
            y_pred = modelo.predecir(x)
            print(f"Predicción de ventas (Sales): {y_pred:.2f}")

# Ejecución del programa
if __name__ == "__main__":
    Main.main()
