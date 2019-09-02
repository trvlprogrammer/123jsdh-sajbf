# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from reportlab.lib.validators import Auto
from odoo.exceptions import Warning

class automated_task(models.Model):
    _name = 'automated.task'
 
    name            = fields.Char(string = 'Title')
    project_id      = fields.Many2one('project.project', string = 'Project')
    start_date      = fields.Date(default = datetime.now().date(),string = 'Start Date')
    end_date        = fields.Date(default = datetime.now().date(),string='End Date')
    assigned_to     = fields.Many2many('res.users','automated_task_users_rel','automated_task_id','user_id', string='Assigned To')
    type            = fields.Selection([('day','Day'),('weekdays','Weekdays'),('week','Week'),('month','Month')])
    daily           = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])
    description     = fields.Html(string = 'Description')
    monday          = fields.Boolean(string = 'Monday')
    tuesday         = fields.Boolean(string = 'Tuesday')
    wednesday       = fields.Boolean(string = 'Wednesday')
    thursday        = fields.Boolean(string = 'Thursday')
    friday          = fields.Boolean(string = 'Friday')
    saturday        = fields.Boolean(string = 'Saturday')
    sunday          = fields.Boolean(string = 'Sunday')
    project_task    = fields.One2many('project.task','automated_task', string = 'Project Task')
    create_date_on  = fields.Char(compute='_compute_create_date_on', string = 'Create Date On', store=True) 
    summary         = fields.Char(compute='_compute_summary', string = 'Summary')
     
     
    @api.one 
    @api.depends('type','start_date','end_date','daily',
                 'monday','tuesday','wednesday', 'thursday', 
                 'friday','saturday', 'sunday')
    def _compute_create_date_on(self):                 
        
        format              =  "%Y-%m-%d"
        create_dates        = []                        
        data                = {}
        data['create_date'] = datetime.strptime(str(self.start_date), format).date()
        data['end_date']    = datetime.strptime(str(self.end_date), format).date()
        
        if self.type == 'day' :                        
            data['daily']       = int(self.daily)
            create_dates = self.count_daily(data)
            
        elif self.type == 'month' :                        
            create_dates = self.count_monthly(data)
            
        elif self.type == 'weekdays' :
            create_dates = self.count_weekdays(data)
                     
        elif self.type == 'week' :
            data['monday']      = self.monday
            data['tuesday']     = self.tuesday
            data['wednesday']   = self.wednesday
            data['thursday']    = self.thursday
            data['friday']      = self.friday
            data['saturday']    = self.saturday
            data['sunday']      = self.sunday
            
            create_dates = self.count_weekly(data)
                      
        self.create_date_on = create_dates
        
        
        
    def count_daily(self,data):
        
        create_date     = data['create_date']
        end_date        = data['end_date']
        iteration       = end_date - create_date 
        iteration       = iteration.days
        create_dates    = [] 
        i               = 0
        
        if data['daily'] :                
            while i <= iteration :
    #             if i == 0 :
    #                 create_dates.append(str(create_date))
    #                 
    #             else : 
                create_dates.append(str(create_date))
                create_date = create_date + timedelta(days=int(data['daily']))                                
    #             create_date = next_create_date
                     
                i += int(data['daily'])
        
        return create_dates
    
    def count_monthly(self,data):
        
        create_date     = data['create_date']
        end_date        = data['end_date']
        iteration       = end_date - create_date 
        iteration       = iteration.days
        create_dates    = [] 
        i               = 0
        
                         
        while i <= iteration :
            
#             if i == 0 :
#                 create_dates.append(str(create_date))
#                 
#             else :                               
            create_dates.append(str(create_date))
            create_date = create_date + timedelta(days=int(30))                                    
#             create_date = next_create_date
                     
            i += int(30)
    
        return create_dates
    
    
    
    def count_weekdays(self,data):
        
        create_date     = data['create_date']
        end_date        = data['end_date']
        iteration       = end_date - create_date 
        iteration       = iteration.days
        create_dates    = [] 
        i               = 0
        date_today      = datetime.now().date()
        today_dayName   = date_today.strftime("%A").lower()
        
        
#         if date_today >= create_date and date_today <= end_date :
#         if create_date != 'saturday' and create_date != 'sunday':
#             create_dates.append(str(create_date))
                             
        while i <= iteration :
            
            create_date_name = create_date.strftime("%A").lower()
            
            if create_date_name == 'friday' :
                create_dates.append(str(create_date))
                next_create_date = create_date + timedelta(days=int(3))                                    
                create_date = next_create_date
                i += int(3)
                
            elif create_date_name != 'saturday' and create_date_name != 'sunday' and create_date_name != 'friday' :                
                create_dates.append(str(create_date))                
                next_create_date = create_date + timedelta(days=int(1))                    
                create_date = next_create_date
                i += int(1)
                
            elif create_date_name == 'saturday':                                                
                create_date = create_date + timedelta(days=int(2))                                    
                i += int(2)
            
            elif create_date_name == 'sunday':                                                
                create_date = create_date + timedelta(days=int(1))                                    
                i += int(1)
            
        return create_dates     
                    
                                                    
    
    def count_weekly(self,data):
        
        create_date     = data['create_date']
        end_date        = data['end_date']
        iteration       = end_date - create_date 
        iteration       = iteration.days
        create_dates    = [] 
        i               = 0
        
        
        while i <= iteration :
            
            create_date_name = create_date.strftime("%A").lower()
            
            if create_date_name == 'monday' and data['monday'] == True :
                create_dates.append(str(create_date))
                next_create_date = create_date + timedelta(days=int(1))                                    
                create_date = next_create_date
                
            elif create_date_name == 'tuesday' and data['tuesday'] == True :
                create_dates.append(str(create_date))
                next_create_date = create_date + timedelta(days=int(1))                                    
                create_date = next_create_date
                
            elif create_date_name == 'wednesday' and data['wednesday'] == True :
                create_dates.append(str(create_date))
                create_date = create_date + timedelta(days=int(1))                                    
                
                
            elif create_date_name == 'thursday' and data['thursday'] == True :
                create_dates.append(str(create_date))
                create_date = create_date + timedelta(days=int(1))                                    
                
                
            elif create_date_name == 'friday' and data['friday'] == True :
                create_dates.append(str(create_date))
                create_date = create_date + timedelta(days=int(1))                                    
                
                
            elif create_date_name == 'saturday' and data['saturday'] == True :
                create_dates.append(str(create_date))
                create_date = create_date + timedelta(days=int(1))                                    
                
                
            elif create_date_name == 'sunday' and data['sunday'] == True :
                create_dates.append(str(create_date))
                create_date = create_date + timedelta(days=int(1))                                                    
            
            
            else :
                create_date = create_date + timedelta(days=int(1))
            
                                                    
            i += int(1)
        
        return create_dates

        
    @api.depends('type','start_date','end_date','daily',
                 'monday','tuesday','wednesday', 'thursday', 
                 'friday','saturday', 'sunday')        
    def _compute_summary(self):
        day = ' day'                     
        if self.type == 'day':
            if self.daily != '1' :
                day = ' days'  
            self.summary = self.name + ' will be created every ' + str(self.daily) + day
        
        elif self.type == 'month' :
            self.summary = self.name + ' will be created every month'
        
        elif self.type == 'weekdays' :
            self.summary = self.name + ' will be created every weekdays'
        
        elif self.type == 'week' :
                day = ''
                if self.monday == True :
                    day += ',Monday '
                if self.tuesday == True :
                    day += ',Tuesday '
                if self.wednesday == True :
                    day += ',Wednesday '
                if self.thursday == True :
                    day += ',Thursday '
                if self.friday == True :
                    day += ',Friday '
                if self.saturday == True :
                    day += ',Saturday '
                if self.sunday == True :
                    day += ',Sunday '
                    
                self.summary = self.name + ' will be created every ' + day
                     
    
    
    @api.model 
    def create(self,vals):
        format      =  "%Y-%m-%d"
        res         = super(automated_task,self).create(vals)
        start_date  = datetime.strptime(str(vals['start_date']),format).date()
        end_date    = datetime.strptime(str(vals['end_date']),format).date()
        date_today  = datetime.now().date()
        
        
        data                    = {}
        data['name']            = vals['name']
        data['project_id']      = vals['project_id']
        data['description']     = vals['description']
        data['automated_task']  = res.id
        data['created_on']      = datetime.now().date()
        
        
        if datetime.strptime(str(vals['end_date']), format).date() < datetime.strptime(str(vals['start_date']), format).date():
            raise Warning ('Error! End date should be greater than start date')
        
        if date_today >= start_date and date_today <= end_date :
            
            if vals['type'] == 'day' or vals['type'] == 'month' :            
                for user_id in vals['assigned_to'][0][2] :
                    data['user_id'] = user_id                
                    data['message_follower_ids'] = False
                    self.env['project.task'].create(data)
            
            elif vals['type'] == 'weekdays' :                
                today_dayName   =  date_today.strftime("%A").lower()             
                if today_dayName != 'saturday' and today_dayName != 'sunday': 
                    for user_id in vals['assigned_to'][0][2] :
                        data['user_id'] = user_id                
                        data['message_follower_ids'] = False
                        self.env['project.task'].create(data)
                        
        
        return res
    
    
    
    @api.multi 
    def write(self,vals):
        
        format =  "%Y-%m-%d"
        if vals.has_key('start_date') and vals.has_key('end_date') :
            if datetime.strptime(str(vals['end_date']), format).date() < datetime.strptime(str(vals['start_date']), format).date():
                raise Warning ('Error! End date should be greater than start date')
        elif vals.has_key('start_date') :
            if datetime.strptime(str(self.end_date), format).date() < datetime.strptime(str(vals['start_date']), format).date():
                raise Warning ('Error! End date should be greater than start date')
        elif vals.has_key('end_date') :
            if datetime.strptime(str(vals['end_date']), format).date() < datetime.strptime(str(self.start_date), format).date():
                raise Warning ('Error! End date should be greater than start date')
                  
        return super(automated_task,self).write(vals)
    
    
    @api.multi
    def scheduler_automated_task(self,context=None):
        automated_task_ids = self.env['automated.task'].search([])
        date_today = datetime.now().date()
        for id in automated_task_ids :
            if not self.env['project.task'].search([('automated_task','=',id.id),('created_on','=',str(date_today))]) and str(date_today) in eval(id.create_date_on): 
                
                data                    = {}
                data['name']            = id.name 
                data['project_id']      = id.project_id.id  
                data['description']     = id.description
                data['automated_task']  = id.id
                data['created_on']      = datetime.now().date() 
                
                for user_id in id.assigned_to :
                    data['user_id'] = user_id.id                
                    data['message_follower_ids'] = False
                    self.env['project.task'].create(data)
            else :
                print 'task already exists'
        
class ProjectTask_inherit(models.Model):
    _inherit = 'project.task'
    
    automated_task      = fields.Many2one('automated.task', string = "Automated Task")
    created_on          = fields.Date(string='Created On') 
    
#     
#     @api.model 
#     def create(self,vals):
#         print 'c'
    
