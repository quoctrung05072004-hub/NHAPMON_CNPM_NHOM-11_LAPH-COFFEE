# Hồ sơ Sprint 0 — Phần nhóm trưởng Mai Quốc Trung

**Dự án:** Nhóm 11 – LAPH CAFE – Quản lý Order tại quầy  
**Môn:** Nhập môn Công nghệ phần mềm  
**Jira:** [LAPH11 – Scrum Backlog](https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog)  
**Task nhóm trưởng:** [LAPH11-17](https://quoctrung05072004.atlassian.net/browse/LAPH11-17)  
**Ngày chuẩn bị:** 24/11/2026  
**Trạng thái:** Hoàn thành **bản dự thảo** do nhóm trưởng tổng hợp; cần cả nhóm rà soát/chốt Story Points và bổ sung kết quả bàn giao trước khi kết luận Sprint 0 hoàn tất.

## 1. Lý do chọn đề tài và vấn đề cần giải quyết

Từ khảo sát LAPH CAFE: quán hoạt động theo mô hình khách **order và thanh toán tại quầy**, nhận **thẻ số** rồi tự chọn chỗ ngồi; pha chế nhận bill, phục vụ giao nước theo số thẻ. Các vấn đề:
1. Ghi chú ít đường/không đá có thể thất lạc trên bill chuyển sang pha chế.
2. Chưa có luồng trạng thái điện tử xuyên suốt thu ngân → pha chế → phục vụ.
3. Khách ngồi tự do và có thể đổi chỗ; phục vụ phải tự tìm nếu không biết vị trí mới.

**Giới hạn tính đúng đắn:** Số thẻ là định danh lượt khách, **không phải số bàn cố định**. Phục vụ chỉ cập nhật vị trí sau khi xác nhận được; không giả định hệ thống tự theo dõi khách.

## 2. Product Vision

> Xây dựng một hệ thống web demo hỗ trợ thu ngân, pha chế, phục vụ và quản lý tại LAPH CAFE, giúp chuyển đầy đủ đơn và ghi chú từng món, theo dõi tiến độ pha chế, nhận diện lượt khách bằng số thẻ và cập nhật vị trí ngồi khi được xác nhận, qua đó giảm sai sót và thời gian tìm khách.

**Người dùng:** Thu ngân; pha chế; phục vụ; quản lý (và chủ quán với vai trò phê duyệt giá ở giai đoạn sau).  
**Phương án demo:** **Một laptop**, mở trình duyệt và chuyển qua các vai trò, không cần nhiều thiết bị.  
**Stack dự kiến:** HTML/CSS/JavaScript + Bootstrap; Python Flask; SQL Server; SQLAlchemy/pyodbc.

### Phạm vi MVP

**Có:** xem menu; tạo đơn nhiều món; lưu ghi chú từng món; cấp thẻ; ghi nhận thanh toán giả lập; màn hình pha chế; trạng thái từng món; màn hình phục vụ; cập nhật vị trí tự do; xác nhận giao đủ.

**Không có trong MVP:** xử lý ngân hàng thật, đồng bộ POS/máy in bill thật, tích điểm, chấm công, báo cáo nâng cao. Sửa/hủy sau thanh toán **chưa được chốt chính sách**, không tự xây dựng quy định.

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

**Tổng sơ bộ:** 16 Story, 70 Story Points đề xuất (P1: 41; P2: 13; P3: 8; Chờ khảo sát: 8). **Không coi 70 điểm là cam kết Sprint 1**. Điểm chưa được nhóm xác nhận và US13 chỉ là độ phức tạp ước lượng, không lên lịch triển khai.

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
4. Trung cập nhật **trường Story Points và Priority trên Jira**, không chỉ trong Description, sau cuộc thống nhất.
5. Ghi lại mục chưa thống nhất hoặc còn câu hỏi vào Backlog, không trình bày ước lượng dự thảo như dữ liệu đã được bình chọn.

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

## 5. Tiến độ nhóm trưởng — phân biệt việc đã làm và việc cần xác nhận

### Đã có minh chứng

- [x] Jira **LAPH11** theo mẫu Scrum đã được tạo (người dùng đã xác nhận qua ảnh).
- [x] Nhập CSV **22/22 công việc**, gồm 16 Story và 6 Task, không lỗi (ảnh kết quả import).
- [x] Đưa 6 Task **LAPH11-17 đến LAPH11-22** vào Sprint 0 (ảnh Backlog).
- [x] Gán 6 Task tương ứng cho Trung, Vũ, Thơ, Ánh, Cường, Hưng (ảnh Board).
- [x] Có repository GitHub dự án với README, Backlog và tài liệu kiến trúc.
- [x] Bản dự thảo Product Vision, phạm vi và Backlog có ưu tiên/SP đề xuất được tổng hợp tại đây.

### Chưa hoàn tất, phải làm thật trước khi báo xong Sprint 0

- [ ] Cả 6 thành viên cùng **xác nhận** Story Points, ưu tiên và nội dung.
- [ ] Người phụ trách nộp đủ tài liệu của mình và được nhóm rà soát.
- [ ] Hưng cung cấp **username GitHub**, được mời và clone repo (email Jira đã có).
- [ ] Từng thành viên clone repo và xác nhận trên Jira.
- [ ] Kiểm tra giảng viên đăng nhập được vào Jira **LAPH11**; trạng thái *Open* không đảm bảo truy cập công khai.
- [ ] Cập nhật trường Priority và Story Points riêng biệt trong Jira sau cuộc thống nhất.
- [ ] Từng bạn chụp ảnh Jira đúng Task cá nhân và điền Google Form.

## 6. Tiêu chí nộp theo thông báo

- **Link Jira:** https://quoctrung05072004.atlassian.net/jira/software/projects/LAPH11/boards/3/backlog
- **Link GitHub:** https://github.com/quoctrung05072004-hub/NHAPMON_CNPM_NHOM-11_LAPH-COFFEE
- **Ảnh minh chứng Jira:** Người nộp chụp Task gắn tên mình và mã LAPH11.
- **Ảnh Commit GitHub:** Biểu mẫu ghi “**chưa áp dụng với Sprint 0**”; không phải tạo commit hình thức.
- **Hạn:** 18:00 ngày 25/11/2026 theo ảnh thông báo đã được nhóm cung cấp.

## 7. Kết luận nhóm trưởng

Nhóm đã xác định rõ vấn đề thực tế, giới hạn sản phẩm demo, Product Backlog ban đầu và nhiệm vụ của các thành viên. Bản tổng hợp này làm cơ sở để **cả 6 người xác nhận và bổ sung** trong Sprint 0, sau đó phát triển lần lượt các tính năng qua Sprint 1 trở đi. Không trình bày đây là sản phẩm đã hoàn thành hoặc kết quả khảo sát chính sách chưa xác minh.
