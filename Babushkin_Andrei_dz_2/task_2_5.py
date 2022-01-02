price = [100.2, 58.65, 28, 32.2, 44.88, 25.9, 1058.25, 2958, 588.25, 65, 8.85, 15]

price_r_kk = []

for i in price:
    r = int(i)
    kk = round((i - r) * 100)
    i = "{:02} руб {:02} коп".format(r, kk)
    price_r_kk.append(i)
price_r_kk = ", ".join(price_r_kk)

print(price_r_kk)


print(id(price))
price.sort()

for i, item in enumerate(price):
    r = int(item)
    kk = round((item - r) * 100)
    item = "{:02} руб {:02} коп".format(r, kk)
    price[i] = item
price = ", ".join(price)

print(price, id(price))



new_price = [100.2, 58.65, 28, 32.2, 44.88, 25.9, 1058.25, 2958, 588.25, 65, 8.85, 15]
new_price.sort(reverse=True)

new_price_r_kk = []

for i in new_price:
    r = int(i)
    kk = round((i - r) * 100)
    i = "{:02} руб {:02} коп".format(r, kk)
    new_price_r_kk.append(i)
new_price_r_kk = ", ".join(new_price_r_kk)

print(new_price_r_kk)


new_price.sort()
for i, item in enumerate(new_price):
    r = int(item)
    kk = round((item - r) * 100)
    item = "{:02} руб {:02} коп".format(r, kk)
    new_price[i] = item
new_price = new_price[-5:]
new_price = ", ".join(new_price)
print(new_price)


