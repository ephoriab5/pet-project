from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, Enum, func
from datetime import datetime
from database import Base

class Booking(Base):
    __tablename__ = "booking"

    booking_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    guest_id: Mapped[int] = mapped_column(Integer, nullable=False)
    room_id: Mapped[int] = mapped_column(Integer, nullable=False)
    check_in: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    check_out: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(Enum('paid', 'pending'), server_default='pending', nullable=False)
    staff_id: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())