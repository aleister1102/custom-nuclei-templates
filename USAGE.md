# Hướng Dẫn Sử Dụng Nuclei Template Organizer

## Tổng Quan

Bộ công cụ này giúp bạn tự động phân loại các nuclei templates từ nhiều thư mục khác nhau vào một thư mục có tổ chức, đồng thời:
- Xóa các template trùng lặp bằng hash checksum
- Lọc ra chỉ những template dành cho web pentest
- Phân loại theo công nghệ và kiểu tấn công (ưu tiên công nghệ)
- Tạo báo cáo markdown chi tiết
- Di chuyển file thay vì sao chép để tiết kiệm dung lượng

## Cài Đặt

1. **Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

2. **Đảm bảo Python 3.7+ được cài đặt**

## Sử Dụng

### Bước 1: Phân Loại Templates

```bash
python nuclei_organizer.py
```

Script sẽ:
- Quét tất cả thư mục con để tìm file `.yaml` và `.yml`
- Phân tích từng template để xác định:
  - Có phải là web pentest template không
  - Có yêu cầu thực thi script/payload không (sẽ bỏ qua)
  - Thuộc công nghệ nào hoặc kiểu tấn công nào
- Tính hash để phát hiện trùng lặp
- Di chuyển templates vào thư mục `organized-folder` với cấu trúc:
  ```
  organized-folder/
  ├── technology-wordpress/
  ├── technology-apache/
  ├── attack-sqli/
  ├── attack-xss/
  ├── cve-vulnerabilities/
  ├── information-gathering/
  └── miscellaneous/
  ```

### Bước 2: Xem Báo Cáo

Sau khi phân loại, script sẽ tạo các báo cáo:
- `organized-folder/README.md` - Báo cáo tổng quan
- `organized-folder/{category}_report.md` - Báo cáo chi tiết từng category

### Bước 3: Dọn Dẹp Thư Mục (Tùy Chọn)

```bash
python cleanup_directories.py
```

Script này sẽ:
- Xem trước những thư mục sẽ bị xóa
- Chỉ xóa những thư mục rỗng hoặc không chứa YAML templates
- Bảo vệ thư mục `.git`, `organized-folder` và các thư mục quan trọng khác

## Cách Phân Loại

### Ưu Tiên 1: Công Nghệ
Templates được phân loại theo công nghệ nếu chứa các từ khóa:
- **Web Servers**: apache, nginx, iis, tomcat, jboss
- **Languages**: php, asp, jsp, python, nodejs, ruby
- **CMS**: wordpress, drupal, joomla, magento
- **Databases**: mysql, postgresql, mongodb, redis
- **Frameworks**: spring, django, laravel, symfony
- **Tools**: jenkins, gitlab, docker, kubernetes

### Ưu Tiên 2: Kiểu Tấn Công  
Nếu không phải công nghệ cụ thể, phân loại theo kiểu tấn công:
- **Injection**: sqli, xss, xxe, command-injection
- **File**: lfi, rfi, file-upload, path-traversal
- **Auth**: weak-authentication, broken-authentication
- **Info**: information-disclosure, sensitive-data-exposure

### Ưu Tiên 3: Các Category Khác
- **CVE**: Tất cả CVE vulnerabilities
- **Info Gathering**: Templates thu thập thông tin
- **Config Issues**: Vấn đề cấu hình
- **Miscellaneous**: Không thuộc category nào khác

## Lọc Templates

### Được Giữ Lại:
- Templates có HTTP requests
- Templates với web-related tags
- Templates targeting web applications
- CVE của web vulnerabilities

### Bị Loại Bỏ:
- Templates yêu cầu thực thi script/payload
- Network-based templates (SSH, FTP, SMB, etc.)
- Infrastructure templates
- IoT/SCADA templates  
- Mobile app templates
- Binary analysis templates

## Tính Năng Nâng Cao

### Hash-based Duplicate Detection
- Sử dụng MD5 hash để phát hiện file trùng lặp hoàn toàn
- Tự động bỏ qua các template trùng lặp

### Smart Categorization
- Phân tích tags, name, description của template
- Ưu tiên công nghệ hơn kiểu tấn công
- Xử lý multiple tags và nested categories

### Comprehensive Reporting
- Báo cáo tổng quan với statistics
- Báo cáo chi tiết từng category
- Nhóm theo severity level
- Thông tin author, tags, description

## Ví Dụ Output

```
🚀 Nuclei Template Organizer
========================================
📂 Source directories found: 45
🔍 Scanning for nuclei templates...
📁 Found 2847 YAML files
📊 Processed 100/2847 files...
📊 Processed 200/2847 files...
...
📝 Generating reports...

============================================================
🎉 ORGANIZATION COMPLETED!
============================================================
📊 Total files processed: 2847
✅ Files successfully moved: 1923  
🔄 Duplicate files removed: 234
⏭️  Files skipped (non-web/invalid): 690
📁 Categories created: 23
📝 Target directory: organized-folder

📋 Categories breakdown:
   attack-sqli: 156 templates
   technology-wordpress: 234 templates
   technology-apache: 89 templates
   cve-vulnerabilities: 445 templates
   ...
```

## Troubleshooting

### Lỗi PyYAML
```bash
pip install --upgrade PyYAML
```

### Permission Errors
```bash
# Trên Linux/Mac
sudo python nuclei_organizer.py

# Hoặc thay đổi quyền thư mục
chmod -R 755 .
```

### Memory Issues (với dataset lớn)
Script được tối ưu để xử lý từng file một, không load tất cả vào memory.

## Lưu Ý Quan Trọng

⚠️ **BACKUP**: Luôn backup dữ liệu trước khi chạy script
⚠️ **TEST**: Chạy thử trên một thư mục nhỏ trước
⚠️ **REVIEW**: Kiểm tra báo cáo trước khi cleanup directories

## Liên Hệ & Hỗ Trợ

Nếu gặp vấn đề, hãy kiểm tra:
1. Python version >= 3.7
2. Tất cả dependencies đã cài đặt
3. Quyền đọc/ghi thư mục
4. Format của YAML templates hợp lệ 