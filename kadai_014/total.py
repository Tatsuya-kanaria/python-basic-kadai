# %%
class PRODUCT:
    price1 = 100
    price2 = 200

class TAX:
    tax = 1.1

    def total(*price):
        return int(sum(price))

print (TAX.total(PRODUCT.price1, PRODUCT.price2) * TAX.tax)

# %%
