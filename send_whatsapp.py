from twilio.rest import Client

def send_feedback_message(phone, score, comment):
    account_sid = 'SEU_SID'
    auth_token = 'SEU_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Obrigado pelo feedback!\nNota: {score}\nComentário: {comment}',
        to=f'whatsapp:{phone}'
    )
