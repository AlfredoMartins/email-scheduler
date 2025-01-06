import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import csv
import random
from datetime import datetime

random.seed(int(datetime.now().microsecond))

load_dotenv()

GMAIL_USERNAME = os.environ.get("GMAIL_USERNAME", "your_email@gmail.com")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD", "your_password")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
RECEIVER = 'geral@aima.gov.pt'
BCC = 'codetyper.angola@gmail.com'

def reset():
    msg = EmailMessage()
    msg['Subject'] = f'RE: Urgente - Estudante [Pedido de Agendamento para Título de Residência] | {random.randint(0, 999999999)}'
    msg['From'] = 'Alfredo Martins'
    msg['To'] = RECEIVER
    msg['Bcc'] = BCC

    with open('content.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        content = "\n".join(" ".join(row) for row in reader)

    msg.set_content(content)

    # Read attachments
    files = ['passport.png', 'visa.png']
    dir_path = './files/'
    for name in files:
        file_path = os.path.join(dir_path, name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
                file_type = name.split('.')[-1]
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=name)
        else:
            print(f"File not found: {file_path}")
    
    return msg

# Send email
def send_email():
    msg = reset()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        server.send_message(msg)
        print("Sent...")

# send_email() ❯ python3 app.py