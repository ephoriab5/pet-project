import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# 1. Завантажуємо дані для підключення з існуючого файлу .env
load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "m")

DATABASE_URL = f"mysql+aiomysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 2. Створюємо підключення (Engine)
engine = create_async_engine(DATABASE_URL, echo=True)

# 3. Створюємо фабрику сесій
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 4. Оскільки ми не створюємо окремих файлів, базовий клас для моделей теж живе тут
class Base(DeclarativeBase):
    pass



import asyncio
from app.models import rooms  # Імпортуємо нашу "коробку" для кімнати

# Створюємо асинхронну функцію для додавання даних
async def seed_rooms():
    # 1. Відкриваємо сесію (викликаємо кур'єра)
    async with AsyncSessionLocal() as session:
        try:
            # 2. Збираємо посилку (створюємо кімнату)
            # room_id та status не вказуємо — база даних підставить їх автоматично!
            room_1 = rooms.Room(
                room_number=101,
                room_category="standard",
                price=1200.00
            )

            room_2 = rooms.Room(
                room_number=205,
                room_category="lux",
                price=3500.50
            )

            # 3. Передаємо кімнати кур'єру (додаємо в сесію)
            # Можна додавати по одній: session.add(room_1), або відразу кілька:
            session.add_all([room_1, room_2])

            # 4. Зберігаємо в базу (підписуємо накладну)
            await session.commit()
            
            print("✅ Кімнати успішно додані до бази даних!")

        except Exception as e:
            # Якщо щось пішло не так (наприклад, кімната 101 вже існує)
            await session.rollback()
            print(f"❌ Помилка: {e}")

# Цей рядок запускає нашу функцію, коли ми запускаємо файл main.py
if __name__ == "__main__":
    asyncio.run(seed_rooms())


        