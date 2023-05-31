from odoo import models, fields


# Define a class named "Unit" that inherits from "models.Model"
class Unit(models.Model):
    _name = 'university.unit' # Technical name of the module (module_name.model_name)
    _description = 'A self-contained unit of study or instruction within a particular subject or discipline'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text
    description = fields.Text(string='Description')

    # Define a Many-to-One relationship field named "section_id" with 'university.section' model
    section_id = fields.Many2one('university.section', string='Section')


# Define a class named "Section" that inherits from "models.Model"
class Section(models.Model):
    _name = 'university.section'
    _description = 'A subdivision or smaller group within a larger course'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text, which is editable
    description = fields.Text(string='Description', readonly=False)

    # Define a One-to-Many relationship field named "unit_ids" with 'university.unit' model
    unit_ids = fields.One2many('university.unit', 'section_id', string='Units')

    # Define a Many-to-One relationship field named "level_id" with 'university.level' model
    level_id = fields.Many2one('university.level', string='Level')


# Define a class named "Level" that inherits from "models.Model"
class Level(models.Model):
    _name = 'university.level'
    _description = 'The stage or degree of advancement in an academic program.'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text, which is editable
    description = fields.Text(string='Description', readonly=False)

    # Define a One-to-Many relationship field named "unit_ids" with 'university.unit' model
    section_ids = fields.One2many('university.section', 'level_id', string='Sections')

    # Define a Many-to-One relationship field named "level_id" with 'university.level' model
    cycle_id = fields.Many2one('university.cycle', string='Cycle')


# Define a class named "Cycle" that inherits from "models.Model"
class Cycle(models.Model):
    _name = 'university.cycle'
    _description = 'The regular sequence of academic activities throughout the year, typically divided into semesters ' \
                   'or quarters.'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text, which is editable
    description = fields.Text(string='Description', readonly=False)

    # Define a One-to-Many relationship field named "level_ids" with 'university.level' model
    level_ids = fields.One2many('university.level', 'cycle_id', string='Levels')

    # Define a Many-to-One relationship field named "registration_id" with 'university.registration' model
    registration_id = fields.Many2one('university.registration', string='Registration')


# Define a class named "Registration" that inherits from "models.Model"
class Registration(models.Model):
    _name = 'university.registration'
    _description = 'the process by which students enroll or sign up for classes and academic activities for a ' \
                   'particular term or semester'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text, which is editable
    description = fields.Text(string='Description', readonly=False)

    # Define a field named "start_date" of type Date
    start_date = fields.Date('Start Date', help='Date')

    # Define a field named "end_date" of type Date
    end_date = fields.Date('End Date', help='Date')

    # Define a One-to-Many relationship field named "cycle_ids" with 'university.cycle' model
    cycle_ids = fields.One2many('university.cycle', 'registration_id', string='Cycles')

    # Define a Many-to-One relationship field named "year_id" with 'university.year' model
    year_id = fields.Many2one('university.year', string='Year')

    # Define a One-to-Many relationship field named "claim_ids" with 'university.claim' model
    claim_ids = fields.One2many('university.claim', 'registration_id', string='Claims')


# Define a class named "Year" that inherits from "models.Model"
class Year(models.Model):
    _name = 'university.year'
    _description = 'A period of time during which academic activities take place'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text, which is editable
    description = fields.Text(string='Description', readonly=False)

    # Define a field named "start_date" of type Date
    start_date = fields.Date('Start Date', help='Date')

    # Define a field named "end_date" of type Date
    end_date = fields.Date('End Date', help='Date')

    # Define a One-to-Many relationship field named "registration_ids" with 'university.year' model
    registration_ids = fields.One2many('university.registration', 'year_id', string='Registrations')

    # Define a One-to-Many relationship field named "session_ids" with 'university.session' model
    session_ids = fields.One2many('university.session', 'year_id', string='Sessions')


# Define a class named "Session" that inherits from "models.Model"
class Session(models.Model):
    _name = 'university.session'
    _description = 'A defined period of academic instruction or activity within an academic year.'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text, which is editable
    description = fields.Text(string='Description', readonly=False)

    # Define a field named "start_date" of type Date
    start_date = fields.Date('Start Date', help='Date')

    # Define a field named "end_date" of type Date
    end_date = fields.Date('End Date', help='Date')

    # Define a One-to-Many relationship field named "registration_ids" with 'university.year' model
    registration_ids = fields.One2many('university.registration', 'year_id', string='Registrations')

    # Define a Many-to-One relationship field named "year_id" with 'university.session' model
    year_id = fields.Many2one('university.session', string='Year')


# Define a class named "Claim" that inherits from "models.Model"
class Claim(models.Model):
    _name = 'university.claim'
    _description = 'A university claim.'

    # Define a field named "name" of type Char with a required constraint
    name = fields.Char(string='Name', required=True)

    # Define a field named "code" of type Char with a default value of '001'
    code = fields.Char(string='Code', default='001')

    # Define a field named "description" of type Text, which is editable
    description = fields.Text(string='Description', readonly=False)

    # Define a field named "start_date" of type Date
    start_date = fields.Date('Start Date', help='Date')

    # Define a field named "end_date" of type Date
    end_date = fields.Date('End Date', help='Date')

    # Define a Many-to-One relationship field named "registration_id" with 'university.registration' model
    registration_id = fields.Many2one('university.registration', string='Registration')