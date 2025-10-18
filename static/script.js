// مرکز نقشه روی ایران
const map = L.map('map').setView([32.0, 53.0], 5);

// لایه OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

// اضافه کردن لوکیشن‌ها
data.forEach(d => {
    let color = 'black';
    if(d.visit_status === 'بازدید شده') color = 'blue';
    else if(d.visit_status === 'بازدید نشده') color = 'red';

    if(d.lat && d.lon){
        const marker = L.circleMarker([d.lat, d.lon], {color, radius: 8}).addTo(map);

        marker.bindPopup(`
            <b>نام فروشگاه:</b> ${d.store_name}<br>
            <b>پذیرنده:</b> ${d.owner_name}<br>
            <b>ترمینال:</b> ${d.terminal_id}<br>
            <b>آدرس:</b> ${d.address}<br>
            <b>تلفن:</b> ${d.phone}<br>
            <b>موبایل:</b> ${d.mobile}<br>
            <b>تعداد تراکنش:</b> ${d.transaction_count}<br>
            <b>مبلغ تراکنش:</b> ${d.transaction_amount}
        `);
    }
});
