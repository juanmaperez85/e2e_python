from __future__ import unicode_literals
from core.base_page_packlink import BasePagePacklink


class DashboardPage(BasePagePacklink):
    url = "pro.packlink.es/private"
    welcome_text = ".empty-state__title"
    header_actions = ".app-header__actions"
    new_shipment = header_actions + " div.button-dropdown"
