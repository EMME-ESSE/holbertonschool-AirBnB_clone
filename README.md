# AirBnB_clone

### Description of the project

This project is part of a larger project in order to build a copy of the AirBnb website.

This project tries to be a part of the back-end console of the website. 

The project is created in Visual Studio Code and the cmd from windows.

### Description of the back-end system
The back-end system is coded in Python 3:

1). **The console system**. Is a console used to control the storage by the using of functions.

2). **Communication**. All the functions works with specific attributes depending on the user´s requeriments,
and update, create and delete in the storage.

3). **The storage**.All the process of serialization/deserialization of objects is based on JSON.

### How to use
* Download all the parts of the project

* Launch the file "console.py"

* Enter the listed commands

### Example

´´creation of object by uniq ID´´

***********

### List of command
* **create** : Creates a new instance of a class and assign a uniq id.

* **update** : Updates an instance based on the class name and the corresponding id.

* **destroy** : Destroy an instance based on the class name and the corresponding id.

* **show** : Prints the string representation of an object based on the class name.

* **all** : Prints all strings representations of all instances.
 
### List of object-attribute

* **Base Model** : id, created_at, updated_at

* **User** : email, password, first_name, last_name

* **Review** : place_id, user_id, text

* **Place** : city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids

* **Amenity** : name

* **State** : name

* **City** : state_id, name

### Contributors
Matias Mancini <matimancini@gmail.com>

Gustavo <Gustavo@gmail.com>
