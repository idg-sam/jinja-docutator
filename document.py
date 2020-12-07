from jinja2 import Environment, select_autoescape, FileSystemLoader, Template
import importlib

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=False, 
    )

scenario = 'authN' # get it from config
languages = ['python', 'flask'] # get this from config
python_msal_link = 'the [Microsoft Authentication Library (MSAL) for Python](https://github.com/AzureAD/microsoft-authentication-library-for-python)'
tenant_type = 'your Azure Active Directory tenant' # or 'any Azure Active Directory tenant' or 'your Azure Active Directory B2C tenant'
survey_link = 'https://example.com'

# your apps:
app_type = [].append('web app')
language_and_framework=[].append('Python Flask')

#######
parts = ['meta_and_title','overview']

for i,part in enumerate(parts):
    template = importlib.import_module(f'templates.{part}.template')
    parts[i] = template.prerender_template(env.get_template(f'{part}/template.md'), scenario)


template_dict = dict(
    app_type=app_type,
    msal_link=python_msal_link,
    languages=languages,
    language_and_framework=language_and_framework,
    tenant_type=tenant_type,
)

base = env.get_template('base.md')
### add parts ###
base = Template(base.render(parts=parts))
### render in full ###
print(base.render(**template_dict))