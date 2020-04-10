# Summary
Build RSS feed web application that users can register, login and create post


# Tech used
- Django Rest Framework == 3.11.0
- Python == 3.7
- React == 16.13.0
- React-Redux == 7.2.0
- PostgreSQL

# How to start locally
## backend
1. create local_settings.py and have secret key and db setup
  ```python
  # webapp/local_settings.py
    local_secret_key = 'secret_key'
    local_db = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name of db',
        'USER': ''username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
        }
    }
  ```
2. create virtualenv and install requirements.txt
```python
# in terminal
>> virtualenv venv
>> venv/Scripts/activate.bat
# move to the directory which contains requirements.txt
>> pip install -r requirements.txt
```
3. run python script
```python
# in the directory where manage.py exists
# create daba connection
python manage.py makemigrations
python manage.py migrate
# create superuser
python manage.py createsuperuser
# run server
python manage.py runserver
```
   
## frontend
1. move directory to apps/frontend/
2. install npm packages
   ```javascript
   npm i
   ```
3. run frontend
   ```javascript
   npm run dev
   ```

## trouble shooting
1. Since this app is still under development stage, debug mode is on.
   - It means you can see the error message on the Internet browswer
2. If you see the ProgrammingError relation  **board_board**  does not exist,
   - run this python script
     ```python
     python manage.py makemigrations board # it will create table in the db
     python manage.py migrate board # it will apply migrations
     ```
