virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
npm install -g bower
npm install
bower install
python manage.py migrate
python manage.py runserver
