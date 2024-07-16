from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ Менеджер объекта для создания пользователя и суперпользователя"""

    def create_user(self, email, first_name, last_name, phone, image=None, password=None, role="user"):
        """
        Функция создания пользователя
        """
        if not email:
            raise ValueError("У пользователей должен быть адрес электронной почты")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            image=image,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, image=None, password=None, role="admin"):
        """
        Функция создания суперпользователя — с ее помощью мы создаем администратора,
        с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            image=image,
            password=password,
            role=role
        )
        user.save(using=self._db)
        return user
