# Sơ đồ Quy trình nghiệp vụ Quản lý tồn kho

Dưới đây là các sơ đồ biểu diễn trực quan các quy trình nghiệp vụ được mô tả trong hệ thống quản lý tồn kho.

## 1. Thiết lập Dữ liệu gốc & Tồn kho ban đầu

```mermaid
flowchart TD
    A[Bắt đầu] --> B[Định nghĩa Đơn vị tính]
    B --> C[Tạo Sản phẩm / Phân loại]
    C --> D[Chọn Đơn vị tính]
    D --> E{Sản phẩm đã kích hoạt?}
    E -- Có --> F[Khóa Đơn vị tính]
    E -- Không --> C
    F --> G[Thiết lập số lượng tồn kho ban đầu]
    G --> H[Kết thúc thiết lập]
```

## 2. Quy trình Điều chỉnh tồn kho

```mermaid
stateDiagram-v2
    [*] --> Nhap: Tạo yêu cầu (Thủ công / Import File)
    Nhap --> Nhap: Chỉnh sửa yêu cầu
    Nhap --> [*]: Xóa yêu cầu
    Nhap --> Cho_Duyet: Gửi yêu cầu duyệt
    Cho_Duyet --> Da_Duyet: Admin Duyệt
    Cho_Duyet --> Tu_Choi: Admin Từ chối
    Da_Duyet --> Cap_Nhat_Ton_Kho: Áp dụng thay đổi tồn kho
    Cap_Nhat_Ton_Kho --> [*]: Xác thực tồn kho thực tế >= 0
    Tu_Choi --> [*]
```

## 3. Quy trình Đặt hàng & Thanh toán

```mermaid
sequenceDiagram
    participant Khach_Hang as Khách hàng
    participant He_Thong as Hệ thống
    participant Ton_Kho as Tồn kho
    Khach_Hang->>He_Thong: Lướt xem / Xem giỏ hàng / Thanh toán
    He_Thong->>Ton_Kho: Kiểm tra số lượng tồn
    Ton_Kho-->>He_Thong: Trạng thái tồn kho
    He_Thong-->>Khach_Hang: Hiển thị Hết hàng (nếu bằng 0)

    Khach_Hang->>He_Thong: Đặt hàng & Thanh toán
    He_Thong->>Ton_Kho: Giữ hàng (Reserved)

    alt Đặt hàng thành công
        He_Thong-->>Khach_Hang: Xác nhận đơn hàng
    else Hủy đơn hàng
        He_Thong->>Ton_Kho: Bỏ giữ hàng (Unreserved)
        He_Thong-->>Khach_Hang: Xác nhận hủy đơn
    end
```

## 4. Quy trình Trả hàng & Hoàn tiền

```mermaid
flowchart TD
    A[Khởi tạo Yêu cầu Hoàn/Hủy] --> B[Tạo yêu cầu]
    B --> C[Đánh dấu sản phẩm: Hỏng / Không hỏng]
    C --> D[Gửi Admin]
    D --> E[Admin xem xét yêu cầu]
    E --> F[Admin có thể sửa trạng thái Hỏng]
    F --> G{Duyệt yêu cầu?}
    G -- Không --> H[Kết thúc quy trình]
    G -- Có --> I{Sản phẩm bị hỏng?}
    I -- Có --> J[Không cộng lại vào tồn kho]
    I -- Không --> K[Cộng lại số lượng vào tồn kho]
```
