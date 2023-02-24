from odoo import fields, models, api, tools

class StudentDetails(models.Model):
    _name = "student.details"

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="Birthdate")
    address = fields.Text(string="Address")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default='male')
    std = fields.Many2one('std.std', string="Standard")

    reference_number = fields.Char(string="Number", required=True, index=True, copy=False, default='New', readonly=True)


    def unlink(self):
        a = self.env['student.marks'].search([('name', 'like', self.name)])
        for i in a:
            if i.id != self.id:
                i.unlink()
        rec = super(StudentDetails, self).unlink()
        return rec



    @api.model
    def create(self, vals):
        if vals.get('reference_number', 'New'):
            vals['reference_number'] = self.env['ir.sequence'].next_by_code('reference.order') or 'New'
        return super(StudentDetails, self).create(vals)