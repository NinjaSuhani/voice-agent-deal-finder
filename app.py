from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Google Sheets Setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Sneaker Deals").sheet1

def send_email(deals):
    from_email = "your_email@gmail.com"
    to_email = "receiver_email@gmail.com"
    password = "your_gmail_app_password"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Top Sneaker Deals"
    message["From"] = from_email
    message["To"] = to_email

    html = "<h3>Top 3 Sneaker Deals:</h3><ul>"
    for deal in deals:
        html += f"<li>{deal['Seller Name']} - ₹{deal['Price']} - Delivery in {deal['Delivery Time']} days</li>"
    html += "</ul>"

    message.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())

@app.route('/log_seller_data', methods=['POST'])
def log_data():
    data = request.json
    row = [
        data.get("seller_name"),
        data.get("price"),
        data.get("delivery_time"),
        data.get("availability"),
        data.get("timestamp")
    ]
    sheet.append_row(row)

    records = sheet.get_all_records()
    if len(records) >= 3:
        sorted_deals = sorted(records, key=lambda x: float(x["Price"]))
        send_email(sorted_deals[:3])

    return "Data logged and email sent (if applicable)", 200

if __name__ == "__main__":
    app.run(debug=True, port=10000)
