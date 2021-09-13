from .models import Country
from ariadne import QueryType, MutationType
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from . import db
#File containing graphql resolvers(queries)

#establish binder that binds resolvers to schema // alternative query=ObjectType("Query")
query = QueryType()
mutation = MutationType()


#bind resolver to schema item with query.field
@query.field("listCountries")
def listCountries_resolver(obj, info):
    """Get all countries from database and modify output- resolver"""
    try:
        countries = [country.to_dict() for country in Country.query.all()]
        payload = {
            "success": True,
            "countries": countries
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@query.field("getCountry")
def getCountry_resolver(obj, info, id):
    """Get single country by ID- resolver"""
    try:
        country = Country.query.get(id)
        payload = {
            "success": True,
            "country": country.to_dict()
        }
    except AttributeError:  # country not found
        payload = {
            "success": False,
            "errors": ["Country matching {id} not found"]
        }
    return payload

@query.field("countries")
def resolve_countries(*_):
    """Simple way to create graphql resolver that lists all items from the model"""
    return Country.query.all()

@mutation.field("createCountry")
def resolve_create_country(obj, info, input):
    """mutation type resolver to create country(item)"""
    try:
        country = Country(
            iso=input['iso'], name=input['name']
        )
        db.session.add(country)
        db.session.commit()
        payload = {
            "success": True,
            "country": country.to_dict()
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

@mutation.field("updateCountry")
def update_country_resolver(obj, info, id, input):
    """Update country by its ID"""
    try:
        country = Country.query.get(id)
        if country:
            country.iso = input['iso']
            country.name = input['name']
        db.session.add(country)
        db.session.commit()
        payload = {
            "success": True,
            "country": country.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@mutation.field("deleteCountry")
def delete_country_resolver(obj, info, id):
    try:
        country = Country.query.get(id)
        db.session.delete(country)
        db.session.commit()
        payload = {"success": True, "country": country.to_dict()}
    except:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload

@mutation.field("bulkCreateCountry")
def resolve_bulk_create_country(obj, info, input):
    """mutation type resolver to bulk create country/countries"""
    try:
        countries=[Country(iso=country['iso'], name=country['name']) 
        for country in input]

        # country = Country(
        #     iso=input['iso'], name=input['name']
        # )
        db.session.add_all(countries)
        db.session.commit()
        payload = {
            "success": True,
            "countries": countries
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

@query.field("hello")
def resolve_hello(*_):
    return "Hello!"