# odoo-kickoff
Start your odoo module starting from here

# "Failed building wheel for psycopg2"

`sudo apt-get install libpq-dev`
`pip install psycopg2`

# Create Odoo user for postgresql DB
`sodu su postgres`
 `createuser --createdb --username postgres --no-createrole --no-superuser --pwprompt odoo15`
