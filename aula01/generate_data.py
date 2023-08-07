"""
Geração de base de dados faker para curso de Power Bi (PB)
São 3 tabelas a serem geradas conforme arquivo aulas-power-bi.drawio aula01
Os dados são gerados com nomes despadronizados para corrigir dentro do PB
"""
from random import randrange
from aula01.classes.product.product import Product
from aula01.classes.product.product_db import create_products, get_products, to_csv_products
from aula01.classes.customer.customer_db import create_customers, to_csv_customers, get_customers
from aula01.classes.customer.customer import Customer
from aula01.classes.seller.seller_db import create_sellers, to_csv_sellers, get_sellers
from aula01.classes.seller.seller import Seller
from aula01.classes.order.order_db import create_orders, to_csv_orders
from aula01.classes.order.order import Order

# Tabela de produtos
products = [
    Product("Xiaomi Redmi Note 12", "Smartphone", 3.590),
    Product("Motorola Edge 30 Pro 5G", "Smartphone", 2.789),
    Product("Xiaomi Poco X5", "Smartphone", 4.269),
    Product("Apple iPhone 13", "Smartphone", 4.149),
    Product("Samsung Galaxy A54", "Smartphone", 1.229),
    Product("Motorola Edge 30 Fusion 5G", "Smartphone", 1.589),
    Product("Xiaomi Redmi 12C", "Smartphone", 2.919),
    Product("Apple iPhone 11", "Smartphone", 5.389),
    Product("Samsung Galaxy S21", "Smartphone", 2.319),
    Product("Motorola Edge 30 Neo 5G", "Smartphone", 3.131),
    Product("Apple iPhone 14", "Smartphone", 2.789),
    Product("Motorola Moto G73 5G", "Smartphone", 1.899),
    Product("Xiaomi Poco X5", "Smartphone", 3.279),
    Product("Motorola Edge 30 Ultra 5G", "Smartphone", 3.519),
    Product("MacBook Air M1", "Notebook", 6.219),
    Product("Acer Aspire 5 – A515-45-R4ZF", "Notebook", 5.109),
    Product("Samsung Book Core I5-1135G7", "Notebook", 4.719),
    Product("Acer Aspire 5 A515-56-32PG", "Notebook", 4.561),
    Product("Lenovo IdeaPad 3i I5-1135G7", "Notebook", 4.879),
    Product("Lenovo IdeaPad Flex 5i I5-1235U", "Notebook", 5.119),
    Product("Lenovo IdeaPad Flex 5i I7-1255U", "Notebook", 6.119),
    Product("MacBook Air M2", "Notebook", 8.279),
    Product("Lenovo Ultrafino IdeaPad 3 Ryzen 5 5500U", "Notebook", 4.27)
]
create_products(products)
products_db = get_products()
to_csv_products("outputs/produtos.csv")

# Tabela de clientes
customers = [Customer() for _ in range(500)]
create_customers(customers)
customers_db = get_customers()
to_csv_customers("outputs/clientes.csv")

# Tabela de vendedores
sellers = [Seller() for _ in range(300)]
create_sellers(sellers)
sellers_db = get_sellers()
to_csv_sellers("outputs/vendedores.csv")

# Tabela de pedidos
orders = []
for _ in range(50000):
    customer = customers_db[randrange(0, len(customers_db)-1)]
    seller = sellers_db[randrange(0, len(sellers_db)-1)]
    product = products_db[randrange(0, len(products_db)-1)]

    orders.append(Order(customer_id=customer["id"],
                        seller_id=seller["id"],
                        product_id=product["id"],
                        quantity=randrange(1, 5),
                        product_price=product["price"]))

create_orders(orders)
to_csv_orders("outputs/vendas.csv")
