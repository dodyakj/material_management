from odoo import models, fields, api

class Material(models.Model):
    _name = 'material.material'
    _description = 'Material'
    _rec_name = 'material_code'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    material_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('material.supplier', string='Related Supplier', required=True)

    @api.constrains('material_price')
    def _check_material_price(self):
        for record in self:
            if record.material_price < 100:
                raise models.ValidationError("Material Buy Price must be greater than or equal to 100.")