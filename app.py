from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import json

app = Flask(__name__)
app.secret_key = "123456"

# ==== خواندن کاربران ====
users_df = pd.read_excel("users.xlsx", sheet_name="data", dtype=str)
users = users_df.to_dict(orient="records")

# ==== خواندن داده‌های لوکیشن‌ها ====
with open("static/data.json", encoding="utf-8") as f:
    all_data = json.load(f)

# ==== صفحه ورود ====
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = next((u for u in users if u["username"] == username and u["password"] == password), None)
        if user:
            session["user"] = user
            return redirect(url_for("map_view"))
        else:
            return render_template("login.html", error="نام کاربری یا رمز عبور اشتباه است.")
    return render_template("login.html")

# ==== صفحه نقشه ====
@app.route("/map")
def map_view():
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]

    # ==== فیلتر داده‌ها بر اساس نقش ====
    if user["role"] == "pushtiban":
        data = [d for d in all_data if d.get("supporter") == user.get("name_pushtiban")]
    elif user["role"] == "karshenas":
        office = user.get("نام دفتر", "")
        data = [d for d in all_data if office in d.get("office_name", "")]
    else:  # admin
        data = all_data

    return render_template("index.html", user=user, data=data)

# ==== خروج ====
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
