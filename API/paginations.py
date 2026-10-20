from rest_framework.pagination import LimitOffsetPagination

class pagination_pagenumber(LimitOffsetPagination):
    limit_query_param='limit'
    offset_query_param='off'
    default_limit=4
    max_limit=44