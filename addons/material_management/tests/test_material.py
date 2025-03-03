from odoo.tests.common import TransactionCase

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env['material.material']
        self.Supplier = self.env['material.supplier']

        self.supplier = self.Supplier.create({
            'name': 'Test Supplier'
        })

        self.material = self.Material.create({
            'material_code': 'TEST001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_price': 150,
            'supplier_id': self.supplier.id
        })

    def test_material_creation(self):
        self.assertEqual(self.material.material_code, 'TEST001')
        self.assertEqual(self.material.material_name, 'Test Material')
        self.assertEqual(self.material.material_type, 'fabric')
        self.assertEqual(self.material.material_price, 150)
        self.assertEqual(self.material.supplier_id.name, 'Test Supplier')

    def test_material_price_constraint(self):
        with self.assertRaises(Exception):
            self.Material.create({
                'material_code': 'TEST002',
                'material_name': 'Test Material 2',
                'material_type': 'jeans',
                'material_price': 50,
                'supplier_id': self.supplier.id
            })

    def test_material_update(self):
        self.material.write({'material_price': 200})
        self.assertEqual(self.material.material_price, 200)

    def test_material_deletion(self):
        self.material.unlink()
        self.assertFalse(self.material.exists())