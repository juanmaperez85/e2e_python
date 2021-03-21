from __future__ import unicode_literals
from core.base_page_packlink import BasePagePacklink

class LoginPage(BasePagePacklink):
    url = "auth.packlink.com/es-ES/pro/login?platform=PRO&platform_country=ES"
    username = "#email"
    password = "#password"
    login_button = "button[type=submit]"
