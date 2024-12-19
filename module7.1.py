import builtins
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name},{self.weight},{self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):

        file = open("products.txt", "r")
        string_file = file.read()
        file.close()
        return string_file

    def add(self, *products):

        new_s = self.get_products()
        file = open("products.txt", "a")
        for name in products:
            if name.name in new_s:
                print(f'Продукт {name} уже есть в магазине')
            else:
                file.write(name + "\n")
        file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
