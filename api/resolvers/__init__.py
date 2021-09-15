from .base import query as baseQuery
from .countries import query as countriesQuery
from .countries import mutation as countriesMutation
from .borders import query as bordersQuery
from .borders import mutation as bordersMutation

resolvers = [baseQuery, countriesQuery, countriesMutation, bordersQuery, bordersMutation]