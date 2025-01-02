from flask import Flask, request, render_template, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Serves the HTML page

@app.route("/generate", methods=["POST"])
def generate_qr():
    data = request.form.get("data")  # Get the text/URL from the form
    if not data:
        return "No data provided", 400

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="yellow", back_color="blue")

    # Save the image to a BytesIO object to send as a response
    buffer = BytesIO()
    img.save(buffer, "PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png", as_attachment=False, download_name="REYA.png")

if __name__ == "__main__":
    app.run(debug=True)
