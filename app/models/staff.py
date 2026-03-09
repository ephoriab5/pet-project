from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String , DateTime, func
from datetime import datetime
from database import Base

class Staff(Base):
    __tablename__ = "staff"

    staff_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    posada: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())