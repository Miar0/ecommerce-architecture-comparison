import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from apps.users.tests.factories import UserFactory

User = get_user_model()


@pytest.fixture
def valid_user_data():
    return {
        "email": "test@example.com",
        "username": "testuser",
        "password": "securepassword",
    }


@pytest.mark.django_db
class TestCustomUserManager:
    def test_create_user_success(self, valid_user_data):
        user = User.objects.create_user(**valid_user_data)

        assert user.email == valid_user_data["email"]
        assert user.username == valid_user_data["username"]
        assert user.is_active is True
        assert user.is_staff is False
        assert user.is_superuser is False
        assert user.check_password(valid_user_data["password"]) is True

    def test_create_user_normalizes_email(self, valid_user_data):
        valid_user_data["email"] = "TEST@EXAMPLE.COM"
        user = User.objects.create_user(**valid_user_data)
        assert user.email == "TEST@example.com"

    def test_create_user_without_email_raises_error(self, valid_user_data):
        valid_user_data["email"] = ""
        with pytest.raises(ValueError, match="The Email field must be set"):
            User.objects.create_user(**valid_user_data)

    def test_create_user_without_username_raises_error(self, valid_user_data):
        valid_user_data["username"] = ""
        with pytest.raises(ValueError, match="The Username field must be set"):
            User.objects.create_user(**valid_user_data)

    def test_create_superuser_success(self, valid_user_data):
        admin = User.objects.create_superuser(**valid_user_data)
        assert admin.is_staff is True
        assert admin.is_superuser is True

    def test_create_superuser_with_is_staff_false_raises_error(self, valid_user_data):
        valid_user_data["is_staff"] = False
        with pytest.raises(ValueError, match="Superuser must have is_staff=True."):
            User.objects.create_superuser(**valid_user_data)

    def test_create_superuser_with_is_superuser_false_raises_error(
        self, valid_user_data
    ):
        valid_user_data["is_superuser"] = False
        with pytest.raises(ValueError, match="Superuser must have is_superuser=True."):
            User.objects.create_superuser(**valid_user_data)


@pytest.mark.django_db
class TestUserModel:
    def test_user_str_representation(self):
        user = UserFactory(email="test_str@example.com")
        assert str(user) == "test_str@example.com"

    def test_email_must_be_unique(self):
        UserFactory(email="unique@example.com")
        with pytest.raises(IntegrityError):
            UserFactory(email="unique@example.com")

    def test_username_must_be_unique(self):
        UserFactory(username="uniqueuser")
        with pytest.raises(IntegrityError):
            UserFactory(username="uniqueuser")

    @pytest.mark.parametrize(
        "invalid_username",
        [
            "usrюзернейм",
            "invalid space",
            "user@name!",
        ],
    )
    def test_username_validators_reject_invalid_data(self, invalid_username):
        user = UserFactory.build(username=invalid_username)

        with pytest.raises(ValidationError) as exc_info:
            user.full_clean()

        assert "username" in exc_info.value.message_dict
