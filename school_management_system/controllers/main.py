from odoo import http
from odoo.http import request

class StudentData(http.Controller):
	@http.route(['/data/'], type='http', auth='public', website='True')
	def student_data(self, **kwargs):
		data = request.env['student.details'].sudo().search([])
		vals = {'records' : data}
		return request.render('school_management_system.tmp_data', vals)