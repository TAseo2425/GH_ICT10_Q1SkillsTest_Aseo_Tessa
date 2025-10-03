from pyscript import display, document

# Header + Footer
restaurant = 'BAMYUM'
system = 'Food Ordering System'


display(f'{restaurant}', target='name')
display(f'{system}', target='system')


def summary_order(k):
#Customer Details
    customer_mobile = document.getElementById('cnumb').value
    customer_name = document.getElementById('cname').value
    customer_address = document.getElementById('caddress').value

#Menu
    gh_amt = int(document.getElementById("gilded_hall").value)
    at_amt = int(document.getElementById("almond_tofu").value)
    jp_amt = int(document.getElementById("jade_parcels").value)
    c_amt = int(document.getElementById("cassoulet").value)
    cs_amt = int(document.getElementById("crystal_shrimp").value)

    gh_price = 1331
    at_price = 1200
    jp_price = 750
    c_price = 250
    cs_price = 130

    gh_total = gh_amt * gh_price
    at_total = at_amt * at_price
    jp_total = jp_amt * jp_price
    c_total = c_amt * c_price
    cs_total = cs_amt * cs_price

    total = gh_total + at_total + jp_total + c_total + cs_total

    document.getElementById('output').innerHTML = " "

    display(f'Order for: {customer_name}', target='output')
    display(f'Address: {customer_address}', target='output')
    display(f'Number: {customer_mobile}', target='output')
    display(f'Your total is ₱{total}.', target='output')
