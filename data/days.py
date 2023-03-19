import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Days(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'days'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    day = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sh = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    power_to_engine = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    temperature = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    oxygen = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fuel = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    weight = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    distance_to_next_point = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    energy = sqlalchemy.Column(sqlalchemy.String, nullable=True)
