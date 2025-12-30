from flask import Flask, render_template
import os

app = Flask(__name__)

# === FANDOM DATA ===
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
        "donghua": "Yes (Season 5)",
    },
    {
        "title": "Martial Peak",
        "mc": "Yang Kai",
        "start_age": 15,
        "power_system": "Cultivation",
        "breakthroughs": [
            {"level": "Body Tempering", "chapter": 1, "age": 15},
            {"level": "True Element", "chapter": 120, "age": 17},
            {"level": "Saint King", "chapter": 950, "age": 25},
        ],
        "manhua": "Yes",
        "donghua": "Not Yet",
    }
]

@app.route("/")
def index():
    return render_template("index.html", novels=novels)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
