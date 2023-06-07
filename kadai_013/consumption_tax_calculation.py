# %%

def add_tax(amount, tax_rate=10):
    '''
    amount : int
    tax_rate : int
    tax = amount * tax_rate

    return amount + tax
    '''
    try:
        amount = int(amount)
        if isinstance(tax_rate, str):
            tax_rate = int(tax_rate.replace('%', '')) / 100
        elif isinstance(tax_rate, float):
            tax_rate = tax_rate
        else:
            tax_rate = int(tax_rate) / 100
    except TypeError as e:
        print(e)
    else:
        tax = int(amount * tax_rate)

        return amount + tax, tax_rate

total_amount, tax_rate = add_tax(amount=1000)
print(f'{total_amount}(tax_rate:{tax_rate * 100}%)')

tax_rate_list = ['10%', 0.1, 10, 'aaa%']

for tax_rate in tax_rate_list:
    total_amount, tax_rate = add_tax(amount=1000, tax_rate=tax_rate)

    print(f'{total_amount}(tax_rate:{tax_rate * 100}%)')

# %%
