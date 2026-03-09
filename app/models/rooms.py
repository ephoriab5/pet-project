from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DECIMAL, Enum , DateTime, func
from datetime import datetime
from database import Base

class Room(Base):
    __tablename__ = "rooms"

    room_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    room_number: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    room_category: Mapped[str] = mapped_column(Enum('standard', 'lux', 'suite'), nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(Enum('available', 'booked'), server_default='available', nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())