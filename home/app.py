import flask

home_app = flask.Blueprint(
    name = "home",
    import_name = "app",
    template_folder = "home/templates"
)