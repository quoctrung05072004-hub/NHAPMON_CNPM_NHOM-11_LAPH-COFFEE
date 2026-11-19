import unittest
from src.ui.order_form import OrderForm


class TestOrderForm(unittest.TestCase):
    def test_valid_order_input(self):
        # 1. Arrange
        form = OrderForm()
        table_card = "B05"
        drink_name = "Cà phê sữa đá"
        quantity = 2

        # 2. Act
        actual = form.validate_order_input(table_card, drink_name, quantity)

        # 3. Assert
        self.assertTrue(actual)

    def test_empty_table_card_input(self):
        # 1. Arrange
        form = OrderForm()
        table_card = "   "
        drink_name = "Trà đào cam sả"
        quantity = 1

        # 2. Act
        actual = form.validate_order_input(table_card, drink_name, quantity)

        # 3. Assert
        self.assertFalse(actual)

    def test_invalid_quantity_input(self):
        # 1. Arrange
        form = OrderForm()
        table_card = "B02"
        drink_name = "Bạc xỉu"
        quantity = 0

        # 2. Act
        actual = form.validate_order_input(table_card, drink_name, quantity)

        # 3. Assert
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()