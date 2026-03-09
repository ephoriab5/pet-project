import asyncio
from sqlalchemy import select
from database import AsyncSessionLocal
from app.models.rooms import Room
from app.models.guests import Guest
from app.models.staff import Staff
from app.models.booking import Booking
from app.models.payments import Payment
from app.models.room_occupancy import RoomOccupancy

async def test_db():
    async with AsyncSessionLocal() as session:
        rooms = await session.execute(select(Room))
        guests = await session.execute(select(Guest))
        staff = await session.execute(select(Staff))
        bookings = await session.execute(select(Booking))
        payments = await session.execute(select(Payment))
        room_occupancy = await session.execute(select(RoomOccupancy))

        print("✅ Тестування бази даних пройшло успішно!")
        
if __name__ == "__main__":
    asyncio.run(test_db())