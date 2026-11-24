# TỔNG HỢP CÔNG VIỆC SPRINT 0 – MAI QUỐC TRUNG

**Dự án:** Nhóm 11 – LAPH CAFE – Quản lý Order tại quầy  
**Môn:** Nhập môn Công nghệ phần mềm  
**Jira:** [LAPH11 – Scrum Backlog](https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog)  
**Task nhóm trưởng:** [LAPH11-17](https://quoctrung05072004.atlassian.net/browse/LAPH11-17)  
**Ngày chuẩn bị:** 24/11/2026  
**Nội dung phụ trách:** Tổng hợp yêu cầu, Product Backlog, kế hoạch Sprint 0 và theo dõi công việc nhóm.

## 1. Lý do chọn đề tài và vấn đề cần giải quyết

Tại LAPH CAFE, khách order và thanh toán tại quầy, nhận thẻ số rồi chọn chỗ ngồi. Qua khảo sát quy trình thu ngân, pha chế và phục vụ, nhóm ghi nhận các vấn đề sau:
1. Ghi chú ít đường/không đá có thể thất lạc trên bill chuyển sang pha chế.
2. Chưa có luồng trạng thái điện tử xuyên suốt thu ngân → pha chế → phục vụ.
3. Khách ngồi tự do và có thể đổi chỗ; phục vụ phải tự tìm nếu không biết vị trí mới.

**Lưu ý:** Số thẻ khách cầm không phải số bàn cố định. Khi khách chuyển chỗ, nhân viên phục vụ có thể cập nhật lại vị trí trong hệ thống.

## 2. Mục tiêu dự án

> Xây dựng hệ thống web quản lý đơn hàng tại LAPH CAFE, kết nối thông tin giữa thu ngân, pha chế và phục vụ. Hệ thống giúp lưu đầy đủ ghi chú từng món, theo dõi tình trạng đơn và hỗ trợ giao nước theo số thẻ khách nhận.

**Người sử dụng:** Thu ngân, pha chế, phục vụ, quản lý.  
**Công nghệ dự kiến:** HTML/CSS/JavaScript, Bootstrap, Python Flask và SQL Server.

### Các chức năng ưu tiên

Hệ thống tập trung vào việc xem thực đơn, tạo đơn nhiều món, lưu ghi chú, cấp thẻ số, ghi nhận phương thức thanh toán, theo dõi pha chế và xác nhận giao nước.

Các chức năng như tích điểm, chấm công, báo cáo chi tiết và xử lý sửa/hủy sau thanh toán được xem xét ở các giai đoạn tiếp theo.

## 3. Product Backlog

| Story | Nội dung | Ưu tiên đề xuất | Story Points đề xuất | Jira |
|---|---|---|---:|---|
| US01 | Đăng nhập và phân quyền | P1 | 5 | LAPH11-1 |
| US02 | Thu ngân xem menu | P1 | 3 | LAPH11-2 |
| US03 | Tạo đơn nhiều món | P1 | 5 | LAPH11-3 |
| US04 | Ghi chú riêng từng món | P1 | 3 | LAPH11-4 |
| US05 | Cấp số thẻ | P1 | 3 | LAPH11-5 |
| US06 | Thanh toán mô phỏng | P1 | 5 | LAPH11-6 |
| US07 | Pha chế xem hàng chờ | P1 | 5 | LAPH11-7 |
| US08 | Trạng thái pha chế từng món | P1 | 3 | LAPH11-8 |
| US09 | Phục vụ xem món đã xong | P1 | 3 | LAPH11-9 |
| US10 | Cập nhật vị trí khách | P1 | 3 | LAPH11-10 |
| US11 | Xác nhận đã giao đủ | P1 | 3 | LAPH11-11 |
| US12 | Quản lý thực đơn và hết hàng | P2 | 3 | LAPH11-12 |
| US13 | Sửa/hủy đơn sau thanh toán | Chờ khảo sát | 8* | LAPH11-13 |
| US14 | Doanh thu và món bán chạy | P2 | 5 | LAPH11-14 |
| US15 | Giao ca và đối soát | P2 | 5 | LAPH11-15 |
| US16 | Khách hàng thành viên, tích điểm | P3 | 8 | LAPH11-16 |

Product Backlog gồm **16 User Story**, tổng ước lượng ban đầu **70 Story Points**. Nhóm sẽ trao đổi và điều chỉnh các điểm số khi lên kế hoạch thực hiện.

Chi tiết User Story và Acceptance Criteria từng mục: [PRODUCT_BACKLOG.md](./PRODUCT_BACKLOG.md).

### Nguyên tắc ưu tiên

- **P1**: Các chức năng chính trong quy trình bán hàng, pha chế và giao nước.
- **P2**: Có giá trị cho quản lý, nhưng phụ thuộc vào luồng cốt lõi.
- **P3**: Các chức năng bổ sung sau khi hoàn thiện quy trình chính.
- **Chờ khảo sát**: Nghiệp vụ chưa đủ thông tin; chưa đưa vào Sprint thực thi.

### Cách nhóm chốt Story Points

1. Cả 6 người đọc mỗi Story và Acceptance Criteria.
2. Mỗi người tự ước lượng 1/2/3/5/8 theo khối lượng, độ khó và rủi ro.
3. Khi có điểm khác nhau, trao đổi nguyên nhân, thống nhất một điểm.
4. Nhóm trưởng tổng hợp điểm đã thống nhất và cập nhật lên Jira.

## 4. Phân công Sprint 0

Ngoài phần việc được giao, các thành viên cùng góp ý cho Product Backlog và thống nhất kế hoạch chung của nhóm.

| Jira | Người phụ trách chính | Bàn giao | Người rà soát chéo |
|---|---|---|---|
| [LAPH11-17](https://quoctrung05072004.atlassian.net/browse/LAPH11-17) | **Trung** | Tầm nhìn, phạm vi, Backlog và điều phối | Cả nhóm |
| [LAPH11-18](https://quoctrung05072004.atlassian.net/browse/LAPH11-18) | **Vũ** | Quy trình thu ngân + AC US02–US06 | Ánh, Trung |
| [LAPH11-19](https://quoctrung05072004.atlassian.net/browse/LAPH11-19) | **Thơ** | ERD, PK/FK, các bảng dữ liệu | Hưng, Trung |
| [LAPH11-20](https://quoctrung05072004.atlassian.net/browse/LAPH11-20) | **Ánh** | Wireframe thu ngân / pha chế / phục vụ | Vũ, Cường |
| [LAPH11-21](https://quoctrung05072004.atlassian.net/browse/LAPH11-21) | **Cường** | Sơ đồ luồng và trạng thái từng món | Vũ, Ánh |
| [LAPH11-22](https://quoctrung05072004.atlassian.net/browse/LAPH11-22) | **Hưng** | Kiến trúc 3 lớp, NFR, checklist kiểm thử | Thơ, Trung |

## 5. Kết quả thực hiện

Các công việc đã thực hiện:

- Tạo dự án Scrum **LAPH11** trên Jira.
- Nhập **16 User Story** vào Product Backlog và **6 Task** vào Sprint 0.
- Phân công các Task từ **LAPH11-17 đến LAPH11-22** cho 6 thành viên.
- Tổng hợp tầm nhìn sản phẩm, chức năng cần phát triển, mức ưu tiên và Story Points dự kiến.
- Cập nhật README, Product Backlog và tài liệu kế hoạch trên GitHub.

### Công việc của nhóm trong thời gian tiếp theo

- Các thành viên xem lại User Story và cùng thống nhất Story Points.
- Hoàn thành các phần được phân công: nghiệp vụ thu ngân, ERD, giao diện, quy trình pha chế – phục vụ, kiến trúc và kiểm thử.
- Tổng hợp các tài liệu vào hồ sơ Sprint 0 và cập nhật tiến độ trên Jira.
- Kiểm tra quyền truy cập Jira và GitHub, chuẩn bị thông tin nộp bài của từng thành viên.

## 6. Đường dẫn dự án

- **Jira:** https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog
- **GitHub:** https://github.com/quoctrung05072004-hub/NHAPMON_CNPM_NHOM-11_LAPH-COFFEE
- **Hạn nộp Sprint 0:** 18:00, ngày 25/11/2026.

## 7. Tổng kết

Sprint 0 giúp nhóm thống nhất yêu cầu, cách tổ chức hệ thống và trách nhiệm của từng thành viên. Trên cơ sở đó, nhóm tiếp tục triển khai các chức năng quản lý order tại quầy ở các Sprint tiếp theo.
