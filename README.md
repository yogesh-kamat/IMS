# sales-and-inventory-management-system (using django)

## DBMS Project  
##### To setup virtual environment for the project and to install dependencies type : pipenv install
##### After that to start the WebApp type : python manage.py runserver
##### For authentication :
###### Superuser : 'yogesh' | Password : 'password'
###### Sample user for testing : username - 'sampleuser' | password - 'password@123'


### SQL

1. Initial db and user creation
```
create database sims;
create user simsadmin with encrypted password 'password';
grant all privileges on database sims to simsadmin;
```

### Total Migrations
```
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
home
 [X] 0001_initial
sessions
 [X] 0001_initial
```

### SQL to create view and demonstrate joins
```
create view home_SupplierProductCostView as
select b.id, b.sname, sum(a.quantity*a.selling_price) as price
from home_inventory as a right join home_supplier as b
on a.supplier_id = b.id
group by a.supplier_id,b.id
order by b.id;

select * from home_SupplierProductCostView;
```

## Instructions for hosting to heroku
Install following  
1. django-heroku
2. gunicorn

After installing Create Procfile in project root with following line:
```
web: gunicorn project_name.wsgi
web: python project/manage.py runserver 0.0.0.0:$PORT
```


Add following lines in settings.py  
```
import django_heroku
```
Activate Django-Heroku.
```
django_heroku.settings(locals())
```
Then set DEBUG = False 

Finally Run following commands in projects root directory  
```
heroku login
heroku create app-name
git add .
git commit -m "msg"
git push heroku master
heroku ps:scale web=1
heroku run bash
cd SIMS
python3 manage.py migrate
python3 manage.py loaddata supplier
python3 manage.py loaddata inventory
python3 manage.py createsuperuser
heroku open
```



