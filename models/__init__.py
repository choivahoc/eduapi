from uuid import uuid4
from application.extensions import db


def _uuid4(context):
    return str(uuid4())


class Client(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(128), primary_key=True, default=_uuid4,
                   unique=True)
    name = db.Column(db.String(128), unique=True)
    description = db.Column(db.String(3000), nullable=True)
    secret = db.Column(db.String(128), nullable=True)
    redirect_uri = db.Column(db.String(128), nullable=True)
    return_access_token = db.Column(db.Boolean, nullable=False, default=False)


class Tenant(db.Model):
    name = db.Column(db.String(128), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.String(3000), nullable=True)
    enable = db.Column(db.Boolean, nullable=False, default=True)


class User(db.Model):
    id = db.Column(db.String(128), primary_key=True, default=_uuid4)
    username = db.Column(db.String(250), nullable=False)
    firstname = db.Column(db.String(250))
    lastname = db.Column(db.String(250))
    email = db.Column(db.String(250), default="TBA")
    organization = db.Column(db.String(100))
    country = db.Column(db.String(30))
    address = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    active = db.Column(db.Boolean, nullable=False, default=True)
    creation_time = db.Column(db.BigInteger)
    tenant = db.Column(db.String(128), nullable=False)
    management_role = db.Column(db.Integer, default=0)
    __table_args__ = (db.UniqueConstraint('username', 'tenant', name='_user_tenant_uc'),)
