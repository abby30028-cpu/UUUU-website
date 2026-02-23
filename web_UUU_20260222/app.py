from flask import Flask, render_template, request
import datetime
import requests

app = Flask(__name__)

# 當使用者連線到首頁 ("/") 時，執行這個函式
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    # 如果使用者按下了送出意見 (POST請求)
    if request.method == "POST":
        feedback = request.form.get("feedback")
        if feedback:
            # 將留言發送到 Google 試算表
            google_script_url = "https://script.google.com/macros/s/AKfycbx2jAK-J2cbkSXbzk2J9NLl2xKOsrapdU3feuDPzl5a0Dt3gSpL5uI1Wi11Twi_l6Hqdg/exec"
            payload = {"message": feedback}
            requests.post(google_script_url, data=payload)
            
            message = "感謝！您的意見已成功送出並記錄。"
            
    # render_template 會自動去找 templates 資料夾下的 index.html
    return render_template("index.html", message=message)
@app.route("/about")
def about():
    # 當進入 /about 網址時，會去尋找 templates 裡面的 about.html
    return render_template("about.html")
if __name__ == "__main__":
    # 啟動網站伺服器
    app.run(debug=True)