from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# 當使用者連線到首頁 ("/") 時，執行這個函式
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    # 如果使用者按下了送出意見 (POST請求)
    if request.method == "POST":
        feedback = request.form.get("feedback")
        if feedback:
            # 儲存意見到 txt 檔案
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("feedback.txt", "a", encoding="utf-8") as file:
                file.write(f"時間：{now}\n意見：{feedback}\n{'-'*20}\n")
            message = "感謝！您的意見已成功送出並隱藏儲存。"
            
    # render_template 會自動去找 templates 資料夾下的 index.html
    return render_template("index.html", message=message)
@app.route("/about")
def about():
    # 當進入 /about 網址時，會去尋找 templates 裡面的 about.html
    return render_template("about.html")
if __name__ == "__main__":
    # 啟動網站伺服器
    app.run(debug=True)