from datetime import datetime
import logging
log = logging.getLogger(__name__)

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Table,
    Text,
)
from sqlalchemy.orm import relationship, backref

from perpetualfailure.db import Base, session


revision_rel = Table('knowledgebase_article_rel_revision', Base.metadata,
                     Column('article', Integer, ForeignKey('knowledgebase_article.id'), primary_key=True),
                     Column('revision', Integer, ForeignKey('knowledgebase_article_revision.id'))
                    )


class KB_Article(Base):
    __tablename__ = "knowledgebase_article"
    id = Column(Integer, primary_key=True)

    parent_id = Column('parent', Integer, ForeignKey("knowledgebase_article.id"))
    children = relationship("KB_Article", backref=backref('parent', remote_side=[id]))

    revision = relationship('KB_ArticleRevision', secondary=lambda: revision_rel, uselist=False)

    name = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)

    def __init__(self):
        self.title = "Untitled"
        self.name = "unnamed"
        self.content = ""

        self.revision_id = None
        self.parent = None

    def path(self):
        # Start at the bottom and walk upwards
        item = self
        # If we're checking the root article, bail now
        if item.parent is None and item.name == "index": return ""
        # Add this article to the path
        path = [self.name]
        # Loop through all parents
        while item.parent:
            item = item.parent
            # Again; bail if root article
            if item.parent is None and item.name == "index": break
            # Add to path
            path.insert(0, item.name)
        # Add an empty string to the start of the array so that we'll get a
        # slash between "/kb" and the path matchdict variable when using
        # request.route_url/path.
        path.insert(0, "")
        return "/".join(path)


class KB_ArticleRevision(Base):
    __tablename__ = "knowledgebase_article_revision"
    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)

    parent_id = Column('parent', Integer, ForeignKey("knowledgebase_article_revision.id"))
    children = relationship("KB_ArticleRevision", backref=backref('parent', remote_side=[id]))

    article_id = Column(Integer, ForeignKey('knowledgebase_article.id'), nullable=False)
    article = relationship('KB_Article', backref='revisions')

    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)

    def __init__(self, article):
        self.article = article
        self.time = datetime.utcnow()
        self.title = article.title
        self.content = article.content
