# 9gag-rpa

:robot: Simple RPA to automate image capture in 9GAG using Selenium and Python

## Introduction

A quick explanation of this `RPA`:

- Basically, this `RPA` opens **Firefox** and accesses the 9GAG website;

- After the page is fully loaded, the `RPA` starts to scroll down the page according to the number entered during its execution;

- This number entered during the execution of `RPA` is the number of times someone would be "clicking the down arrow";

- This was thought because 9GAG has no pagination, its content is loaded according to scroll down ad infinitum;

- After going down the specified number of times, `RPA` starts downloading ONLY the images of the main content of the site;

- Downloaded images are not repeated. There is a check to avoid downloading repeated images;

- Upon completion of `RPA`, the browser closes.

## First steps

You need to have the drivers needed to run Selenium in **Firefox**. I have separated the documentation you will need to effectively install this driver so there is no error, to access, click [here](https://selenium-python.readthedocs.io/installation.html#drivers).


After downloading the driver, be sure to install project dependencies. To do this, run the following command in the root folder (where the file `requirements.txt` is located):

```shell
$ pip install -r requiments.txt
```

Once the dependencies are installed, read on.

## Running

To run `9GAG RPA`, go to the `src/bot/` directory, and run the following command:

```
$ python app.py 1000
```

***PS: This number "1000" is the amount of "clicks down" that RPA will simulate, since in 9GAG there is not really a pagination, but an "infinite scroll". You can increase or decrease this amount as long as it is not less than 0.***

## Contributing

Feel free to do whatever you want with this project. :-)