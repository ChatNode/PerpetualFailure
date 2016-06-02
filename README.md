perpetualfailure README
==================
[![Dependency Status](https://www.versioneye.com/user/projects/54f963344f31084fdc000215/badge.svg?style=flat)](https://www.versioneye.com/user/projects/54f963344f31084fdc000215)

Getting Started
---------------

- `cd <directory containing this file>`

- `$VENV/bin/python setup.py develop`

- Install a bcrypt backend if necessary for your system. See <https://pythonhosted.org/passlib/install.html#optional-libraries>

- `$VENV/bin/initialize_perpetualfailure_db development.ini`

- `$VENV/bin/pserve development.ini`

Licensing
---------
The majority of this project is licensed under the GNU GPL 2.0 license, but
parts of the project falls under other licenses as detailed below:

- This project contains content from the Bourbon project, copyrighted by
  thoughtbot. The Bourbon license is available at LICENSE-Bourbon.
  The content in question is located inside
  `perpetualfailure/assets/scss/bourbon` and is subject to the MIT license.
  The original repository is available here:

  <https://github.com/thoughtbot/bourbon>

- This project contains content from the Bootstrap Sass project, copyrighted by
  Twitter. The Bootstrap license is available at LICENSE-Bootstrap.
  The content in question is located inside `perpetualfailure/assets/fonts`,
  `perpetualfailure/assets/js` and
  `perpetualfailure/assets/scss/bootstrap`, and is subject to the MIT license.
  The original repository is available here:

  <https://github.com/twbs/bootstrap-sass>
