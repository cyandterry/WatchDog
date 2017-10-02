BASE_URL = 'http://www.supremenewyork.com'


class ProductType:
    BAG = 'bags'
    TOP_SWEATERS = 'tops-sweaters'
    SHOE = 'shoes'
    SWEATSHIRT = 'sweatshirts'
    HAT = 'hats'
    ACCESSORY = 'accessories'
    SKATE = 'skate'
    SHIRT = 'shirts'
    JACKET = 'jackets'
    T_SHIRT = 't-shirts'
    PANTS = 'pants'


TOP_PRIORITY_PRODUCTS = [
    ProductType.BAG,
    ProductType.SWEATSHIRT,
    ProductType.T_SHIRT,
    ProductType.TOP_SWEATERS,
]


class InventoryActivityType:
    NEW_ITEM = 1
    AVAILABILITY_CHANGE = 2
