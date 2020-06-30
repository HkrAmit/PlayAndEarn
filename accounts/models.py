from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, mobile, userid, username, password=None):
        """
        Creates and saves a User with the given mobile, userid and password.
        """
        if not mobile:
            raise ValueError('Users must have an mobile number')

        user = self.model(
            mobile=mobile,
            userid=userid,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, userid, password, username):
        """
        Creates and saves a superuser with the given mobile, userid and password.
        """
        user = self.create_user(
            mobile,
            password=password,
            userid=userid,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    mobile = models.CharField(
        verbose_name='mobile number',
        unique=True,
        max_length=11
    )
    userid = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['userid','username']

    def __str__(self):
        return self.mobile

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

