import os
import psutil
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Workload(Base):
    __tablename__ = "workload"
    id: Mapped[int] = mapped_column(primary_key=True)
    time: Mapped[str]
    cpu: Mapped[str]
    total_virtual_memory: Mapped[str]
    total_memory: Mapped[str]
    used_virtual_memory: Mapped[str]
    used_memory: Mapped[str]






