from . import api

v1 = [
    (
        r'campusonline/room',
        api.RoomViewSet,
        'campusonline-room'
    ),
    (
        r'campusonline/function',
        api.FunctionViewSet,
        'campusonline-function'
    ),
    (
        r'campusonline/organization',
        api.OrganizationViewSet,
        'campusonline-organization'
    ),
    (
        r'campusonline/person',
        api.PersonViewSet,
        'campusonline-person'
    ),
    (
        r'campusonline/personorganizationfunction',
        api.PersonOrganizationFunctionViewSet,
        'campusonline-personorganizationfunction'
    ),
    (
        r'campusonline/distributionlist',
        api.DistributionListViewSet,
        'campusonline-distributionlist'
    ),
    (
        r'campusonline/finalthesis',
        api.FinalThesisViewSet,
        'campusonline-finalthesis'
    ),
    (
        r'campusonline/event',
        api.EventViewSet,
        'campusonline-event'
    ),
    (
        r'campusonline/bulletin:page',
        api.BulletinPageViewSet,
        'campusonline-bulletin-page'
    ),
    (
        r'campusonline/bulletin',
        api.BulletinViewSet,
        'campusonline-bulletin'
    ),
    (
        r'campusonline/search/bulletin:page',
        api.BulletinPageSearchViewSet,
        'campusonline-search-bulletin-page'
    ),
    (
        r'campusonline/course-group-term',
        api.CourseGroupTermViewSet,
        'campusonline-course-group-term'
    ),
]
