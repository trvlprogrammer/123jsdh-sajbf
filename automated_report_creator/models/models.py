# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date,datetime, timedelta

class reportDefinitionInherit(models.Model):
    _inherit = "report.definition"
    
    automatically_generated = fields.Boolean(string="Automatically Generated")
    schedule                = fields.Selection([('15minutes','15 Minutes'),('30minutes','30 Minutes'),
                                 ('1hour','1 Hour'),('6hours','6 Hours'),('1day','1 Day'),('1week','1 Week')
                                 ])
    
    
class reportResultInherit(models.Model):
    _inherit = "report.result"
    
    
    def schedule_15_minutes(self):      
        data = {}  
        data["start_date"]     = str(date.today())
        data["end_date"]       = str(date.today())
        data['schedule']       = "15minutes"  
        self.schedule_report(data)
        
    def schedule_30_minutes(self):
        data = {}
        data["start_date"]     = str(date.today())
        data["end_date"]       = str(date.today())
        data['schedule']       = "30minutes"
        self.schedule_report(data)
        
    def schedule_1_hour(self):
        data = {}
        data["start_date"]     = str(date.today())
        data["end_date"]       = str(date.today())
        data['schedule']       = "1hour"
        self.schedule_report(data)
        
    def schedule_6_hours(self):
        data = {}
        data["start_date"]     = str(date.today())
        data["end_date"]       = str(date.today())
        data['schedule']       = "6hours"
        self.schedule_report(data)
        
    def schedule_1_day(self):
        data = {}
        data["start_date"]     = str(date.today())
        data["end_date"]       = str(date.today())
        data['schedule']       = "1day"
        self.schedule_report(data)
        
    def schedule_1_week(self):
        data = {}
        format                 =  "%Y-%m-%d"
        data["start_date"]     = start_date      = datetime.strptime(str(date.today()), format) - timedelta(days=7)
        data["end_date"]       = str(date.today())
        data['schedule']       = "1week"
        self.schedule_report(data)
        
        
    def schedule_report(self,data):
        reports = self.env["report.definition"].search([("automatically_generated","=",True),("schedule","=",data['schedule'])])
        for report in reports :
            data['report_def_obj'] = report
            self.env['report.result'].generate_report(data)
        
    