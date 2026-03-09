from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DECIMAL, Enum, DateTime, func
from datetime import datetime
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    booking_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    method: Mapped[str] = mapped_column(Enum('cash', 'card'), nullable=False)
    paid_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())