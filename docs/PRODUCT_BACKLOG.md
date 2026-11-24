# Product Backlog ban đầu — LAPH CAFE

**Phiên bản:** Sprint 0 · 24/11/2026 · **Tình trạng:** Dự thảo cần cả nhóm xác nhận.

## Cách xác định ưu tiên và điểm

- **P1:** Luồng order cốt lõi (dự kiến Sprint 1–3).
- **P2:** Nghiệp vụ quản lý sau khi có luồng cốt lõi.
- **P3:** Mở rộng.
- **Story Points:** Ước lượng tương đối theo 1, 2, 3, 5, 8. Con số dưới đây là đề xuất ban đầu, **chưa phải nhóm đã bỏ phiếu**.
- **US13:** Chính sách sửa/hủy/hoàn tiền chưa được chủ quán xác nhận; để ở trạng thái chờ khảo sát.

## Danh sách ưu tiên

| ID | Chức năng | Ưu tiên | Điểm đề xuất |
|---|---|---|---:|
| US01 | Đăng nhập và phân quyền cơ bản | P1 | 5 |
| US02 | Xem menu và giá bán | P1 | 3 |
| US03 | Tạo đơn nhiều món | P1 | 5 |
| US04 | Ghi chú riêng từng món | P1 | 3 |
| US05 | Cấp số thẻ cho lượt khách | P1 | 3 |
| US06 | Ghi nhận thanh toán mô phỏng | P1 | 5 |
| US07 | Pha chế xem hàng chờ | P1 | 5 |
| US08 | Cập nhật trạng thái từng món | P1 | 3 |
| US09 | Phục vụ xem món sẵn sàng | P1 | 3 |
| US10 | Cập nhật vị trí khách | P1 | 3 |
| US11 | Xác nhận giao đủ nước | P1 | 3 |
| US12 | Quản lý menu và hết hàng | P2 | 3 |
| US13 | Sửa/hủy đơn sau thanh toán | Chờ khảo sát | 8 |
| US14 | Báo cáo doanh thu | P2 | 5 |
| US15 | Đối soát ca làm việc | P2 | 5 |
| US16 | Điểm thành viên | P3 | 8 |

## User Story và Acceptance Criteria

### US01 — Đăng nhập và phân quyền cơ bản

**User Story:** Là một **Nhân viên**, tôi muốn đăng nhập theo tài khoản và vai trò, để truy cập đúng màn hình và quyền hạn.

**Ưu tiên:** P1 · **Story Points đề xuất:** 5

**Acceptance Criteria:**
- Đăng nhập đúng tài khoản chuyển đến đúng vai trò
- Sai thông tin đăng nhập hiển thị lỗi và không vào hệ thống
- Thu ngân không có quyền cập nhật báo cáo quản lý

### US02 — Xem menu và giá bán

**User Story:** Là một **Thu ngân**, tôi muốn xem danh mục món, giá và trạng thái bán, để tư vấn và chọn món nhanh cho khách.

**Ưu tiên:** P1 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Hiển thị tên, danh mục, giá hiện hành
- Món hết hàng không được thêm vào đơn
- Có thể tìm kiếm tên món

### US03 — Tạo đơn nhiều món

**User Story:** Là một **Thu ngân**, tôi muốn tạo đơn có nhiều món và số lượng, để ghi nhận đầy đủ yêu cầu khách.

**Ưu tiên:** P1 · **Story Points đề xuất:** 5

**Acceptance Criteria:**
- Một đơn có thể chứa nhiều dòng món
- Số lượng là số nguyên dương và tổng tiền tính đúng
- Sau khi lưu có mã đơn và thời gian tự động

### US04 — Ghi chú riêng từng món

**User Story:** Là một **Thu ngân**, tôi muốn nhập ghi chú cho từng món như ít đường, không đá, để pha chế nhận đúng yêu cầu.

**Ưu tiên:** P1 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Mỗi dòng món lưu ghi chú độc lập
- Màn hình pha chế hiển thị nguyên vẹn ghi chú
- Món không có ghi chú vẫn tạo bình thường

### US05 — Cấp số thẻ cho lượt khách

**User Story:** Là một **Thu ngân**, tôi muốn gắn số thẻ đang rảnh vào lượt order, để nhân viên phục vụ nhận biết khách.

**Ưu tiên:** P1 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Lưu số thẻ vào lượt sử dụng
- Không cấp một thẻ đang được sử dụng cho hai lượt đồng thời
- Số thẻ không được hiểu là số bàn cố định

### US06 — Ghi nhận thanh toán mô phỏng

**User Story:** Là một **Thu ngân**, tôi muốn ghi nhận thanh toán tiền mặt hoặc chuyển khoản, để xác định trạng thái thanh toán của đơn.

**Ưu tiên:** P1 · **Story Points đề xuất:** 5

**Acceptance Criteria:**
- Lưu phương thức và số tiền đã thanh toán
- Không xử lý qua ngân hàng thật
- Đơn chưa thanh toán không tự xuất hiện như đơn đã thanh toán

### US07 — Pha chế xem hàng chờ

**User Story:** Là một **Pha chế**, tôi muốn xem đơn mới theo thứ tự thời gian, để ưu tiên làm đồ uống đúng đơn.

**Ưu tiên:** P1 · **Story Points đề xuất:** 5

**Acceptance Criteria:**
- Hiển thị số thẻ, món, số lượng và ghi chú
- Sắp xếp theo thời gian tạo đơn
- Có thông tin nhận biết đơn mới

### US08 — Cập nhật trạng thái từng món

**User Story:** Là một **Pha chế**, tôi muốn đánh dấu Chờ pha, Đang pha, Đã pha xong, để phục vụ biết món nào sẵn sàng.

**Ưu tiên:** P1 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Chỉ nhân viên được quyền mới cập nhật
- Trạng thái được lưu theo từng dòng món
- Trạng thái mới hiển thị ở màn hình phục vụ

### US09 — Phục vụ xem món sẵn sàng

**User Story:** Là một **Phục vụ**, tôi muốn xem đơn có món đã pha xong, để chủ động mang nước cho khách.

**Ưu tiên:** P1 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Hiển thị rõ số thẻ và món sẵn sàng
- Không đánh dấu món chưa pha xong là sẵn sàng
- Hiển thị vị trí khách nếu đã có thông tin

### US10 — Cập nhật vị trí khách

**User Story:** Là một **Phục vụ**, tôi muốn cập nhật vị trí khách sau khi xác nhận, để giao nước nhanh hơn khi khách đổi chỗ.

**Ưu tiên:** P1 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Cho phép vị trí trống khi chưa xác minh
- Cập nhật không thay đổi số thẻ
- Lưu người và thời điểm cập nhật vị trí

### US11 — Xác nhận giao đủ nước

**User Story:** Là một **Phục vụ**, tôi muốn xác nhận các món đã giao, để đóng đơn đúng thời điểm.

**Ưu tiên:** P1 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Chỉ cho hoàn tất khi đủ món đã giao
- Lưu người và thời điểm hoàn tất
- Đơn hoàn tất không còn ở danh sách cần giao

### US12 — Quản lý menu và hết hàng

**User Story:** Là một **Quản lý**, tôi muốn đề xuất cập nhật món, giá và tình trạng còn hàng, để thực đơn chính xác.

**Ưu tiên:** P2 · **Story Points đề xuất:** 3

**Acceptance Criteria:**
- Món hết hàng không được đặt
- Đổi giá không ảnh hưởng đơn cũ
- Quy trình phê duyệt thay đổi giá của chủ quán được ghi nhận ở giai đoạn sau

### US13 — Sửa/hủy đơn sau thanh toán

**User Story:** Là một **Quản lý**, tôi muốn xem xét và xử lý yêu cầu sửa hoặc hủy đơn, để kiểm soát sai sót và hoàn tiền.

**Ưu tiên:** Chờ khảo sát · **Story Points đề xuất:** 8

**Acceptance Criteria:**
- Chưa triển khai khi chưa chốt người phê duyệt
- Chưa triển khai khi chưa chốt thời hạn và quy tắc hoàn tiền
- Mọi thao tác tương lai phải có lịch sử

### US14 — Báo cáo doanh thu

**User Story:** Là một **Quản lý**, tôi muốn xem doanh thu ngày/tuần và món bán chạy, để đánh giá hiệu quả bán hàng.

**Ưu tiên:** P2 · **Story Points đề xuất:** 5

**Acceptance Criteria:**
- Chỉ tính đơn đã thanh toán hợp lệ
- Có lọc khoảng thời gian
- Tổng doanh thu khớp dữ liệu thanh toán

### US15 — Đối soát ca làm việc

**User Story:** Là một **Quản lý**, tôi muốn xem giao dịch tiền mặt, chuyển khoản và đơn hủy theo ca, để kiểm tra giao ca.

**Ưu tiên:** P2 · **Story Points đề xuất:** 5

**Acceptance Criteria:**
- Có thời điểm bắt đầu/kết thúc ca
- Phân loại phương thức thanh toán
- Quy tắc xử lý đơn hủy phải chốt trước khi triển khai

### US16 — Điểm thành viên

**User Story:** Là một **Thu ngân**, tôi muốn tra cứu khách và tích điểm theo giao dịch, để hỗ trợ chương trình khách hàng thân thiết.

**Ưu tiên:** P3 · **Story Points đề xuất:** 8

**Acceptance Criteria:**
- Lưu tên, số điện thoại và điểm tích lũy
- Không tạo điểm cho đơn chưa thanh toán
- Quy tắc quy đổi điểm sẽ xác minh sau


## Quy tắc sẵn sàng cho Sprint 1

Một User Story được chọn khi có vai trò, lợi ích, các tiêu chí chấp nhận kiểm thử được, phụ thuộc rõ ràng, ước lượng được nhóm thông qua và không còn câu hỏi nghiệp vụ chặn tiến độ.

## Definition of Done cho tính năng (từ Sprint 1)

Code thực sự chạy được, có kiểm thử liên quan, được review, Merge vào main, demo được luồng nghiệp vụ và dữ liệu lưu đúng vào SQL Server. Không áp tiêu chí lập trình tính năng này cho Sprint 0.
