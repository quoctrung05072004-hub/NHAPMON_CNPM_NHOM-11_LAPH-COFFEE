# LAPH CAFE – Hệ thống quản lý order tại quầy

**Nhóm 11 – Môn Nhập môn Công nghệ phần mềm**

## Giới thiệu đề tài

LAPH CAFE phục vụ khách theo hình thức order và thanh toán tại quầy. Khách nhận thẻ số rồi tự chọn chỗ ngồi; nhân viên pha chế nhận đơn và nhân viên phục vụ giao nước theo số thẻ.

Qua khảo sát, nhóm nhận thấy một số bất tiện trong quá trình chuyển thông tin giữa thu ngân, pha chế và phục vụ. Ghi chú món có thể bị thiếu trên bill, việc theo dõi đơn chưa thuận tiện và nhân viên đôi khi khó tìm khách khi khách đổi vị trí. Từ đó, nhóm lựa chọn xây dựng hệ thống quản lý order để hỗ trợ các bộ phận phối hợp hiệu quả hơn.

## Chức năng chính

- **Thu ngân:** Xem thực đơn, chọn món, nhập số lượng và ghi chú riêng từng món, cấp số thẻ và ghi nhận thanh toán.
- **Pha chế:** Tiếp nhận đơn, xem ghi chú, cập nhật trạng thái món.
- **Phục vụ:** Xem món đã pha xong, kiểm tra số thẻ, cập nhật vị trí khách và xác nhận đã giao.
- **Quản lý:** Quản lý thực đơn, theo dõi hoạt động và xem báo cáo bán hàng.

Số thẻ khách nhận không gắn cố định với số bàn. Việc sửa hoặc hủy đơn đã thanh toán sẽ được bổ sung sau khi nhóm làm rõ quy trình của quán.

## Công nghệ dự kiến

| Thành phần | Công nghệ |
|---|---|
| Giao diện | HTML, CSS, JavaScript, Bootstrap |
| Xử lý nghiệp vụ | Python Flask |
| Cơ sở dữ liệu | Microsoft SQL Server |
| Truy cập dữ liệu | SQLAlchemy, pyodbc |
| Quản lý công việc | Jira |
| Quản lý mã nguồn | Git, GitHub |

## Thành viên nhóm 11

| Họ và tên | Công việc phụ trách trong Sprint 0 | GitHub |
|---|---|---|
| Mai Quốc Trung | Tổng hợp yêu cầu và quản lý công việc nhóm | [quoctrung05072004-hub](https://github.com/quoctrung05072004-hub) |
| Trương Đình Vũ | Phân tích nghiệp vụ thu ngân | [vu175070-laph](https://github.com/vu175070-laph) |
| Xa Anh Thơ | Thiết kế cơ sở dữ liệu | [kaido-911](https://github.com/kaido-911) |
| Hoàng Trương Ngọc Ánh | Thiết kế giao diện | [angt22588-glitch](https://github.com/angt22588-glitch) |
| Mai Văn Cường | Phân tích quy trình pha chế và phục vụ | [cuong2k7-b](https://github.com/cuong2k7-b) |
| Lê Viết Hưng | Kiến trúc hệ thống và kiểm thử | Đang cập nhật |

## Tài liệu dự án

- [Product Backlog và User Story](docs/PRODUCT_BACKLOG.md)
- [Kế hoạch Sprint 0 và phân công nhóm](docs/SPRINT0_PLAN.md)
- [Kiến trúc hệ thống](docs/ARCHITECTURE.md)
- [Tổng hợp công việc nhóm trưởng](docs/LEADER_SPRINT0_DELIVERABLE.md)
- [Thông tin Jira và nộp bài](docs/JIRA_SETUP.md)
- [Các vấn đề cần làm rõ](docs/OPEN_QUESTIONS.md)

## Jira và GitHub

**Jira:** https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog

**GitHub:** https://github.com/quoctrung05072004-hub/NHAPMON_CNPM_NHOM-11_LAPH-COFFEE

Nhóm sử dụng Sprint 0 để chuẩn bị yêu cầu, kế hoạch và thiết kế ban đầu. Các chức năng của hệ thống được triển khai ở các Sprint tiếp theo.
