
from flask import Flask, render_template
import os

app = Flask(__name__)

novels = [
    {
        "title": "Battle Through The Heavens",
        "mc": "Xiao Yan",
        "start_age": 15,
        "power_system": "Dou Qi",
        "breakthroughs": [
            {"level": "Dou Zhe", "chapter": 1, "age": 15},
            {"level": "Dou Shi", "chapter": 200, "age": 17},
            {"level": "Dou Zong", "chapter": 700, "age": 22},
        ],
        "manhua": "Yes",
        "donghua": "Season 5",
    }
]

@app.route("/")
def home():
    return render_template("index.html", novels=novels)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
