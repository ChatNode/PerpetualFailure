from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    )
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

"""
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)
Index('my_index', MyModel.name, unique=True, mysql_length=255)
"""

class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    title = Column(Text)
    content = Column(Text)

