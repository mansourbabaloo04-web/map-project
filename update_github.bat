@echo off
cd /d "C:\Users\HP\Desktop\map"
echo ========================================
echo 🔄 در حال بروز رسانی امن پروژه در GitHub (SSH)
echo ========================================

git add .
git commit -m "Daily secure auto update"
git push origin main

echo ✅ پروژه با موفقیت و به صورت امن آپلود شد!
pause
