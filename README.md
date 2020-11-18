## Diorama
 A personal gallery application that displays photos for viewing, based on category
### Author
#### Virginia Wairimu

## User Requirements

1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3. Search for different categories of photos.
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Features

+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Bootstrap image model and copy link button.
+ [x] Filter images based on location.
+ [x] search functionality based on image category.


## Setup

### Requirements
* Python3

### Cloning the repository
```bash
git clone https://github.com/Virginia202/IP1-Gallery.git
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
Create a .env file and add the following configutions to it
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running Tests
```bash
python manage.py test 
```

### Running the server 
```bash
python manage.py runserver
```

### Deploying to heroku

Set the configuration to production mode



## Technology used

* python3.6
* Django
* Heroku CLI


