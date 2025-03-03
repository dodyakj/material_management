from odoo import http
from odoo.http import request, Response
import json

class MaterialController(http.Controller):

    @http.route('/api/materials', type='http', auth='none', methods=['GET'], csrf=False)
    def get_materials(self, **kwargs):
        material_type = kwargs.get('material_type')
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type))
        materials = request.env['material.material'].sudo().search(domain)
        material_list = []
        for material in materials:
            material_list.append({
                'material_code': material.material_code,
                'material_name': material.material_name,
                'material_type': material.material_type,
                'material_price': material.material_price,
                'supplier_name': material.supplier_id.name
            })
        return Response(json.dumps(material_list), content_type='application/json')

    @http.route('/api/materials', type='json', auth='none', methods=['POST'], csrf=False)
    def create_material(self, **kwargs):
        material_data = json.loads(request.httprequest.data)
        new_material = request.env['material.material'].sudo().create({
            'material_code': material_data.get('material_code'),
            'material_name': material_data.get('material_name'),
            'material_type': material_data.get('material_type'),
            'material_price': material_data.get('material_price'),
            'supplier_id': material_data.get('supplier_id')
        })
        return {'id': new_material.id}

    @http.route('/api/materials/<int:id>', type='json', auth='none', methods=['PUT'], csrf=False)
    def update_material(self, id, **kwargs):
        material_data = json.loads(request.httprequest.data)
        material = request.env['material.material'].sudo().browse(id)
        if material:
            material.write(material_data)
            return {'status': 'success'}
        return {'status': 'not found'}

    @http.route('/api/materials/<int:id>', type='http', auth='none', methods=['DELETE'], csrf=False)
    def delete_material(self, id, **kwargs):
        material = request.env['material.material'].sudo().browse(id)
        if material:
            material.unlink()
            return Response(json.dumps({'status': 'success'}), content_type='application/json')
        return Response(json.dumps({'status': 'not found'}), content_type='application/json')