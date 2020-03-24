# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

import requests, xmltodict, json
from datetime import datetime
import pytz
import time

class PropertyWayReferenceSale(models.Model):
    _name = 'property.way.reference.sale'
    _description = 'Property Way Reference Sale'
    
    property_way_id = fields.Many2one(
        comodel_name='property.way',
        string='Property Way Id'
    )
    property_transaction_type_id = fields.Many2one(
        comodel_name='property.transaction.type',
        string='Property Transaction Type Id'
    )
    property_home_type_id = fields.Many2one(
        comodel_name='property.home.type',
        string='Property Home Type Id'
    )
    maximum_properties = fields.Integer(
        string='Maximum Properties'
    )
    radius = fields.Integer(
        string='Radius'
    )
    maximum_price = fields.Float(
        string='Maximum Price'
    )
    minimum_price = fields.Float(
        string='Minimum Price'
    )
    maximum_surface_area = fields.Float(
        string='Maximum Surface Area'
    )
    minimum_surface_area = fields.Float(
        string='Minimum Surface Area'
    )                        
    full = fields.Boolean(
        string='Full'
    )
    date_last_check = fields.Date(
        string='Date Last Check'
    )    
    source = fields.Selection(
        selection=[
            ('bbva','BBVA')                                      
        ],
        string='Source',
        default='bbva'
    )    
    
    @api.multi    
    def bbva_generate_tsec(self):
        tsec = False
        url = 'https://www.bbva.es/ASO/TechArchitecture/grantingTicketsOauth/V01/'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic SU1NQjAwMTpTajhCbGpRYw=='
        }
        data_obj = {
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, headers=headers, data=data_obj)
        if response.status_code==200:        
            response_json = json.loads(response.text)
            if 'access_token' in response_json:
                tsec = str(response_json['access_token'])
            
        return tsec    