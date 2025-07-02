from flask import Flask, render_template, request
import send_email
import send_whatsapp

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    score = request.form['score']
    comment = request.form['comment']
    email = request.form['email']
    phone = request.form['phone']

    # Envio de confirmação
    send_email.send_feedback_email(email, score, comment)
    send_whatsapp.send_feedback_message(phone, score, comment)

    return f"Obrigado por seu feedback! Nota: {score}"

if __name__ == '__main__':
    app.run(debug=True)
