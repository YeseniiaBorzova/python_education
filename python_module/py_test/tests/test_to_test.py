from testfixtures import Replace, test_datetime
from functions_and_classes.to_test import *
import pytest


@pytest.mark.parametrize("x, expected",
                         [(4, 'even'),
                          (1, 'odd'),
                          (-12, "even"),
                          (-7, 'odd')])
def test_even_odd(x, expected):
    assert even_odd(x) == expected


def test_type_error_even_odd_input_str():
    with pytest.raises(TypeError):
        even_odd("feuygferuo")


def test_type_error_even_odd_input_list():
    with pytest.raises(TypeError):
        even_odd([4, 3, 2, 1, 9])


@pytest.mark.parametrize("numbers, expected",
                         [(1, 1),
                          (1.3, 1.3)])
def test_sum_all_one_number(numbers, expected):
    assert sum_all(numbers) == expected


@pytest.mark.parametrize("numbers, expected",
                         [((1, 2, 7, 5), 15),
                          ([2.7, 9.1, 2.78, 5], 19.58),
                          ([0, 0, 2.78], 2.78)])
def test_sum_all_list(numbers, expected):
    assert sum_all(*numbers) == expected


def test_type_error_sum_all():
    with pytest.raises(TypeError):
        sum_all("dsgh", "usaihf", 'edh')


def test_time_of_day_night():
    with Replace('functions_and_classes.to_test.datetime', test_datetime(2021, 5, 24, 5, 15, 34)):
        assert time_of_day() == 'night'


def test_time_of_day_morning():
    with Replace('functions_and_classes.to_test.datetime', test_datetime(2021, 5, 24, 10, 15, 34)):
        assert time_of_day() == 'morning'


def test_time_of_day_afternoon():
    with Replace('functions_and_classes.to_test.datetime', test_datetime(2021, 5, 24, 15, 15, 34)):
        assert time_of_day() == 'afternoon'


def test_time_of_day_strange_time():
    with pytest.raises(ValueError):
        with Replace('functions_and_classes.to_test.datetime', test_datetime(2021, 5, 24, 49, 155, 234)):
            time_of_day()


@pytest.fixture()
def set_up_product_subtract_quantity():
    product = Product("Chocolate", 30.5, 4)
    product.subtract_quantity(2)
    return product.quantity


@pytest.fixture()
def set_up_product_add_quantity():
    product = Product("Cherry", 15.75, 200)
    product.add_quantity(10)
    return product.quantity


@pytest.fixture()
def set_up_product_change_price():
    product = Product("Sugar", 20.35, 1000)
    product.change_price(5.68)
    return product.price


@pytest.fixture()
def set_up_product_change_price_negative():
    product = Product("Potato", 7, 500)
    product.change_price(-3000)
    return product.price


@pytest.fixture()
def set_up_product_quantity_negative():
    product = Product("Milk", 22, 3)
    product.subtract_quantity(500)
    return product.quantity


def test_product_subtract(set_up_product_subtract_quantity):
    assert set_up_product_subtract_quantity == 2


def test_product_add(set_up_product_add_quantity):
    assert set_up_product_add_quantity == 210


def test_product_change_price(set_up_product_change_price):
    assert set_up_product_change_price == 5.68


def test_product_change_price_negative(set_up_product_change_price_negative):
    with pytest.raises(ValueError):
        assert set_up_product_change_price_negative == -3000


def test_product_quantity_negative(set_up_product_quantity_negative):
    with pytest.raises(ValueError):
        assert set_up_product_quantity_negative == -497


@pytest.fixture()
def set_up_shop_products_list():
    carrot = Product('Carrot', 4.5, 3000)
    cabbage = Product('Cabbage', 10.2, 200)
    chicken = Product('Chicken', 90, 1500)
    candy = Product('Candy', 55, 15)
    shop = Shop([candy, cabbage, carrot, chicken])
    shop.add_product(Product("Beans", 15, 150))
    return len(shop.products)


@pytest.fixture()
def set_up_shop_sell_product():
    carrot = Product('Carrot', 4.5, 3000)
    cabbage = Product('Cabbage', 10.2, 200)
    chicken = Product('Chicken', 90, 1500)
    candy = Product('Candy', 55, 15)
    shop = Shop([candy, cabbage, carrot, chicken])
    money = shop.sell_product("Candy", 2)
    return money


@pytest.fixture()
def set_up_shop_sell_negative_amount_of_product():
    carrot = Product('Carrot', 4.5, 3000)
    cabbage = Product('Cabbage', 10.2, 200)
    chicken = Product('Chicken', 90, 1500)
    candy = Product('Candy', 55, 15)
    shop = Shop([candy, cabbage, carrot, chicken])
    money = shop.sell_product("Candy", -2)
    return money


def test_add_product_to_shop(set_up_shop_products_list):
    assert set_up_shop_products_list == 5


def test_sell_product_in_shop(set_up_shop_sell_product):
    assert set_up_shop_sell_product == 110


def test_sell_negative_amount_of_product(set_up_shop_sell_negative_amount_of_product):
    with pytest.raises(ValueError):
        assert set_up_shop_sell_negative_amount_of_product == -110


def test_bad_init_strings():
    with pytest.raises(TypeError):
        shop = Shop(["dgh", 'IUHih', 'iuhil'])


def test_bad_init_list():
    with pytest.raises(TypeError):
        shop = Shop([1, 22, 3.67, 3])


def test_adding_bad_product():
    with pytest.raises(TypeError):
        shop = Shop()
        shop.add_product('hhsiofud')