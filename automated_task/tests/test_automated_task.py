from odoo.tests import common
 
 
class TestAutomatedTask(common.TransactionCase):
    
    def test_create_automated_task(self):
        
        data = {}
        data['name']            = 'daily'
        data['type']            = 'day'        
        data['project_id']      = 1  
        data['description']     = 'test automated task'
        data['start_date']      = '2019-7-22'
        data['end_date']        = '2019-7-31'
        data['assigned_to']     = [[6, False, [1, 6]]]
        data['sunday']          = True
        data['monday']          = True
        data['daily']           = '2'
        
        
        
        automatedtask1 = self.env['automated.task'].create(data)
        
        
        data['name']            = 'weekdays'
        data['type']            = 'weekdays'
        automatedtask2 = self.env['automated.task'].create(data)
        
        
        data['name']            = 'weekly'          
        data['type']            = 'week'
        automatedtask3 = self.env['automated.task'].create(data)
        
        
        data['name']            = 'monthly'
        data['type']            = 'month'
        data['end_date']        = '2019-12-28'
        automatedtask4 = self.env['automated.task'].create(data)
        
        
        self.assertEqual(automatedtask1.name, 'daily')
        self.assertEqual(automatedtask2.name, 'weekdays')
        self.assertEqual(automatedtask3.name, 'weekly')
        self.assertEqual(automatedtask4.name, 'monthly')
        
        
#         daily
        for id in self.env['project.task'].search([('automated_task','=',automatedtask1.id)]):
            self.assertEqual(automatedtask1.id,id.automated_task.id)
            self.assertEqual(automatedtask1.name, id.name)
            self.assertEqual("['2019-07-22', '2019-07-24', '2019-07-26', '2019-07-28', '2019-07-30']", str(automatedtask1.create_date_on))
        
#         weekdays
        for id in self.env['project.task'].search([('automated_task','=',automatedtask3.id)]):
            self.assertEqual(automatedtask3.id,id.automated_task.id)
            self.assertEqual(automatedtask3.name, id.name)
            self.assertEqual(str(['2019-7-22','2019-7-23','2019-7-24','2019-7-25','2019-7-26','2019-7-29','2019-7-30','2019-7-31']), automatedtask2.create_date_on)                
        
#         weekly
        for id in self.env['project.task'].search([('automated_task','=',automatedtask3.id)]):
            self.assertEqual(automatedtask3.id,id.automated_task.id)
            self.assertEqual(automatedtask3.name, id.name)
            self.assertEqual(str(['2019-7-22','2019-7-29']), automatedtask3.create_date_on)
            
        for id in self.env['project.task'].search([('automated_task','=',automatedtask4.id)]):
            self.assertEqual(automatedtask4.id,id.automated_task.id)
            self.assertEqual(automatedtask4.name, id.name)
            print 'create monthly'
            
            print automatedtask4.create_date_on
        
#         self.assertEqual(automatedtask3.id, self.env['project.task'].search([('automated_task','=',automatedtask3.id)]))
#         self.assertEqual(automatedtask4.id, self.env['project.task'].search([('automated_task','=',automatedtask4.id)]))
        
        
#         self.assertEqual(automatedtask1.name, self.env['project.task'].browse(automatedtask1.id).name)
#         self.assertEqual(automatedtask3.name, self.env['project.task'].browse(automatedtask3.id).name)
#         self.assertEqual(automatedtask4.name, self.env['project.task'].browse(automatedtask4.id).name)
        
        
        
        self.env['automated.task'].scheduler_automated_task(context=None)
        
        
        
        print 'test success'
        
# "['2019-7-22', '2019-7-24', '2019-7-26', '2019-7-28', '2019-07-30']" != "['2019-07-22', '2019-07-24', '2019-07-26', '2019-07-28', '2019-07-30']"        
 
        