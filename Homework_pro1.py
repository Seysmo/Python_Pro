class Goods:

    def __init__(self, price, name, description, num_id):
        self.price = price
        self.name = name
        self.description = description
        self.num_id = num_id

    def fulldis(self):
        return f'{self.name}\nDescription:\n{self.description}\nPrice: {self.price}$, Code: {self.num_id}'

class Customer:

    def __init__(self, fname, sname, email):
        self.fname = fname
        self.sname = sname
        self.email = email

    def brief_view(self):
        return f'{self.fname} {self.sname}\n'

class Basket(Goods, Customer):

    items_in = 0

    def __init__(self, fname, sname, price, name, description, num_id, basket_items=None):
        super().__init__(price, name, description, num_id)
        if basket_items is None:
            self.basket_items = []
        else:
            self.basket_items = basket_items


    def add_item(self, b_item):
        if b_item not in self.basket_items:
            self.basket_items.append(b_item)

    def remove_item(self, b_item):
        if b_item in self.basket_items:
            self.basket_items.remove(b_item)

    def view_basket(self):
        for b_item in self.basket_items:
            print(super().brief_view(),'_________________________\n', b_item.fulldis())
        Basket.items_in += 1


good_1 = Goods(2_996.5, 'LG OLED', 'LG OLED77C1PUB 4K Smart OLED TV (2021)', 'N82E16889007773')
good_2 = Goods(1_996.99, 'Sony OLED', 'Sony OLED77C1PUB 8K Smart OLED TV (2021)', 'N82E16889007773')
good_3 = Goods(996.99, 'Samsung OLED', 'Samsung OLED77C1PUB UHD Smart OLED TV (2021)', 'N82E16889007773')

client_1 = Customer('John', 'Doe', 'johndoe@market.com.ua')

basket_it1 = Basket('', '', '', '', '', [])
basket_it1.add_item(good_2)
basket_it1.add_item(good_1)
basket_it1.add_item(good_3)

basket_it1.remove_item(good_3)
basket_it1.view_basket()
# print(good_1.fulldis())