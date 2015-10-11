### Creating a new virutal env

* first install or upgrade virtualenv
  - `$ sudo pip install --upgrade virtualenv`
* create a new virtual env for python3
  - `$ virtualenv -p python3 tdd-env`
* source it
  - `$ source tdd-env/bin/activate`
* install requirements 
  - `$ cd superlists`
  - `$ pip3 install -r requirements.txt`


###  running unit tests
$ python3 manage.py test lists

### running functional tests
$ python3 manage.py test functional_tests

