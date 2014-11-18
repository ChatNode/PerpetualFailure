from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Text,
)

from perpetualfailure.db import session, Base
import perpetualfailure.news


class News_Article(Base):
    __parent__ = perpetualfailure.news.root
    __tablename__ = "news_article"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    title = Column(Text)
    content = Column(Text)

    def __init__(self):
        self.title = "Untitled"
        self.content = ""

