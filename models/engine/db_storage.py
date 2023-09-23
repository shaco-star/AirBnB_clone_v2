#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''

from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.base_model import Base


class DBStorage:
    """
    Create SQLalchemy database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Create engine and link to MySQL databse (hbnb_dev, hbnb_dev_db)
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV", None)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if env == 'test':
            Base.MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current database session"""
        dict_db = {}
        if cls is not None:
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dict_db[key] = obj
            return dict_db
        else:
            for key, value in models.classes.items():
                if key != "BaseModel":
                    objs = self.__session.query(value).all()
                    if len(objs > 0):
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            dict_db[key] = obj
            return dict_db

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Commit all changes of current database session"""
        self.__session = Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.remove()
