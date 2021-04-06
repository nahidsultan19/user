from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # for user profile auto add image
    def ready(self):
        import users.signals
