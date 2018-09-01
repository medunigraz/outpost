import os

import django
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'outpost.settings')

django.setup()
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})
