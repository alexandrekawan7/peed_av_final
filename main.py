from stack import Stack

class Product:
    def __init__(self, name, category, price, barcode, quantidy):
        self.name = name
        self.category = category
        self.price = price
        self.barcode = barcode
        self.quantity = quantidy

    def __dic__(self):
        return f"Product(name={self.name}, category={self.category}, price={self.price}, barcode={self.barcode}, quantidy = {self.quantity})"
    
    def value(self):
        return self.price * self.quantity



def add_product(stack):
        name = input("Enter the product name: ")
        category = input("Enter the product category: ")
        price = float(input("Enter the product price: $"))
        barcode = input("Enter the product barcode: ")
        quantity = int(input("Enter the product quantity: "))
        product = Product(name, category, price, barcode, quantity)
        stack.push(product)

   
def main():
    stack = Stack()
    while True:
        print("\n1. Adicionar produto")
        print("2. Imprimir pilha")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            add_product(stack)
            stack.push()
        elif escolha == "2":
            stack.print()
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
    