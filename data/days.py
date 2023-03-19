import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Days(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'days'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    day = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sh = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fuel = sqlalchemy.Column(sqlalchemy.String, nullable=True)
