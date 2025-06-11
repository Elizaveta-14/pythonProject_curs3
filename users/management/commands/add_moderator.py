from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class Command(BaseCommand):
    """
    Кастомная команда Django для добавления модератора.

    Создаёт пользователя с правами модератора, используя переданные имя пользователя, email и пароль.
    Добавляет пользователя в группу Moderators с соответствующими правами.
    """
    help = 'Создаёт пользователя с правами модератора'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Имя пользователя модератора', required=True)
        parser.add_argument('--email', type=str, help='Email модератора', required=True)
        parser.add_argument('--password', type=str, help='Пароль модератора', required=True)

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        email = options['email']
        password = options['password']
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'Пользователь {username} уже существует.'))
            return
        group, created = Group.objects.get_or_create(name='Moderators')
        if created:
            self.stdout.write(self.style.WARNING('Группа Moderators создана.'))
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_active=True
        )
        user.groups.add(group)
        self.stdout.write(self.style.SUCCESS(f'Модератор {username} успешно создан и добавлен в группу Moderators.'))