# settings.py или где у вас инициализируется shop_app
from main.settings import main
from flask_mail import Mail

main.config['MAIL_SERVER'] = 'smtp.gmail.com'
main.config['MAIL_PORT'] = 587
main.config['MAIL_USE_TLS'] = True  # Используйте TLS для безопасности
main.config['MAIL_USERNAME'] = 'rudy.bodik@gmail.com'
main.config['MAIL_PASSWORD'] = 'eeof nrwy lnss zfmn'  # Убедитесь, что это ваш реальный пароль или пароль приложения
main.config['MAIL_DEFAULT_SENDER'] = 'rudy.bodik@gmail.com'

mail = Mail(main)
