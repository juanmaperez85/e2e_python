from core.base_page import BasePage


class BasePagePacklink(BasePage):
    def get_base_url(self, context):
        base_url = context.config.get('PACKLINK', 'PROTOCOL')
        return base_url