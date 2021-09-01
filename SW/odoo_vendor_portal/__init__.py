# -*- coding: utf-8 -*-
#################################################################################
# Author	  : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################

from . import models
from . import controllers
from . import wizard
def pre_init_check(cr):
	from odoo.service import common
	from odoo.exceptions import Warning
	versionInfo = common.exp_version()
	serverSerie =versionInfo.get('server_serie')
	if serverSerie!='12.0':
		raise Warning(
		'Module support Odoo series 12.0, found {}.'.format(serverSerie))
	return True
