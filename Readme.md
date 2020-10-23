## Background 

 an application that can import the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) data and allow his team to add, update, and view squirrel data. 

## Features

1. meet the reuqirements

2. the timer is divided into multiple renderings in order to load all map data without freezing

   > - - - Please note: Your browser will start to freeze if you plot more than 100 points at once. We will assume our client is okay with this plotting issue. Any 100 unique coordinates will do. Any 100 squirrel sightings will do. A simple slice of the database records is sufficient.

3.  Bootstrap4

## Contributor 

### project7 

Jonathan Karten jdk2173；

Muyao Zhang mz2829

## Prerequisites

Python3.7+

Django framweork		

### How to run the code

```
open terminal
cd -uni-_git_project
# you need to import data first in order to see maps and views
python manage.py runserver

```

## 1. data

### 1.1 import

```
python manage.py import_squirrel_data /path/to/file.csv
```

### 1.2 output

```
python manage.py export_squirrel_data /path/to/file.csv
```

## 2. View

open web browser like Chrome


```
### not http://127.0.0.1:8000
http://127.0.0.1:8000/sightings/
```



### 2.1 a map that displays the location of the squirrel sightings

```
http://127.0.0.1:8000/map
```

### 2.2 	all squirrel sightings with links to view each sighting

```
http://127.0.0.1:8000/sightings/
```

### 2.3 update a particular sighting

```
http://127.0.0.1:8000//sightings/<unique-squirrel-id>
```

### 2.4 new sighting

```
http://127.0.0.1:8000/sightings/add
```

### 2.5 stats about the sightings

```
http://127.0.0.1:8000/sightings/stats
```



- 

- - 

- 

- 

- 