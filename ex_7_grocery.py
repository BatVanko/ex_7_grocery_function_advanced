def grocery_store(**kwargs):
    result = []
    sorted_products = sorted(kwargs.items(), key= lambda x : (-x[1], -len(x[0]),x[0]))
    for product_name, product_quantity in sorted_products:
        result.append(f'{product_name}: {product_quantity}')

    return '\n'.join(result)

print(grocery_store(
    bread=5,
    pasta=12,
    eggses=12,
))





