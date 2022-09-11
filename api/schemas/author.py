from api import ma
from api.models.author import AuthorModel
from api.schemas.author import author_schema, authors_schema

class AuthorSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = AuthorModel
       exclude = ("id", )

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)