# LAPH CAFE — Hệ thống quản lý order tại quầy

**Nhóm 11 | Nhập môn Công nghệ phần mềm | Sprint 0**

## Tầm nhìn sản phẩm

Xây dựng phần mềm web demo giúp quán LAPH CAFE quản lý quy trình **thu ngân → pha chế → phục vụ**, truyền đầy đủ ghi chú riêng từng món, theo dõi trạng thái và giao đồ uống theo **số thẻ** khách cầm. Số thẻ không phải số bàn cố định.

## Phạm vi demo

- Chạy trên **một máy tính**, chuyển giao diện bằng cách đăng nhập các vai trò: thu ngân, pha chế, phục vụ, quản lý.
- Thu ngân tạo đơn, gắn thẻ, lưu ghi chú, ghi nhận thanh toán mô phỏng.
- Pha chế xem và cập nhật trạng thái từng món.
- Phục vụ theo dõi, cập nhật vị trí khách khi xác nhận được, đánh dấu đã giao.
- SQL Server lưu dữ liệu; **không** tích hợp POS/máy in/thanh toán ngân hàng thật.
- Quy trình sửa hoặc hủy đơn đã thanh toán **chờ khảo sát**, không tự giả định.

## Công nghệ dự kiến

Python + Flask (backend), HTML/CSS/JavaScript + Bootstrap (frontend), Microsoft SQL Server (database), SQLAlchemy + pyodbc (truy cập dữ liệu), Git/GitHub (cộng tác), Jira (theo dõi).

**Lịch sử thành viên:** Từ bài thực hành trước đến hết tuần trước nhóm có 5 thành viên (Trung, Vũ, Thơ, Ánh, Cường). **Lê Viết Hưng chính thức tham gia từ 24/11/2026, bắt đầu ở Sprint 0 dự án LAPH CAFE.** Không ghi Hưng là người thực hiện các bài thực hành/commit trước thời điểm này.

## Thành viên nhóm 11

| Thành viên | Vai trò Sprint 0 | GitHub |
|---|---|---|
| Mai Quốc Trung | Nhóm trưởng / Scrum Master | [@quoctrung05072004-hub](https://github.com/quoctrung05072004-hub) |
| Trương Đình Vũ | Phân tích thu ngân | [@vu175070-laph](https://github.com/vu175070-laph) |
| Xa Anh Thơ | Phân tích dữ liệu | [@kaido-911](https://github.com/kaido-911) |
| Hoàng Trương Ngọc Ánh | Thiết kế giao diện | [@angt22588-glitch](https://github.com/angt22588-glitch) |
| Mai Văn Cường | Phân tích vận hành | [@cuong2k7-b](https://github.com/cuong2k7-b) |
| Lê Viết Hưng | Kiến trúc và kiểm thử | Chưa có username |

**Lưu ý:** Bảng vai trò Sprint 0 là **phân công dự kiến của nhóm trưởng** để các bạn xác nhận; không khẳng định các nhiệm vụ đã được hoàn thành.

## Hồ sơ Sprint 0

- [Product Backlog — 16 User Stories](docs/PRODUCT_BACKLOG.md)
- [Kế hoạch & phân công 6 người](docs/SPRINT0_PLAN.md)
- [Kiến trúc kỹ thuật dự kiến](docs/ARCHITECTURE.md)
- [Hướng dẫn tạo Jira và nộp Google Form](docs/JIRA_SETUP.md)
- [Các câu hỏi chưa xác minh](docs/OPEN_QUESTIONS.md)

## Quy trình Git nhóm

1. Clone repository về máy: `git clone https://github.com/quoctrung05072004-hub/NHAPMON_CNPM_NHOM-11_LAPH-COFFEE.git`
2. Tạo nhánh cá nhân từ `main` cho từng hạng mục, ví dụ `docs/sprint0-phan-tich-thu-ngan`.
3. Commit những thay đổi thực tế của mình, push lên GitHub, tạo Pull Request để thành viên khác review trước khi Merge.
4. Sprint 0 **chưa bắt buộc nộp ảnh commit** theo biểu mẫu thầy cung cấp; không cần tạo commit giả để lấy minh chứng.

## Trạng thái

Sprint 0 đang trong quá trình chuẩn bị, chưa hoàn thành xác nhận Jira, Story Points nhóm, sơ đồ ERD và tài khoản GitHub của thành viên Hưng.
