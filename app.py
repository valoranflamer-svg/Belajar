from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Hallo")


@app.route("/proses", methods=["POST"])
def proses():
    nama = request.form["nama"]
    umur = request.form["umur"]
    sekolah = request.form["sekolah"]

    return render_template(
        "hasil.html",
        nama=nama,
        umur=umur,
        sekolah=sekolah
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
