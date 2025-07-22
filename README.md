
# Django Docker Compose Practice

یک پروژه ساده Django با PostgreSQL که با Docker Compose اجرا می‌شود.  
هدف تمرین راه‌اندازی سریع و مدیریت متغیرهای محیطی است.

---

## پیش‌نیازها

- Docker و Docker Compose نصب شده
- کلید SSH برای GitHub (اگر می‌خوای با SSH پوش کنی)

---

## اجرا

1. مخزن را کلون کن:

```bash
git clone git@github.com:fatemehkhosravi002/django-docker-compose-practice.git
cd django-docker-compose-practice
```

2. فایل `.env` بساز و متغیرها را وارد کن (می‌توانی از `.env.example` استفاده کنی):

```env
SECRET_KEY=your_secret_key_here
POSTGRES_DB=testdb
POSTGRES_USER=bahar
POSTGRES_PASSWORD=Bfafa1381
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

3. کانتینرها را اجرا کن:

```bash
docker compose up --build
```

4. در مرورگر برو به:

```
http://localhost:8000/hello/YourName/
```

---

## نکات

- فایل `.env` نباید به گیت پوش شود.  
- اگر پورت 5432 اشغال است، در `docker-compose.yml` تغییرش بده.  
- پروژه برای تمرین است، مناسب production نیست.

---

## مشارکت

اگر پیشنهادی داری، Pull Request خوش‌آمد است!

---

## تماس

برای سوالات با من در تماس باش
