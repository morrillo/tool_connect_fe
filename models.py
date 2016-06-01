# -*- coding: utf-8 -*-
from openerp import models, api, fields


class wsafip_connection(models.Model):
	_inherit = "wsafip.connection"

        @api.model
        def _connect_ws_afip(self):
		connections = self.search([])
		for connection in connections:
			if connection.state != 'connected':
				connection.do_login()
                return None


