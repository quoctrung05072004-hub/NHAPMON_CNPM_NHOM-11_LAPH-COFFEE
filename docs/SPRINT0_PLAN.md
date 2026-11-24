# KẾ HOẠCH SPRINT 0 – NHÓM 11 LAPH CAFE

**Đề tài:** Xây dựng hệ thống quản lý order tại quầy cho LAPH CAFE  
**Môn học:** Nhập môn Công nghệ phần mềm  
**Nhóm:** 11 – 6 thành viên  
**Thời gian thực hiện:** 24–25/11/2026  
**Hạn nộp bài:** 18:00 ngày 25/11/2026

## 1. Mục tiêu Sprint 0

Trong tuần này, nhóm tập trung chuẩn bị cho dự án: thống nhất các chức năng cần làm, lập Product Backlog, phân công nhiệm vụ, chọn công nghệ và phác thảo thiết kế ban đầu.

Nhóm chọn làm **ứng dụng web**, sử dụng Python Flask, HTML/CSS/JavaScript và SQL Server. Khi báo cáo, nhóm sẽ demo trên một máy tính và chuyển qua các màn hình thu ngân, pha chế, phục vụ, quản lý.

Ở Sprint 0, nhóm chưa triển khai toàn bộ chức năng. Phần lập trình sẽ được thực hiện ở các Sprint tiếp theo.

## 2. Phân công công việc

| Thành viên | Mã công việc trên Jira | Nội dung phụ trách | Kết quả dự kiến |
|---|---|---|---|
| **Mai Quốc Trung** | **LAPH11-17** | Tổng hợp yêu cầu, viết tầm nhìn sản phẩm, lập Backlog và theo dõi tiến độ | Product Vision, danh sách User Story và kế hoạch nhóm |
| **Trương Đình Vũ** | **LAPH11-18** | Phân tích các thao tác của thu ngân: chọn món, ghi chú, tính tiền, cấp số thẻ | Mô tả quy trình thu ngân, User Story và tiêu chí chấp nhận |
| **Xa Anh Thơ** | **LAPH11-19** | Xác định dữ liệu cần lưu và thiết kế các bảng liên quan | Sơ đồ ERD sơ bộ, các bảng và quan hệ dữ liệu |
| **Hoàng Trương Ngọc Ánh** | **LAPH11-20** | Phác thảo giao diện thu ngân, pha chế và phục vụ | Bản vẽ giao diện và mô tả thao tác chính |
| **Mai Văn Cường** | **LAPH11-21** | Phân tích các bước nhận đơn, pha chế, giao nước và cập nhật tình trạng đơn | Sơ đồ quy trình xử lý đơn hàng |
| **Lê Viết Hưng** | **LAPH11-22** | Đề xuất cách tổ chức hệ thống, yêu cầu bảo mật và kiểm thử | Sơ đồ kiến trúc và danh sách các trường hợp cần kiểm thử |

Đây là phần việc mỗi người phụ trách chính. Cả nhóm cùng đọc lại các User Story, góp ý và thống nhất độ ưu tiên cũng như Story Points trước khi bắt đầu Sprint 1.

## 3. Kế hoạch thực hiện

**Bước 1 – Xác định yêu cầu**

Dựa trên khảo sát tại LAPH CAFE, nhóm tập trung vào ba vấn đề: ghi chú món đôi khi bị thiếu trên bill, khó theo dõi tình trạng pha chế và mất thời gian tìm khách khi khách đổi chỗ.

**Bước 2 – Lập Product Backlog**

Nhóm đã tổng hợp 16 User Story trên Jira, gồm các chức năng tạo đơn, nhập ghi chú, thanh toán, theo dõi pha chế, giao nước và quản lý. Mỗi Story có mức ưu tiên và Story Points đề xuất để nhóm trao đổi, điều chỉnh.

Chi tiết xem tại [Product Backlog](PRODUCT_BACKLOG.md).

**Bước 3 – Phác thảo hệ thống**

Các thành viên xây dựng sơ đồ cơ sở dữ liệu, bản phác giao diện, luồng xử lý đơn hàng và kiến trúc hệ thống. Các phần này sẽ được đối chiếu với nhau để thống nhất trước khi viết code.

**Bước 4 – Tổng hợp và nộp bài**

Từng thành viên đưa kết quả vào công việc Jira của mình. Nhóm trưởng kiểm tra, tổng hợp tài liệu và gửi các đường dẫn Jira, GitHub theo biểu mẫu của thầy.

## 4. Tiến độ hiện tại

Nhóm đã tạo dự án Jira **LAPH11**, nhập **16 User Story** vào Product Backlog, tạo **6 công việc Sprint 0** và phân công cho từng thành viên. Repository GitHub LAPH CAFE cũng đã có README, Backlog và tài liệu kiến trúc ban đầu.

Các phần việc của từng thành viên đang tiếp tục được hoàn thiện. Sau khi nhận đủ bản vẽ, sơ đồ và nội dung phân tích, nhóm sẽ rà soát và cập nhật tài liệu chung.

**Jira:** https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog

**GitHub:** https://github.com/quoctrung05072004-hub/NHAPMON_CNPM_NHOM-11_LAPH-COFFEE

## 5. Hướng phát triển ở các Sprint tiếp theo

Nhóm dự kiến làm trước luồng order tại quầy:

1. Thu ngân chọn món, nhập ghi chú riêng cho từng món, nhận thanh toán và cấp thẻ số cho khách.
2. Pha chế nhận được đơn và ghi chú, sau đó cập nhật trạng thái khi hoàn thành món.
3. Phục vụ xem số thẻ, cập nhật vị trí khách khi cần và xác nhận đã giao nước.
4. Quản lý xem thông tin bán hàng và các báo cáo cơ bản.

Sản phẩm được thiết kế để demo trên một máy tính. Nhóm ưu tiên làm ổn định quy trình trên trước, sau đó mới bổ sung các chức năng như tích điểm và báo cáo chi tiết.
