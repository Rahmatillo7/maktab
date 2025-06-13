from jose import jwt
from datetime import datetime, timedelta


SECRET_KEY = "super-maxfiy-kalit"
ALGORITHM = "HS256"


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


def create_token(user):
    payload = {
        "sub": user.username,  # subject: foydalanuvchi nomi
        "role": user.role,     # foydalanuvchining roli
        "exp": datetime.utcnow() + timedelta(hours=1)  # token 1 soat ishlaydi
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


if __name__ == "__main__":
    user = User(username="ali", role="admin")
    token = create_token(user)
    print("Yaratilgan JWT token:")
    print(token)
