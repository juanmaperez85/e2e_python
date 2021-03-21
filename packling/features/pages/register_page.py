from __future__ import unicode_literals
from core.base_page_packlink import BasePagePacklink


class RegisterPage(BasePagePacklink):
    url = "pro.packlink.es/registro"

    email = "#email"
    label_email = "label[for=email]"

    password = "#password"
    label_password = "label[for=password]"

    shipment = "div[data-id=shipments]"
    label_shipment = "label[for=shipments]"

    webshop = "#ecommerces"
    label_webshop = "label[for=ecommerces]"

    marketplace = "#marketplace"
    label_marketplace = "label[for=marketplace]"

    phone = "#phone"
    label_phone = "label[for=phone]"

    terms_conditions_link = ".field__text > span > a:nth-child(1)"
    privacy_link = ".field__text > span > a:nth-child(2)"
    register_button = "button[type=submit]"
