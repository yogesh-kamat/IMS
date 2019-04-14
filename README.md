# sales-and-inventory-management (using django)

### To setup virtual environment for the project and to install dependencies type : pipenv install
### Then to run type : python manage.py runserver
### For authentication :
#### Superuser : yogesh Password : password
#### sample users for testing : username - sampleuser password - password@123


### SQL

1. Initial db and user creation
```
create database sims;
create user simsadmin with encrypted password 'password';
grant all privileges on database sims to simsadmin;
```

2. Initial Django migrations to create tables

#### App : Admin 0001
```
BEGIN;
--
-- Create model LogEntry
--
CREATE TABLE "django_admin_log" ("id" serial NOT NULL PRIMARY KEY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL);
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
COMMIT;
```
#### App : auth 0001
```
BEGIN;
--
-- Create model Permission
--
CREATE TABLE "auth_permission" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL);
--
-- Create model Group
--
CREATE TABLE "auth_group" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" serial NOT NULL PRIMARY KEY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL);
--
-- Create model User
--
CREATE TABLE "auth_user" ("id" serial NOT NULL PRIMARY KEY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL);
CREATE TABLE "auth_user_groups" ("id" serial NOT NULL PRIMARY KEY, "user_id" integer NOT NULL, "group_id" integer NOT NULL);
CREATE TABLE "auth_user_user_permissions" ("id" serial NOT NULL PRIMARY KEY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL);
ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops);
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_username_6821ab7c_like" ON "auth_user" ("username" varchar_pattern_ops);
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
COMMIT;
```

#### App : sessions 0001
```
BEGIN;
--
-- Create model Session
--
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL);
CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops);
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
COMMIT;
```

#### App : contenttypes 0001
```
BEGIN;
--
-- Create model ContentType
--
CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
--
-- Alter unique_together for contenttype (1 constraint(s))
--
ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model");
COMMIT;
```
#### App : home 0001
```
BEGIN;
--
-- Create model Inventory
--
CREATE TABLE "home_inventory" ("id" serial NOT NULL PRIMARY KEY, "pname" varchar(255) NOT NULL, "quantity" integer NOT NULL CHECK ("quantity" >= 0), "measurement" varchar(255) NOT NULL, "orginal_price" integer NOT NULL CHECK ("orginal_price" >= 0), "profit" integer NOT NULL CHECK ("profit" >= 0), "selling_price" integer NOT NULL CHECK ("selling_price" >= 0));
--
-- Create model Supplier
--
CREATE TABLE "home_supplier" ("id" serial NOT NULL PRIMARY KEY, "sname" varchar(255) NOT NULL UNIQUE, "contact" varchar(255) NOT NULL, "address" text NOT NULL);
--
-- Create model Transaction
--
CREATE TABLE "home_transaction" ("id" serial NOT NULL PRIMARY KEY, "cust_name" varchar(255) NOT NULL, "quantity_r" integer NOT NULL CHECK ("quantity_r" >= 0), "success" boolean NOT NULL, "pid_id" integer NOT NULL, "uid_id" integer NOT NULL);
--
-- Add field supplier to inventory
--
ALTER TABLE "home_inventory" ADD COLUMN "supplier_id" integer NOT NULL;
CREATE INDEX "home_supplier_sname_ee45ae34_like" ON "home_supplier" ("sname" varchar_pattern_ops);
ALTER TABLE "home_transaction" ADD CONSTRAINT "home_transaction_pid_id_b0426fed_fk_home_inventory_id" FOREIGN KEY ("pid_id") REFERENCES "home_inventory" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "home_transaction" ADD CONSTRAINT "home_transaction_uid_id_d9017f85_fk_auth_user_id" FOREIGN KEY ("uid_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "home_transaction_pid_id_b0426fed" ON "home_transaction" ("pid_id");
CREATE INDEX "home_transaction_uid_id_d9017f85" ON "home_transaction" ("uid_id");
CREATE INDEX "home_inventory_supplier_id_b03dcb02" ON "home_inventory" ("supplier_id");
ALTER TABLE "home_inventory" ADD CONSTRAINT "home_inventory_supplier_id_b03dcb02_fk_home_supplier_id" FOREIGN KEY ("supplier_id") REFERENCES "home_supplier" ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;
```

### Total Migrations : 
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

### Instructions for hosting to heroku : 
Install following : 
1. django-heroku
2. gunicorn

After installing Create Procfile in project root with following line:
web: gunicorn project_name.wsgi
web: python project/manage.py runserver 0.0.0.0:$PORT


Add following lines in settings.py :
```
import django_heroku
```
Activate Django-Heroku.
```
django_heroku.settings(locals())
```
Then set DEBUG = False 

#### Finally Run following commands in projects root directory : 
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



