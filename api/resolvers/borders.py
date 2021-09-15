from ..models import Border
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from .. import db
from ariadne import QueryType, MutationType, ObjectType
query = QueryType()
mutation = MutationType()

#bind resolver to schema item with query.field
@query.field("listBorders")
def listBorders_resolver(obj, info):
    """Get all countries from database and modify output- resolver"""
    try:
        borders = [border.to_dict() for border in Border.query.all()]
        payload = {
            "success": True,
            "borders": borders
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@mutation.field("createBorder")
def resolve_create_border(obj, info, input):
    """mutation type resolver to create country(item)"""
    try:
        border = Border(
            origin_id=input['origin_id'], destination_id=input['destination_id'], status=input["status"]
        )
        db.session.add(border)
        db.session.commit()
        payload = {
            "success": True,
            "country": border.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect data"]
        }
    except IntegrityError as e:
        if type(e.orig)==UniqueViolation:
            payload = {
                "success": False,
                "errors": [f"Duplicate values"]
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Integrity error"]
            }
    return payload