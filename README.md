# 9gag-rpa

:robot: Simple RPA to automate image capture in 9GAG using Selenium and Python

## Introduction

First of all, you need to have the drivers needed to run Selenium in Firefox. I have separated the documentation you will need to effectively install this driver so there is no error, to access, click [here](https://selenium-python.readthedocs.io/installation.html#drivers).


After downloading the driver, be sure to install project dependencies. To do this, run the following command in the root folder (where the file `requirements.txt` is located):

```shell
$ pip install -r requiments.txt
```

Once the dependencies are installed, read on.

## Running

To run 9GAG RPA, go to the `src/bot/` directory, and run the following command:

```
$ python app.py 1000
```

*PS: This number "1000" is the amount of "clicks down" that RPA will simulate, since in 9GAG there is not really a pagination, but an "infinite scroll". You can increase or decrease this amount as long as it is not less than 0.*

## Contributing

Feel free to do whatever you want with this project. :-)