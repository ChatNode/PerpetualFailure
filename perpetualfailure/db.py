from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    )
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
)
from zope.sqlalchemy import ZopeTransactionExtension


session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class News_Article(Base):
    __tablename__ = "news_article"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    title = Column(Text)
    content = Column(Text)

