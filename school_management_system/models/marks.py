from odoo import models, fields, api

class StudentMarks(models.Model):
	_name = "student.marks"


	name = fields.Many2one('student.details', string="Name")
	std = fields.Integer(string="Standard", compute="_compute_std")
	maths = fields.Float(string="Maths")
	science = fields.Float(string="Science")
	social = fields.Float(string="Social science")
	obtained_marks = fields.Float(string="Obtained marks", readonly=True, compute="_compute_marks", store=True)
	total_marks = fields.Float(string="Total marks", default=300, readonly=True)
	percentage = fields.Float(string="Percentage", readonly=True, compute="_compute_percentage", store=True, digits=(12, 2))

	user = fields.Many2one('res.users', string="Admin")


	@api.depends("maths", "science", "social")
	def _compute_marks(self):
		for rec in self:
			if rec.maths and rec.science and rec.social:
				rec.obtained_marks = (rec.maths + rec.science + rec.social)
		return rec

	@api.depends("obtained_marks")
	def _compute_percentage(self):
		for rec in self:
			if rec.obtained_marks:
				rec.percentage = (rec.obtained_marks / 300) * 100
		return rec

	@api.onchange('name')
	def _compute_std(self):
		for rec in self:
			if rec.name:
				rec.std = rec.name.std.name


