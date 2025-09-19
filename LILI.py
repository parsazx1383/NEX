```python
import requests
import json

# تنظیم هدرها
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "X-Access-Token": "0iGjPQpJrKCpEKFeb0OjN6NRuN6fmbWqeDran0FP90RRSJoBm7br6r6Ttj5wJcu7",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://gharar.ir",
    "Authorization": ""  # اگر توکن Authorization خاصی نیاز است، اینجا اضافه کنید
}

# بدنه درخواست
payload = {
    "termsConfirmed": False,
    "phone": "09935672418"
}

# URL API
url = "https://gharar.ir/users/phone_number/"

# تابع برای ارسال درخواست
def send_request():
    try:
        # ارسال درخواست POST
        response = requests.post(url, headers=headers, json=payload)
        
        # بررسی وضعیت پاسخ
        if response.status_code == 200:
            print("Success: Request sent successfully!")
            print("Response:", response.json())
        else:
            print(f"Error: Status code {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"Error: {str(e)}")

# اجرای درخواست
if __name__ == "__main__":
    # گرفتن شماره تلفن از کاربر
    phone_number = input("لطفاً شماره تلفن را وارد کنید (یا Enter برای استفاده از شماره پیش‌فرض 09935672418): ")
    if phone_number:
        payload["phone"] = phone_number
    
    send_request()
```