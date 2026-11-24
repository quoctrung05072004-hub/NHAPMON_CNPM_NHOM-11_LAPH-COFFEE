# Hồ sơ Sprint 0 — Phần nhóm trưởng Mai Quốc Trung

**Dự án:** Nhóm 11 – LAPH CAFE – Quản lý Order tại quầy  
**Môn:** Nhập môn Công nghệ phần mềm  
**Jira:** [LAPH11 – Scrum Backlog](https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog)  
**Task nhóm trưởng:** [LAPH11-17](https://quoctrung05072004.atlassian.net/browse/LAPH11-17)  
**Ngày chuẩn bị:** 24/11/2026  
**Nội dung phụ trách:** Product Vision, phạm vi hệ thống, Product Backlog, kế hoạch Sprint 0 và điều phối công việc nhóm.

## 1. Lý do chọn đề tài và vấn đề cần giải quyết

Từ khảo sát LAPH CAFE: quán hoạt động theo mô hình khách **order và thanh toán tại quầy**, nhận **thẻ số** rồi tự chọn chỗ ngồi; pha chế nhận bill, phục vụ giao nước theo số thẻ. Các vấn đề:
1. Ghi chú ít đường/không đá có thể thất lạc trên bill chuyển sang pha chế.
2. Chưa có luồng trạng thái điện tử xuyên suốt thu ngân → pha chế → phục vụ.
3. Khách ngồi tự do và có thể đổi chỗ; phục vụ phải tự tìm nếu không biết vị trí mới.

**Lưu ý:** Số thẻ khách cầm không phải số bàn cố định. Khi khách chuyển chỗ, nhân viên phục vụ có thể cập nhật lại vị trí trong hệ thống.

## 2. Product Vision

> Xây dựng một hệ thống web demo hỗ trợ thu ngân, pha chế, phục vụ và quản lý tại LAPH CAFE, giúp chuyển đầy đủ đơn và ghi chú từng món, theo dõi tiến độ pha chế, nhận diện lượt khách bằng số thẻ và cập nhật vị trí ngồi khi được xác nhận, qua đó giảm sai sót và thời gian tìm khách.

**Người dùng:** Thu ngân; pha chế; phục vụ; quản lý (và chủ quán với vai trò phê duyệt giá ở giai đoạn sau).  
**Phương án demo:** **Một laptop**, mở trình duyệt và chuyển qua các vai trò, không cần nhiều thiết bị.  
**Stack dự kiến:** HTML/CSS/JavaScript + Bootstrap; Python Flask; SQL Server; SQLAlchemy/pyodbc.

### Phạm vi MVP

**Có:** xem menu; tạo đơn nhiều món; lưu ghi chú từng món; cấp thẻ; ghi nhận thanh toán giả lập; màn hình pha chế; trạng thái từng món; màn hình phục vụ; cập nhật vị trí tự do; xác nhận giao đủ.

**Không có trong MVP:** xử lý ngân hàng thật, đồng bộ POS/máy in bill thật, tích điểm, chấm công, báo cáo nâng cao. Quy trình sửa/hủy sau thanh toán sẽ bổ sung sau khi thống nhất quy định.

## 3. Product Backlog — bản tổng hợp để nhóm thảo luận

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

**Tổng hợp:** 16 User Story với 70 Story Points ước lượng ban đầu (P1: 41; P2: 13; P3: 8; chờ khảo sát: 8). Nhóm sẽ rà soát và thống nhất lại các điểm trước khi lập kế hoạch Sprint 1.

Chi tiết User Story và Acceptance Criteria từng mục: [PRODUCT_BACKLOG.md](./PRODUCT_BACKLOG.md).

### Nguyên tắc ưu tiên

- **P1**: Phải có để trình diễn được chu trình bán hàng – pha chế – giao nước.
- **P2**: Có giá trị cho quản lý, nhưng phụ thuộc vào luồng cốt lõi.
- **P3**: Chức năng mở rộng, không chặn demo MVP.
- **Chờ khảo sát**: Nghiệp vụ chưa đủ thông tin; chưa đưa vào Sprint thực thi.

### Cách nhóm chốt Story Points

1. Cả 6 người đọc mỗi Story và Acceptance Criteria.
2. Mỗi người tự ước lượng 1/2/3/5/8 theo khối lượng, độ khó và rủi ro.
3. Khi có điểm khác nhau, trao đổi nguyên nhân, thống nhất một điểm.
4. Nhóm trưởng cập nhật độ ưu tiên và điểm đã thống nhất lên Jira.
5. Các nội dung chưa rõ được giữ lại để tiếp tục trao đổi ở buổi họp sau.

## 4. Công việc Sprint 0 — trách nhiệm chung và người phụ trách chính

**Mọi thành viên cùng tham gia:** rà soát 16 Story, thảo luận điểm và độ ưu tiên, đọc luồng nghiệp vụ, đăng nhập Jira, clone repository, bình luận vào công việc có liên quan.

| Jira | Người phụ trách chính | Bàn giao | Người rà soát chéo |
|---|---|---|---|
| [LAPH11-17](https://quoctrung05072004.atlassian.net/browse/LAPH11-17) | **Trung** | Tầm nhìn, phạm vi, Backlog và điều phối | Cả nhóm |
| [LAPH11-18](https://quoctrung05072004.atlassian.net/browse/LAPH11-18) | **Vũ** | Quy trình thu ngân + AC US02–US06 | Ánh, Trung |
| [LAPH11-19](https://quoctrung05072004.atlassian.net/browse/LAPH11-19) | **Thơ** | ERD, PK/FK, các bảng dữ liệu | Hưng, Trung |
| [LAPH11-20](https://quoctrung05072004.atlassian.net/browse/LAPH11-20) | **Ánh** | Wireframe thu ngân / pha chế / phục vụ | Vũ, Cường |
| [LAPH11-21](https://quoctrung05072004.atlassian.net/browse/LAPH11-21) | **Cường** | Sơ đồ luồng và trạng thái từng món | Vũ, Ánh |
| [LAPH11-22](https://quoctrung05072004.atlassian.net/browse/LAPH11-22) | **Hưng** | Kiến trúc 3 lớp, NFR, checklist kiểm thử | Thơ, Trung |

## 5. Kết quả thực hiện

Trong Sprint 0, nhóm trưởng đã thực hiện các công việc khởi tạo và tổng hợp ban đầu:

- Tạo dự án Scrum **LAPH11** trên Jira.
- Nhập **16 User Story** vào Product Backlog và **6 Task** vào Sprint 0.
- Phân công các Task từ **LAPH11-17 đến LAPH11-22** cho 6 thành viên.
- Tổng hợp tầm nhìn sản phẩm, chức năng cần phát triển, mức ưu tiên và Story Points dự kiến.
- Cập nhật README, Product Backlog và tài liệu kế hoạch trên GitHub.

### Công việc tiếp theo của nhóm

- Các thành viên xem lại User Story và cùng thống nhất Story Points.
- Hoàn thành các phần được phân công: nghiệp vụ thu ngân, ERD, giao diện, quy trình pha chế – phục vụ, kiến trúc và kiểm thử.
- Tổng hợp các tài liệu vào hồ sơ Sprint 0 và cập nhật tiến độ trên Jira.
- Kiểm tra quyền truy cập Jira và GitHub, chuẩn bị thông tin nộp bài của từng thành viên.

## 6. Thông tin nộp bài

- **Jira:** https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog
- **GitHub:** https://github.com/quoctrung05072004-hub/NHAPMON_CNPM_NHOM-11_LAPH-COFFEE
- **Ảnh Jira:** Chụp công việc được phân công, thể hiện mã Task và tên người phụ trách.
- **Ảnh commit GitHub:** Chưa áp dụng với Sprint 0 theo nội dung biểu mẫu.
- **Hạn nộp:** 18:00, ngày 25/11/2026.

## 7. Tổng kết

Ở Sprint 0, nhóm tập trung xác định yêu cầu, xây dựng Product Backlog, lựa chọn công nghệ và phân công nhiệm vụ. Các tài liệu được sử dụng làm cơ sở để nhóm triển khai chức năng order tại quầy trong những Sprint tiếp theo.
