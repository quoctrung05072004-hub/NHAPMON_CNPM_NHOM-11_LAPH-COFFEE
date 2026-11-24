# Tạo Jira Project LAPH CAFE và nộp Sprint 0

## A. Tạo Project mới (không dùng KAN cũ)

1. Truy cập Jira của nhóm, chọn **Spaces / Projects → Create space / Create project**.
2. Chọn **Software development** → **Scrum** (ưu tiên vì có Sprint 0; nếu workspace chỉ cho Kanban, vẫn tạo Board và gắn nhãn Sprint 0 trong Task).
3. Tên: **Nhóm 11 – LAPH CAFE – Quản lý order tại quầy**. Key đề xuất: **LAPH** hoặc **LAPH11** nếu chưa dùng.
4. Mời sáu thành viên, phân quyền thành viên. Hưng cần cung cấp email Jira/GitHub.
5. Tạo **Sprint 0** để theo dõi các Task nghiên cứu, thiết kế, môi trường; không đưa tính năng lập trình vào Doing của Sprint 0.

## B. Nhập Backlog

- Từ `docs/PRODUCT_BACKLOG.md`: tạo 16 Story, dùng tiêu đề `US01 - ...`, Description là User Story + Acceptance Criteria, Priority P1/P2/P3, Story Points theo cột đề xuất.
- Nếu không thấy trường Story Points: thêm trường ước lượng trong cấu hình Issue hoặc ghi `Story Points đề xuất: 3/5/8` trong Description; đừng tự ghi nhận là cả nhóm đã thống nhất.
- US13 để **Chờ khảo sát**, không xếp Sprint 1.

## C. Phân công Sprint 0

- Tạo 6 Task theo `docs/SPRINT0_PLAN.md`, mỗi người được gán một Task.
- Giữ trạng thái **To Do** đến khi người nhận bắt đầu; chỉ chuyển **Done** khi có kết quả thật.
- Có thể thêm URL tài liệu đầu ra vào Description/Comment của Task khi hoàn thành.

## D. Nộp Google Form

**Link Jira dự án:** URL Board/Project LAPH mới, không dùng Board KAN của bài quản lý thư viện.

**Ảnh Jira có vai trò cá nhân:** mỗi thành viên chụp màn hình thấy tên Task và assignee của mình. Nếu Board không hiện tên, mở chi tiết Task rồi chụp.

**Link GitHub dự án:** https://github.com/quoctrung05072004-hub/NHAPMON_CNPM_NHOM-11_LAPH-COFFEE

**Ảnh Commit thể hiện vai trò cá nhân:** Biểu mẫu ghi rõ **chưa áp dụng với Sprint 0**, nên không phải tạo commit mới chỉ để có ảnh.

**Ghi chú:** có thể ghi `Nhóm 11 – LAPH CAFE. Sprint 0. Nhiệm vụ: [tên Task].` (chỉ ghi hoàn thành nếu đã hoàn thành).

**Trước khi bấm Gửi:** kiểm tra tên, MSSV, link Jira và GitHub, ảnh có rõ người nhận việc và không có file nào vượt 10MB.
