# the-f-calculator 

This is a python package hosted on PYPI and can be used to perform basic functions on calculator such as:
- ADDITION
- SUBTRACTION
- DIVISION
- MULTIPLICATION
- Nth ROOT OF NUMBER N

### License

The source code is released under an MIT License.

**Author: Oluwafunmilayo  Somoye<br />
Maintainer: Oluwafunmilayo Somoye**

the-f-calculator package has been tested on respectively Mac OS 10.15.7.
This is a school project, expect may never change and any fitness for a particular purpose is disclaimed.


### Installation

pypi_calculator requires python3 and can be installed via PYPI
``` shell
$ pip install the-f-calculator
```


### Usage
The calculator can be used for basic mathematical computation. The calculator has a memory that can reset itself to 0 and also stores previous values, except the memory is reset


Sample Code

``from actions import Calculator``

cal = Calculator()

There are 4 functions in this package:
- add(): takes a list of numbers, whether integers or floats
- subtract(): takes a list of numbers, whether integers or floats
- divide(): takes numbers
- multiply(): takes numbers
- root()


### Development
You can contribute to this project by cloning this repo and pushing to a branch for review and merging.

### Docker
pypi_calculator is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.


**It is a Free Software**
