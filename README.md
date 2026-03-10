# Auto Redeem Gift Code – Garena Delta Force

🌐 **Language**

- English
- Vietnamese (Tiếng Việt) below

---

# 🇺🇸 English

## Introduction

A lightweight Python automation tool that automatically redeems **Garena Delta Force** gift codes.

This project uses **Selenium WebDriver** to automatically open the redeem page, load login cookies, and redeem multiple gift codes from a text file.

---

## Features

- Automatically redeem multiple gift codes
- Login using exported browser cookies (no manual login required)
- Load gift codes from a `.txt` file
- Simple popup file selector
- Can be compiled into `.exe`

---

## Requirements

Before running the project you need:

- Python **3.9+**
- Google Chrome
- ChromeDriver (same version as Chrome)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Download ChromeDriver

Download ChromeDriver from:

https://chromedriver.chromium.org/downloads

Choose the version that matches your **Chrome browser**.

After downloading:

1. Extract the file
2. Place `chromedriver.exe` in the same folder as `main.py`

Example structure:

```
Auto_redeem_Gift_code_Garena_DF
│
├── main.py
├── chromedriver.exe
├── requirements.txt
└── README.md
```

---

## Export Login Cookies

Install extension:

https://chromewebstore.google.com/detail/j2team-cookies/okpidcojinmlaakglciglbpcpajaibco

Steps:

1. Open redeem page

```
https://redeem.df.garena.sg
```

2. Login to your game account  
3. Click **J2TEAM Cookies extension**  
4. Export cookies as **JSON file**  
5. Save it to your computer  

---

## Create Gift Code File

Create file:

```
Gift_code_list.txt
```

Example:

```
DFCL503
DFWizard309
DFRemarkable103
DFRocket825
```

Each line contains **one gift code**.

---

## Run the Project

Run with Python:

```bash
python main.py
```

Program flow:

1. Select **cookies JSON file**
2. Select **gift code list**
3. Tool automatically redeems all codes

---

## Build EXE (Optional)

Install PyInstaller:

```bash
pip install pyinstaller
```

Build:

```bash
pyinstaller --onefile --noconsole --collect-all selenium main.py
```

Output file:

```
dist/main.exe
```

---

## Notes

- Make sure **ChromeDriver version matches your Chrome browser**.
- If Chrome updates automatically, you may need to download a new ChromeDriver.
- Users must **prepare their own list of gift codes** in a `.txt` file.
- Each line in the file should contain **one gift code**.
- If redeem fails, check:
  - internet connection
  - cookies file validity
  - your prepared gift code list

---

## Disclaimer

This project is provided **for educational and personal automation purposes only**.

The author does **not encourage abuse of game systems**.

The author is **not responsible for**:

- account suspension or bans
- misuse of the tool
- changes made by Garena to the redeem system

Use this tool **at your own risk**.

---

## Credits

Developed by:

```
Mentornoob
```

GitHub:

```
https://github.com/Mentornoob
```

⭐ If you like this project, consider giving it a **star**.

---

# 🇻🇳 Tiếng Việt

## Giới thiệu

Đây là một công cụ Python nhỏ giúp **tự động nhập gift code cho game Garena Delta Force**.

Tool sử dụng **Selenium WebDriver** để mở trang redeem, sử dụng cookies đăng nhập và tự động nhập nhiều gift code từ file.

---

## Tính năng

- Tự động redeem nhiều gift code
- Đăng nhập bằng cookies (không cần login thủ công)
- Đọc danh sách code từ file `.txt`
- Popup chọn file đơn giản
- Có thể build thành `.exe`

---

## Yêu cầu

Trước khi chạy cần cài:

- Python **3.9 trở lên**
- Google Chrome
- ChromeDriver đúng version Chrome

Cài thư viện:

```bash
pip install -r requirements.txt
```

---

## Tải ChromeDriver

Tải tại:

https://chromedriver.chromium.org/downloads

Chọn version **trùng với Chrome đang dùng**.

Sau khi tải:

1. Giải nén
2. Đặt file `chromedriver.exe` cùng thư mục với `main.py`

Ví dụ:

```
Auto_redeem_Gift_code_Garena_DF
│
├── main.py
├── chromedriver.exe
├── requirements.txt
└── README.md
```

---

## Xuất Cookies đăng nhập

Cài extension:

https://chromewebstore.google.com/detail/j2team-cookies/okpidcojinmlaakglciglbpcpajaibco

Các bước:

1. Mở trang redeem

```
https://redeem.df.garena.sg
```

2. Đăng nhập tài khoản game  
3. Bấm extension **J2TEAM Cookies**  
4. Export cookies dạng **JSON**  
5. Lưu file về máy  

---

## Tạo file danh sách Gift Code

Tạo file:

```
Gift_code_list.txt
```

Ví dụ:

```
DFCL503
DFWizard309
DFRemarkable103
DFRocket825
```

Mỗi dòng chứa **1 gift code**.

---

## Chạy chương trình

Chạy bằng Python:

```bash
python main.py
```

Chương trình sẽ:

1. Yêu cầu chọn file **cookies**
2. Yêu cầu chọn file **gift code**
3. Tự động redeem toàn bộ code

---

## Build file EXE (tuỳ chọn)

Cài PyInstaller:

```bash
pip install pyinstaller
```

Build:

```bash
pyinstaller --onefile --noconsole --collect-all selenium main.py
```

File `.exe` sẽ nằm trong:

```
dist/main.exe
```

---

## Ghi chú

- Đảm bảo **ChromeDriver trùng version với Chrome**.
- Khi Chrome tự cập nhật, bạn có thể cần tải lại ChromeDriver mới.
- Người dùng cần **tự chuẩn bị danh sách gift code của mình** và lưu trong file `.txt`.
- Mỗi dòng trong file phải chứa **1 gift code**.
- Nếu redeem thất bại hãy kiểm tra:
  - kết nối internet
  - file cookies còn hợp lệ
  - danh sách gift code đã chuẩn bị

---

## Tuyên bố miễn trừ trách nhiệm

Dự án này được tạo **chỉ nhằm mục đích học tập và tự động hoá cá nhân**.

Tác giả **không khuyến khích việc lạm dụng hệ thống game**.

Tác giả **không chịu trách nhiệm** cho:

- tài khoản bị khóa hoặc bị cấm
- việc sử dụng sai mục đích
- các thay đổi từ phía Garena đối với hệ thống redeem

Người dùng **tự chịu trách nhiệm khi sử dụng công cụ này**.

---

## Tác giả

Developed by:

```
Mentornoob
```

GitHub:

```
https://github.com/Mentornoob
```

⭐ Nếu bạn thấy dự án hữu ích hãy **Star repo**.