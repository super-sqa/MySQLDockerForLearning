# MySQLDockerForLearning
### Description
Python script to run a mysql container that as some sample data. 
The script will start a container with existing folders as volumes. The existing folders have information for one database and two tables.
Database/Schema: countries
Tables:
  capital_city
  country_info
  
### Dependency
1. You must have docker installed and running on your local machine.
2. You must install Python library for the Docker Engine API
    * You can use pip to install the library.
    * You find more informtion [here](https://github.com/docker/docker-py)
    * Command to install (This is the version the script is tested with. Both Python 2 and Python 3 are ok)
    ```
    pip install docker==3.1.0
    ```
    
### Usage
Simply run the script with python
```
$ python run_mysql_docker_container.py
```
or
```
$ python run_mysql_docker_container.py --print_docker_logs=True
```
