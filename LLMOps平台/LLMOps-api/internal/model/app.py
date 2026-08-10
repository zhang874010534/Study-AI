from datetime import datetime
import uuid

from internal.extension.database_extension import db
from sqlalchemy import Column, UUID, Text, String, DateTime, PrimaryKeyConstraint, Index


class App(db.Model):
    __tablename__ = 'app'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pk_app_id'),
        Index('idx_app_account_id', 'account_id'),
    )

    id = Column(UUID, default=uuid.uuid4, nullable=False)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    status = Column(String(255), default="", nullable=False)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
