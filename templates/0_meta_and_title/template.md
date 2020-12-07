{% raw %}---
page_type: sample
languages:{% for language in languages %}
  - {{ language }}{% endfor %}
products:
  - azure
  - azure-active-directory
  - microsoft-identity-platform
name: Enable your {{ language_and_framework }} {{ app_type }} to sign in users to {{tenant_type }} with the Microsoft identity platform
urlFragment: {{ url_fragment }}
description: "This sample demonstrates a {{ language_and_framework }} {{ app_type }} that signs in users to {{tenant_type }} with the Microsoft identity platform"
---
# Enable your {{ language_and_framework }} {{ app_type }} to sign in users to {{ tenant_type }} tenant with the Microsoft identity platform{% endraw %}