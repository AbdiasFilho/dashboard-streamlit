import smtplib
from email.mime.text import MIMEText

def send_feedback_email(to_email, score, comment):
    msg = MIMEText(f'Obrigado pelo seu feedback!\nNota: {score}\nComentário: {comment}')
    msg['Subject'] = 'Confirmação da sua resposta NPS'
    msg['From'] = 'seuemail@exemplo.com'
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login('seuemail@exemplo.com', 'sua_senha')
        server.send_message(msg)
