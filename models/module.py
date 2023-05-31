from odoo import models, fields


# Define a class named "Something" that inherits from "models.Model"
class Something(models.Model):
    _name = 'module_name.model_name' # Technical name of the module (module_name.model_name)
    _description = 'Description about your model'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text
    description = fields.Text(string='Description')
