import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    username = factory.Sequence(lambda n: f"testuser{n}")

    password = factory.PostGenerationMethodCall("set_password", "testpass123")

    is_active = True
    is_staff = False
    is_superuser = False
