class OrderForm:
    def validate_order_input(self, table_card: str, drink_name: str, quantity: int) -> bool:
        """Kiểm tra dữ liệu hợp lệ khi tạo đơn order tại quầy."""
        if not table_card or not table_card.strip():
            return False
        if not drink_name or not drink_name.strip():
            return False
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            return False
        return True

    def create_order_ticket(self, table_card: str, drink_name: str, quantity: int, note: str = "") -> dict:
        """Tạo phiếu order gửi xuống quầy pha chế nếu dữ liệu hợp lệ."""
        if not self.validate_order_input(table_card, drink_name, quantity):
            raise ValueError("Thông tin order không hợp lệ!")
        return {
            "table_card": table_card.strip().upper(),
            "drink_name": drink_name.strip(),
            "quantity": quantity,
            "note": note.strip() if note else "Không có",
            "status": "Chờ pha chế"
        }

    def render_order_form(self):
        """Hiển thị giao diện Form nhập liệu trên màn hình Console."""
        print("==========================================")
        print("   FORM TẠO ĐƠN ORDER - LAPH COFFEE       ")
        print("==========================================")
        table_card = input("1. Nhập số thẻ bàn (VD: B01): ")
        drink_name = input("2. Nhập tên đồ uống (VD: Cà phê sữa): ")
        try:
            quantity = int(input("3. Nhập số lượng (> 0): "))
        except ValueError:
            print("-> Lỗi: Số lượng phải là số nguyên!")
            return
        note = input("4. Ghi chú pha chế (bỏ trống nếu không có): ")

        if self.validate_order_input(table_card, drink_name, quantity):
            ticket = self.create_order_ticket(table_card, drink_name, quantity, note)
            print("\n[THÀNH CÔNG] Đã đồng bộ phiếu xuống quầy pha chế:")
            print(ticket)
        else:
            print("\n[LỖI] Vui lòng nhập đầy đủ số thẻ bàn, tên món và số lượng > 0!")


if __name__ == "__main__":
    form = OrderForm()
    form.render_order_form()