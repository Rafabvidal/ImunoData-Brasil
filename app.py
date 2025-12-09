from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    powerbi_url = (
        "https://app.powerbi.com/reportEmbed?reportId=f941271d-f2d8-4919-b7ea-2605b17f3a9f&autoAuth=true&ctid=43f49b1f-d426-4b32-82a7-62cce76d08f0"
    )
    return render_template("index.html", powerbi_url=powerbi_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
