from jinja2 import Template
authN = 'This sample demonstrates a {{ language_and_framework }} {{ app_type }} '\
        'that signs in users to {{ tenant_type }} using {{ msal_link }}.'
call_graph = 'This sample demonstrates a {{ language_and_framework }} {{ app_type }} '\
            'that signs in users and obtains an **Access Token** using {{ msal_link }}.'

def prerender_template(this_template, scenario):
    return this_template.render(details=globals()[scenario]) # fill the details section