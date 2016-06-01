# -*- coding: utf-8 -*-
from openerp import models, api, fields


class wsafip_connection(models.Model):
	_inherit = "wsafip.connection"

        @api.model
        def _connect_ws_afip(self):
		import pdb;pdb.set_trace()
                return None


