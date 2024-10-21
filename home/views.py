import flask
from flask_mail import Message
from main.flask_mail import mail


def show_home_page():
    if flask.request.method == "POST":
        msg = Message(
            subject="Новая заявка на сайте",
            sender='rudy.bodik@gmail.com',  # Указан ваш email как отправитель
            recipients=[flask.request.form['email']]  # Обратите внимание, что это список
        )
        msg.body = f"""
        —————————
        Клієнт {flask.request.form['name']} залишив/ла відгук:

        {flask.request.form['response']}.

        Пошта для зворотнього звʼязку з клієнтом {flask.request.form['email']}.
        —————————
        """
        try:
            mail.send(msg)
            print('Письмо успешно отправлено!')
        except Exception as e:
            print(f'Ошибка при отправке письма: {e}')
    return flask.render_template(template_name_or_list="home.html")
