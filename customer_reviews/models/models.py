# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning

class partnerInherit(models.Model):
    
    _inherit = 'res.partner'
    
    
    number_of_rates = fields.Integer(compute="_compute_rates_number",string= "Number of rates", store=True)
    average_ratings = fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], compute="_compute_ratings", store=True)
    customer_reviews= fields.One2many('customer.reviews', 'vendor_id')
    
    
    
#     using api depends and compute to get number of rates automatically
    @api.one
    @api.depends('customer_reviews.vendor_id')
    def _compute_rates_number(self):
        customer_ids = self.env['customer.reviews'].search([('vendor_id','=',self.id)])
        self.number_of_rates = len(customer_ids)
    
    
    
#     using api depend and compute to get average ratings automatically
    @api.one    
    @api.depends('customer_reviews.ratings','customer_reviews.vendor_id')
    def _compute_ratings(self):
        reviews = self.env['customer.reviews'].search([('vendor_id','=',self.id)])
        ratings = 0
        for review in reviews :
            if review.ratings != '0':
                ratings = ratings + int(review.ratings)
        if ratings != 0 :
            print len(reviews)
            ratings = ratings/len(reviews)
        self.average_ratings = str(ratings)
        
        
        
#     return view to customer reviews, this function called by button    
    @api.multi
    def open_reviews(self):
        
        return {
            'name': 'Customer Reviews',
            'view_type': 'form',
            'view_mode': 'tree,form',            
            'res_model': 'customer.reviews',
            'domain': [('vendor_id','=',self.id)],
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
    


# models for customer reviews    
class customer_review(models.Model):
    
    _name = "customer.reviews"
    
    customer_id     = fields.Many2one('res.partner', string="Customer")
    vendor_id       = fields.Many2one('res.partner', string="Vendor")
    message         = fields.Text(string = 'Message')
    ratings         = fields.Selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], string="Ratings")
    
    
#     overide create function to check if the user is customer or not
#     and to set value of customer id
    @api.model 
    def create(self,vals):        
        customer_id = self.env['res.users'].browse(self._uid).partner_id
        
        if customer_id.customer == False :
            raise Warning('Only Customer Can Make Reviews')    
            
        vals['customer_id'] = customer_id.id            
        return super(customer_review,self).create(vals)
 
 
#     no one can edit the comments except the customer it self
    @api.multi
    def write(self,vals):
        customer_id = self.env['res.users'].browse(self._uid).partner_id.id
        if customer_id != self.customer_id.id :
            raise Warning('You Can Not Edit Other Review')
        
        return super(customer_review,self).write(vals)
            
    