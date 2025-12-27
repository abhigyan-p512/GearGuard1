from odoo import models, fields, api

class EquipmentCategory(models.Model):
    _name = 'equipment.category'
    _description = 'Equipment Category'

    name = fields.Char(string='Category Name', required=True)

class Equipment(models.Model):
    _name = 'equipment.equipment'
    _description = 'Equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Equipment Name', required=True)
    serial_number = fields.Char(string='Serial Number')
    purchase_date = fields.Date(string='Purchase Date')
    warranty_info = fields.Text(string='Warranty Information')
    location = fields.Char(string='Location')
    department_id = fields.Many2one('hr.department', string='Department')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    maintenance_team_id = fields.Many2one('maintenance.team', string='Maintenance Team')
    technician_id = fields.Many2one('res.users', string='Technician', default=lambda self: self.env.user)
    category_id = fields.Many2one('equipment.category', string='Category')

    # Smart button for maintenance requests
    def action_view_maintenance_requests(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Maintenance Requests',
            'view_mode': 'tree,form',
            'res_model': 'maintenance.request',
            'domain': [('equipment_id', '=', self.id)],
            'context': {'default_equipment_id': self.id},
        }

    def _compute_maintenance_request_count(self):
        for record in self:
            record.maintenance_request_count = self.env['maintenance.request'].search_count([
                ('equipment_id', '=', record.id),
                ('stage', '!=', 'repaired')
            ])

    maintenance_request_count = fields.Integer(compute='_compute_maintenance_request_count', string='Open Requests')