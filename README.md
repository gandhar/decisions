**Running vagrant with wordpress blog**


install pre-requisites

`sudo apt-get install ansible virtualbox vagrant git`


clone this repository

`git clone https://github.com/gandhar/decisions.git`

`cd decisions`


start the vm

`vagrant up`

once the vm is up, a demo site should be running on

[http://localhost:8081/wordpress/](http://localhost:8081/wordpress/)


**Deploy post to running blog**

install pre-requisite 
[xmlrpc](xmlrpc.readthedocs.io/en/latest/overview.html#installation)

`sudo easy_install python-wordpress-xmlrpc`


deploy post from text file

`python new_post.py Random_Post_1.txt`
