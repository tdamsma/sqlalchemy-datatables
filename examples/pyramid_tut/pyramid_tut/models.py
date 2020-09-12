from sqlalchemy import Column, Date, ForeignKey, Integer, Unicode, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    backref,
    column_property,
    relationship,
    scoped_session,
    sessionmaker,
)
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

Base = declarative_base()


class User(Base):
    """Define a User."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, unique=True)

    birthday = Column(Date)

    address = relationship("Address", uselist=False, backref=backref("user"))

    age = column_property(
        func.strftime("%Y.%m%d", "now")
        - func.strftime("%Y.%m%d", birthday).cast(Integer)
    )

    def __unicode__(self):
        """Give a readable representation of an instance."""
        return "%s" % self.name

    def __repr__(self):
        """Give a unambiguous representation of an instance."""
        return "<%s#%s>" % self.__class__.__name__, self.id


class Address(Base):
    """Define an Address."""

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)

    description = Column(Unicode, unique=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    def __unicode__(self):
        """Give a readable representation of an instance."""
        return "%s" % self.id

    def __repr__(self):
        """Give a unambiguous representation of an instance."""
        return "<%s#%s>" % self.__class__.__name__, self.id
