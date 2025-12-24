from pydantic import BaseModel


class SystemUser(BaseModel): # клас систем'юзер(унаслідує BAseModel)
    id: int
    username: str
    email: str
    password: str
    surname: str
    name: str
    is_active: bool
    address: dict  # об’єкт (наприклад, словник з даними адреси)
    contacts: list  # список (наприклад, список номерів або email-адрес)

#перший користувч
user1 = SystemUser(
    id=1000,
    username="user1",
    email="first.krut@gmail.com",
    password="Str0ngPassword123",
    surname="krut",
    name="first",
    is_active=True,
    address={"вулиця":"раменьска","будинок":"4", "під'їзд":"2", "квартира":"243"},
    contacts=["050123123123", "0123123123", "093123123123", "067123123123"],
)


# Отримання JSON
user_json_str = user1.model_dump_json()

with open("system_user.json", "w") as f:
    f.write(user_json_str) # запис у джсон файл


with open("system_user.json", "r") as s:
    user2 = SystemUser.model_validate_json(s.read()) # читання файлу і перетворення у стр

print(user2)
print(type(user2))