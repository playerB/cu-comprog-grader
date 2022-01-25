def read_orders(last_line):
    orders = []
    order = input().split()
    while order[0] != last_line:
        product, no = order[0], int(order[1])
        orders.append([product, no])
        order = input().split()
    return orders

def purchase(products, orders):
    purchased = []
    for product, no in orders:
        for i in range(len(products)):
            if product == products[i][0]:
                n = min(no, products[i][2])
                purchased.append([product, n, n * products[i][1]])
                products[i][2] -= n
                break
    return purchased

def read_products(n):
    products = []
    for i in range(n):
        product, price, stock = input().split()
        products.append([product, int(price), int(stock)])
    return products

def sort(purchased):
    x = []
    for product, no, p in purchased:
        x.append([p, product, no])
    x.sort()
    for i in range(len(x)):
        x[i][0], x[i][1], x[i][2] = x[i][1], x[i][2], x[i][0]
    return x

def report(store_name, purchased):
    total = 0
    print('---', store_name, '---')
    for product, no, p in purchased:
        print(">> {:18} {:>4} {:>8} Bahts".format(product, no, p))
        total += p
    print("--------------------")
    print("Total:", total, "Bahts")


def main():  # --- add your codes below
    store_name = input().strip()
    n = int(input().strip())
    report(store_name, sort(purchase(read_products(n), read_orders('q')))[::-1])
exec(input())  # DON'T remove this line

