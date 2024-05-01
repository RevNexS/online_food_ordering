online_food_ordering

Dir Structure:

templates       -(folder for keeping all html file and css file. Its not for design step only. 
|                 files from here will be pick and added to web(django app))
|_accounts      -(contains authetications pages)
| |_forgot      -(all css,html,img and other file for forgot)
| |_login       -(all css,html,img and other file for login)
| |_signup      -(all css,html,img and other file for signup)
|_dashboard     -(all css,html,img and other file for dashboard)

web                 -(django project folder)
|_accounts          -(accounts app)
|_reaturants        -(resto app)
|_maintainers       -(maintainer app)
|_customers         -(customer app)
|_src               -(django first app)
manage.py           -(entry point for django run script)
