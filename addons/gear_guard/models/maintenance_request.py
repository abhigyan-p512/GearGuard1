from odoo import models, fields, api

class MaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _description = 'Maintenance Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Subject', required=True)
    equipment_id = fields.Many2one('equipment.equipment', string='Equipment', required=True)
    request_type = fields.Selection([
        ('corrective', 'Corrective'),
        ('preventive', 'Preventive')
    ], string='Request Type', default='corrective', required=True)
    scheduled_date = fields.Datetime(string='Scheduled Date')
    duration = fields.Float(string='Duration (Hours)')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    stage = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('repaired', 'Repaired'),
        ('scrap', 'Scrap')
    ], string='Stage', default='new', tracking=True)
    team_id = fields.Many2one('maintenance.team', string='Maintenance Team', compute='_compute_team_and_category', store=True)
    category_id = fields.Many2one('equipment.category', string='Category', compute='_compute_team_and_category', store=True)
    overdue = fields.Boolean(compute='_compute_overdue', string='Overdue')

    @api.depends('equipment_id')
    def _compute_team_and_category(self):
        for record in self:
            if record.equipment_id:
                record.team_id = record.equipment_id.maintenance_team_id
                record.category_id = record.equipment_id.category_id
            else:
                record.team_id = False
                record.category_id = False

    @api.depends('scheduled_date', 'stage')
    def _compute_overdue(self):
        for record in self:
            if record.scheduled_date and record.stage in ['new', 'in_progress'] and record.scheduled_date < fields.Datetime.now():
                record.overdue = True
            else:
                record.overdue = False

    def action_assign_to_me(self):
        self.assigned_to = self.env.user
        self.stage = 'in_progress'

    def action_start_repair(self):
        self.stage = 'in_progress'

    def action_repair_done(self):
        self.stage = 'repaired'

    def action_scrap(self):
        self.stage = 'scrap'
        # Log a note that equipment is scrapped
        self.equipment_id.message_post(body='Equipment marked as scrapped due to maintenance request.')