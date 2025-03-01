<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

Project Details
The project is structured with specific requirements in mind:

The codebase is compatible with Python 3.8.5 and is executed on Ubuntu 20.04 LTS.
All code files have the shebang line #!/usr/bin/python3.
Code follows the PEP8 style guidelines for consistent formatting.
All code files are executable.
Modules, classes, and functions include documentation explaining their purpose.
Unit Testing
Testing is a crucial aspect of the project:

Unit tests are organized in the "tests" folder and are written using the unittest module.
Test files have the ".py" extension and begin with "test_".
Tests are designed to ensure code correctness and robustness.
When necessary, tests can be skipped using the skipIf feature of the unittest module.
SQL Scripts
The project includes SQL scripts for database interaction:

SQL files are executed on MySQL 8.0 running on Ubuntu 20.04 LTS.
SQLAlchemy version 1.4.x is used for database operations.
SQL queries are documented with comments for clarity.

Key Learning Objectives
As you work on this project, you will have the opportunity to learn and apply various important concepts and skills, including:

Implementing unit testing in a large-scale project to ensure code reliability.
Working with *args and **kwargs in Python for flexible function parameter handling.
Handling named arguments in functions effectively.
Creating and configuring a MySQL database for data storage.
Managing user accounts and granting privileges in MySQL.
Understanding Object-Relational Mapping (ORM) principles.
Mapping Python classes to MySQL database tables.
Handling two different storage engines (file and database) using a single codebase.
Using environment variables for configuration management.

Project Objectives:

1. Environment Variable Usage
An essential aspect of modern software development is configuration management. This project introduces the use of environment variables to control various aspects of the application, such as choosing between different storage engines and configuring database connections. Participants learn how to handle sensitive data securely and dynamically adjust application settings.

2. Learning Object-Relational Mapping (ORM)
The project introduces Object-Relational Mapping (ORM) principles, which facilitate the mapping of Python classes to database tables. By doing so, participants gain valuable experience in bridging the gap between object-oriented programming and relational databases, a crucial skill for any backend developer.

3. Comprehensive Unit Testing
Robust software relies on rigorous testing. This project emphasizes the importance of unit testing using the unittest module. Participants must ensure that the codebase passes unit tests flawlessly. This experience instills a culture of testing and quality assurance in software development.

4. SQL and Database Management
Understanding database management is paramount for a backend developer. The project includes SQL scripts and interactions with MySQL databases, offering hands-on experience in creating databases, managing user accounts, granting privileges, and executing SQL queries. Participants grasp the fundamentals of database administration.

Technical Details
1. Codebase and Editors
The project is built using Python 3.8.5 and is designed to run on Ubuntu 20.04 LTS. Code files include a shebang line (#!/usr/bin/python3) for compatibility. Editors such as vi, vim, and emacs are utilized for code development.

2. Coding Style
Adherence to the PEP8 style guidelines (version 2.8.*) is a core requirement. Clean, well-formatted code is crucial for maintainability and collaboration.

3. Unit Testing
Unit tests are organized within the "tests" folder, employing the unittest module. Test files have the ".py" extension and follow a naming convention starting with "test_." Ensuring all tests pass without errors is a fundamental requirement.

4. SQL Scripts
SQL scripts are executed on MySQL 8.0, running on Ubuntu 20.04 LTS. SQLAlchemy version 1.4.x is employed for seamless database interactions. SQL queries are documented with comments for clarity and understanding.

Collaboration and Learning
Collaboration and teamwork are encouraged in this project. Participants can work together on test cases to ensure comprehensive coverage and address edge cases. Moreover, the project serves as a platform to enhance problem-solving skills and share knowledge within the developer community.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/Manalhub/AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/__init__.py) [/models/base_model.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/user.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/user.py) [/models/place.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/place.py) [/models/city.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/city.py) [/models/amenity.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/amenity.py) [/models/state.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/state.py) [/models/review.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/Manalhub/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone_v2$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
