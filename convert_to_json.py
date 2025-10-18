import pandas as pd
import json

# ==== تنظیم مسیر فایل ====
excel_file = "customers.xlsx"  # فایل Excel
json_file = "data.json"        # فایل JSON خروجی

# ستون‌های اصلی مورد نیاز
columns_needed = [
    "شماره ترمینال",
    "نام دفتر",
    "نام فروشگاه",
    "نام و نام خانوادگی پذیرنده",
    "شماره سریال",
    "نسخه پایانه",
    "آدرس",
    "شماره تلفن",
    "تلفن همراه",
    "پشتیبان اصلی",
    "تعداد تراکنش",
    "مبلغ تراکنش",
    "latitude",
    "longitude",
    "وضعیت بازدید",
    "عملیات اعلامی"
]

# نام ستون‌ها به انگلیسی
columns_english = [
    "terminal_id", "office_name", "store_name", "owner_name", "serial", "version",
    "address", "phone", "mobile", "supporter", "transaction_count",
    "transaction_amount", "lat", "lon", "visit_status", "operation"
]

try:
    # ==== خواندن Excel ====
    df = pd.read_excel(excel_file, sheet_name="data", dtype=str)

    # ==== بررسی وجود ستون‌های ضروری ====
    for col in columns_needed:
        if col not in df.columns:
            raise ValueError(f"❌ ستون '{col}' در Excel پیدا نشد!")

    # ==== استخراج ستون‌های لازم ====
    df = df[columns_needed]

    # ==== تبدیل latitude و longitude به float ====
    df["latitude"] = pd.to_numeric(df["latitude"], errors='coerce')
    df["longitude"] = pd.to_numeric(df["longitude"], errors='coerce')

    # ==== تغییر نام ستون‌ها ====
    df.columns = columns_english

    # ==== ذخیره JSON ====
    df.to_json(json_file, orient="records", force_ascii=False)
    print(f"✅ JSON ساخته شد و در مسیر '{json_file}' ذخیره شد.")

except FileNotFoundError:
    print(f"❌ فایل '{excel_file}' پیدا نشد. مطمئن شوید فایل در همان فولدر قرار دارد.")
except ValueError as ve:
    print(str(ve))
except Exception as e:
    print("❌ خطا هنگام پردازش فایل Excel:", str(e))
