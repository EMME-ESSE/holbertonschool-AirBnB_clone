# AirBnB_clone

## Description of the project

This project is part of a larger project in order to build a copy of the AirBnb website.

This project tries to be a part of the back-end console of the website. 

The project is created in Visual Studio Code and the cmd from windows.

## Description of the back-end system
The back-end system is coded in Python 3:

:one: **The console system**. Is a console used to control the storage by the using of functions.
      
:two: **Communication**. All the functions manage specific attributes depending on the user´s requeriments and works in the storage.
      
:three: **The storage**.All the process of serialization/deserialization of objects is based on JSON.

## How to use

:small_blue_diamond:  Download all the parts of the project

:small_blue_diamond:  Launch the file "console.py"

:small_blue_diamond:  Enter the listed commands

## Example

```creation of object by uniq ID```

***********

## List of command
:small_blue_diamond: **create** : Creates a new instance of a class and assign a uniq id.

:small_blue_diamond: **update** : Updates an instance based on the class name and the corresponding id.

:small_blue_diamond: **destroy** : Destroy an instance based on the class name and the corresponding id.

:small_blue_diamond: **show** : Prints the string representation of an object based on the class name.

:small_blue_diamond: **all** : Prints all strings representations of all instances.
 
## List of object-attribute

:small_blue_diamond: **Base Model** : id, created_at, updated_at

:small_blue_diamond: **User** : email, password, first_name, last_name

:small_blue_diamond: **Review** : place_id, user_id, text

:small_blue_diamond: **Place** : city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids

:small_blue_diamond: **Amenity** : name

:small_blue_diamond: **State** : name

:small_blue_diamond: **City** : state_id, name

## Contributors
:small_orange_diamond: Matias Mancini <matimancini@gmail.com>

:small_orange_diamond: Gustavo <gdponcemarsiglia@gmail.com>
