# Auto Redeem Gift Code – Garena Delta Force

A lightweight Python tool that automatically redeems **Garena Delta Force** gift codes.

This tool uses **Selenium automation** to log in using saved cookies and redeem multiple gift codes automatically from a text file.

---

# Features

* Automatically redeem multiple gift codes
* Login using saved cookies (no manual login required)
* Load gift codes from a `.txt` file
* Simple popup file selector
* Supports building to `.exe`

---

# Requirements

* Python 3.9+
* Google Chrome
* ChromeDriver (matching your Chrome version)

Install required libraries:

```
pip install selenium
```

---

# Project Structure

```
Auto_redeem_Gift_code_Garena_DF
│
├── main.py
├── README.md
├── Gift_code_list.txt
└── cookies.json
```

---

# How to Use

## 1. Export your cookies

Install the **J2TEAM Cookies extension**:

https://chromewebstore.google.com/detail/j2team-cookies/okpidcojinmlaakglciglbpcpajaibco

Then open the redeem page:

```
https://redeem.df.garena.sg
```

Steps:

1. Log in to your Game account
2. Click the **J2TEAM Cookies** extension
3. Export cookies as a **JSON file**
4. Save the file to your computer

---

## 2. Create your gift code list

Create a text file such as:

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

Each line should contain **one gift code**.

---

## 3. Run the tool

Run with Python:

```
python main.py
```

Or download the **compiled EXE file** from the releases section and run it.

The program will:

1. Ask you to select the **cookies file**
2. Ask you to select the **gift code list**
3. Automatically redeem all codes

---

# Build EXE (Optional)

Install PyInstaller:

```
pip install pyinstaller
```

Build the executable:

```
pyinstaller --onefile --noconsole --collect-all selenium main.py
```

The executable will be generated in:

```
dist/main.exe
```

---

# Notes

* Make sure ChromeDriver matches your Chrome version.
* Some gift codes may expire or only work once.

---

# Disclaimer

This project is for **educational and personal automation purposes only**.

The author is not responsible for any misuse or account issues.

---

# Credits

Developed by:

```
Mentornoob
```

GitHub:

```
https://github.com/Mentornoob
```

---

If you find this tool useful, consider giving the repository a ⭐.
