import os
import select
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase


load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "m")

DATABASE_URL = f"mysql+aiomysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_async_engine(DATABASE_URL, echo=True)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass




import asyncio

# Створюємо асинхронну функцію для додавання даних
async def seed_rooms():
    # ❗️ ІМПОРТ ТУТ: на початку функції, до відкриття сесії
    from app.models import rooms 
    
    # 1. Відкриваємо сесію (викликаємо кур'єра)
    async with AsyncSessionLocal() as session:
        try:
            # 2. Збираємо посилку (створюємо кімнату)
            room_1 = rooms.Room(
                room_number=104,
                room_category="standard",
                price=1200.00
            )

            room_2 = rooms.Room(
                room_number=303,
                room_category="lux",
                price=3500.50
            )

            # 3. Передаємо кімнати кур'єру
            session.add_all([room_1, room_2])

            # 4. Зберігаємо в базу
            await session.commit()
            
            print("✅ Кімнати успішно додані до бази даних!")

        except Exception as e:
            # Якщо щось пішло не так (наприклад, кімната 101 вже існує)
            await session.rollback()
            print(f"❌ Помилка: {e}")

# Цей рядок запускає нашу функцію


import asyncio

async def select_rooms():
    from sqlalchemy import select
    from app.models import rooms
    async with AsyncSessionLocal() as session:
        try:
            s = select(rooms.Room).where(rooms.Room.room_number % 2 != 0)
            result = await session.execute(s)
            rooms_list = result.scalars().all()

            print("✅ Список кімнат:")
            for room in rooms_list:
                print(f"Номер: {room.room_number}, Категорія: {room.room_category}, Ціна: {room.price}")

        except Exception as e:
            print(f"❌ Помилка: {e}")
            
if __name__ == "__main__":
    asyncio.run(select_rooms())