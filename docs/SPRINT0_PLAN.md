# Kế hoạch Sprint 0 — Nhóm 11 LAPH CAFE

**Thời gian chuẩn bị:** 24–25/11/2026; **hạn theo thông báo thầy:** 18:00 Thứ Tư 25/11/2026.

**Sprint Goal:** Thống nhất vấn đề, phạm vi demo và kiến trúc, xây Product Backlog đủ ưu tiên và Story Points sơ bộ, tạo Jira Project và phân công 6 người, cập nhật GitHub và Clone về máy. **Sprint 1 mới bắt đầu code tính năng.**

## Phân công đề xuất

| Người | Vai trò | Công việc | Bàn giao |
|---|---|---|---|
| Mai Quốc Trung | Nhóm trưởng / Scrum Master | Tầm nhìn sản phẩm, Product Backlog, quản lý Jira/GitHub, tổng hợp hồ sơ | README, Product Vision, tổng hợp ưu tiên/Story Points, minh chứng Sprint 0 |
| Trương Đình Vũ | Phân tích thu ngân | Quy trình order, ghi chú, thanh toán giả lập | User Story US02–US06 và AC, quy trình thu ngân |
| Xa Anh Thơ | Phân tích dữ liệu | Sơ đồ ERD, khóa chính/ngoại, số thẻ và lượt dùng | ERD sơ bộ, danh sách bảng dữ liệu |
| Hoàng Trương Ngọc Ánh | Thiết kế giao diện | Wireframe thu ngân, pha chế, phục vụ (responsive) | 2–3 wireframe và mô tả thao tác |
| Mai Văn Cường | Phân tích vận hành | Luồng pha chế, giao nước, trạng thái món/đơn | Activity diagram và bảng trạng thái |
| Lê Viết Hưng | Kiến trúc và kiểm thử | Sơ đồ 3 lớp, yêu cầu phi chức năng, tiêu chí kiểm thử | Sơ đồ kiến trúc, checklist kiểm thử/rủi ro |

## Các Task nên tạo trong Sprint 0 trên Jira

| Mã nội bộ | Assignee | Summary | Tiêu chí hoàn thành |
|---|---|---|---|
| S0-01 | Trung | Tổng hợp Product Vision và Product Backlog | README, phạm vi demo, Backlog có priority + SP đề xuất |
| S0-02 | Vũ | Khảo sát nghiệp vụ thu ngân | Luồng tạo đơn, ghi chú món, thanh toán + AC |
| S0-03 | Thơ | Thiết kế ERD sơ bộ | Sơ đồ dữ liệu, bảng và quan hệ khóa |
| S0-04 | Ánh | Thiết kế wireframe responsive | Màn hình thu ngân, pha chế/phục vụ (bản phác) |
| S0-05 | Cường | Phân tích luồng pha chế — giao nước | Luồng trạng thái món/đơn, trường hợp khách đổi vị trí |
| S0-06 | Hưng | Kiến trúc và tiêu chí kiểm thử | Sơ đồ 3 lớp, bảo mật cơ bản, checklist kiểm thử |

Các Task chỉ chuyển **Done** sau khi có sản phẩm bàn giao thực tế; không đánh dấu hoàn thành thay thành viên.

## Checklist nhóm trưởng

- [ ] Tạo Jira Project mới (không dùng Board KAN quản lý thư viện).
- [ ] Mời đủ sáu thành viên vào Jira, xác nhận tên/người được giao.
- [ ] Nhập Product Backlog từ `docs/PRODUCT_BACKLOG.md`, ưu tiên và Story Points.
- [ ] Giao sáu Task Sprint 0 trên Jira.
- [ ] Tổ chức thảo luận ngắn xác nhận điểm SP và quy trình sản phẩm.
- [ ] Nhờ Hưng gửi username GitHub, mời vào repo, kiểm tra quyền.
- [ ] Mỗi người Clone repository; lấy ảnh Jira có Task cá nhân để nộp.
- [ ] Chụp Jira Project/Board thật, sao chép đúng URL rồi điền Google Form.

## Kịch bản demo về sau

Trên một laptop: đăng nhập thu ngân tạo đơn Trà đào (ít đường) + Cà phê sữa (không đá), cấp thẻ 15 và thanh toán giả lập; đổi sang tài khoản pha chế đọc đầy đủ ghi chú, cập nhật món đã pha; đổi sang phục vụ xem thẻ 15, nhập khu vực khách vừa ngồi, xác nhận đã giao. Đây là **kịch bản tương lai**, không phải tính năng đã hoàn thành ở Sprint 0.
