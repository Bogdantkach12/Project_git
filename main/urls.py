from .settings import main
import home

home.home_app.add_url_rule(rule = "/", view_func = home.show_home_page, methods = ["GET", "POST"])
main.register_blueprint(blueprint=home.home_app)