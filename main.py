from typing import Self
from avl import AVLTree
from hash_table import HashTable
import quicksort
from my_queue import Queue
from stack import Stack

class Product:
    def __init__(self, name, category, price, barcode, quantidy) -> None:
        self.name: str = name
        self.category: str = category
        self.price: float = float(price)
        self.barcode: str = barcode
        self.quantity: int = int(quantidy)
    
    @staticmethod
    def register_product() -> Self:
        name = input("Type the product name: ")
        category = input("Type the product category: ")
        price = float(input("Type the product price: $"))
        barcode = input("Type the product barcode: ")
        quantity = int(input("Type the product quantity: "))
        product = Product(name, category, price, barcode, quantity)

        return product

    def __str__(self) -> str:
        return f"Product: {self.name}, Category: {self.category}, Price: {self.price}, Barcode: {self.barcode}, Quantidy: {self.quantity}"

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Product):
            return self.name < other.name
        elif isinstance(other, str):
            return self.name < other
        return False

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Product):
            return self.name > other.name
        elif isinstance(other, str):
            return self.name > other
        return False
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Product):
            return self.name == other.name or self.barcode == other.barcode
        else:
            return self.name == other

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Product):
            return self.name != other.name or self.barcode != other.barcode
        return False
    
    def value(self) -> float:
        return self.price * self.quantity
   
def main() -> str:
    avl = AVLTree()
    stack = Stack()
    hash_table = HashTable()
    queue = Queue()

    initial_dataset = [
    {"nome": "Smartphone XYZ", "categoria": "Smartphone", "preco": 1200.00, "codigo_barras": "1234567890123", "quantidade": 150},
    {"nome": "Laptop ABC", "categoria": "Laptop", "preco": 2500.00, "codigo_barras": "2345678901234", "quantidade": 60},
    {"nome": "Tablet QRS", "categoria": "Tablet", "preco": 800.00, "codigo_barras": "3456789012345", "quantidade": 25},
    {"nome": "Smartwatch LMN", "categoria": "Smartwatch", "preco": 400.00, "codigo_barras": "4567890123456", "quantidade": 100},
    {"nome": "Fone de Ouvido DEF", "categoria": "Acessórios", "preco": 150.00, "codigo_barras": "5678901234567", "quantidade": 200}]

    initial_products = []

    for p in initial_dataset:
        initial_products.append(Product(p["nome"], p["categoria"], p["preco"], p["codigo_barras"], p["quantidade"]))

    for i in initial_products:
        avl.insert(i)
        hash_table.set(i.barcode, i)


    while True:
        print("\nSelect the desired option:")
        print("1 - Add product")
        print("2 - Product search options")
        print("3 - Remove product")
        print("4. Manage Inventory (Stack)")
        print("5. Manage Orders (Queue)")
        print("6. List Products (QuickSort)")
        print("7 - Generate a report with all registered products")
        print("0 - End")

        op = input("\nChoose an option: ")

        if op not in ["1", "2", "3", "4", "5", "6", "7", "0"]:
            print("\nInvalid option. Please try again.")
            continue
        
        if op == "1":
            add_product: Product = Product.register_product()
            avl.insert(add_product)
            hash_table.set(add_product.barcode, add_product)

        elif op == "2":
            while True:
                print("\nSelect the product search option: ")
                print("1 - Name")
                print("2 - Category")
                print("3 - Barcode")
                print("4 - Exit")

                op3 = input("Choose an option: ")

                if op3 not in ["1", "2", "3", "4"]:
                    break

                if op3 == "1":
                    search_name = str(input("\nType the product name: "))
                    node = avl.search(search_name)

                    if node is not None:
                        print(str(node.value))
                    else:
                        print('No product found')
                elif op3 == "2":
                    search_category = input("\nType the product category: ")
            
                    products = avl.in_order()

                    for product in products:
                        if product.category == search_category:
                            print(str(product))
                elif op3 == "3":
                    search_barcode = input("\nType the product barcode: ")
                    product = hash_table.get(search_barcode)

                    if product is not None:
                        print(str(product))
                    else:
                        print(f'No product found')
                elif op3 == "4":
                    break    

        elif op == "3":
            name_input = str(input("Type the name of the product to remove: "))
            product_node = avl.search(name_input)

            if product_node is None:
                print(f'No product found with name {name_input}')
            else:
                product_to_remove = product_node.value

                avl.remove(product_to_remove.name)
                hash_table.remove(product_to_remove.barcode)

                print(f'Product removed with success')


        elif op == "4":
            print("Product replenishment")
            while True:
                print("\nSelect the option: ")
                print("1 - Add product")
                print("2 - Remove product")
                print("3 - View product replenishment stack")
                print("4 - Exit")

                op4 = input("Choose an option: ")

                if op4 not in ["1", "2", "3", "4"]:
                    print("\nInvalid option. Please try again.")
                    continue

                if op4 == "1":
                    list = [0] * 2
                    add_stack = str(input("\nType the product name: "))
                    q = int(input("Type the quantity desired: "))
                    list[0] = add_stack
                    list[1] = q
                    stack.push(list)

                elif op4 == "2":
                    list = [0] * 2
                    remove_stack = str("\nType the product name: ")
                    q = int(input("ype the quantity desired: "))
                    list[0] = remove_stack
                    list[1] = q
                    stack.pop(list)

                elif op4 == "3":
                    print(stack.print())
                elif op4 == "4":
                    break

        elif op == "5":
            print("Manage product orders")

            while True:
                print("\nSelect the option: ")
                print("1 - Add order")
                print("2 - Remove order")
                print("3 - View order management queue")

                op5 = input("Choose an option: ")

                if op5 not in ["1", "2", "3", "4"]:    
                    print("\nInvalid option. Please try again.")
                    continue
                
                if op5 == "1":
                    list = [0] * 2
                    add_queue = str(input("\nType the product name: "))
                    q = int(input("ype the quantity desired: "))
                    list[0] = add_queue
                    list[1] = q
                    queue.push(list)

                elif op5 == "2":
                    list = [0] * 2
                    remove_queue = str("\nType the product name: ")
                    q = int(input("ype the quantity desired: "))
                    list[0] = remove_queue
                    list[1] = q
                    queue.pop(list)

                elif op5 == "3":
                    print(queue.print())

                elif op5 == "4":
                    break
        elif op == "6":
            pass
        elif op == "7":
            pass

        elif op == "0":
            print("Exiting the program.")
            break

if __name__ == "__main__":
        main()
    