<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<br />
<p align="center">
  <h3 align="center">Simple OCR Project</h3>

  <p align="center">
    This project is based on Django. It uses pytesseract to process the uploaded image and return the words on the picture back in Json format with the result saved in MySQL
    <br />
    <a href="https://github.com/wenb1/simpleocrproject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/wenb1/simpleocrproject">View Demo</a>
    ·
    <a href="https://github.com/wenb1/simpleocrproject/issues">Report Bug</a>
    ·
    <a href="https://github.com/wenb1/simpleocrproject/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

This project is a simple demo for OCR.


### Built With

* [Python 3.7.5]()
* [Django]()
* [MySQL]()


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In MacOS

Have Python3, pip3 and MySQL ready

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/wenb1/simpleocrproject.git
```

2. Install Django to set up the web service
```sh
pip3 install django
```

3. Install Pytesseract which is an OCR library
```sh
pip3 install pytesseract
```

4. Install Pillow which is an image library
```sh
pip3 install Pillow
```

5. Install pymysql to connect to MySQL
```sh
pip3 install pymysql
```

<!-- Usage -->
## Usage

1. Change the MySQL database name and password to yours in settings.py

2. Create a database named **simple_ocr_letters**

3. Configure the project step1
```sh
python3 manage.py makemigrations
```

4. Configure the project step2
```sh
python3 manage.py migrate
```

5. To run the unit test cases
```sh
python3 manage.py test ocr_letters
```

6. To test in the web broswer
```sh
python3 manage.py runserver
```

1. Open the web broswer and type http://127.0.0.1:8000/img/add/ in the address bar
2. Upload the image and type the name
3. Click submit and check the result from database

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Bo - wenb1@yahoo.com

Project Link: [https://github.com/wenb1/simpleocrproject](https://github.com/wenb1/simpleocrproject)





