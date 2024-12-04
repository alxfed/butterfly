# Butterfly
This is a **template repository** for using the 'blue-yonder' package. If you want to create a repository with this template in your account or the account of your organization just click the 'Use this template' button on the top of this page and the copy of this repo will appear in your account where you will be able to use and modify it the way you want.
![image description](./pictures/use_template.png)
<br>The `blue-yonder` package is a pypi Python package that allows you to program your own automation of simple tasks on BlueSky. It can also be your door to the brave new world of AI, because it can serve as a connector between your Language Models and your social presence account on BlueSky if you know Python and can write programs that you need.

#### Installation of 'blue-yonder' package
To install the `blue-yonder` package from pypi.org, run the following command in your terminal:
```Bash
pip install blue-yonder 
```

#### Usage
To use the `blue-yonder` package, import it in your Python code:
```Python
from blue_yonder import Client
```
Notice that the name of the library that you are using is `blue_yonder`, with an underscore.
<br>There are more 'playful' aliases for the `blue_yonder` Client too; namely:
```Python
from blue_yonder import Butterfly
# or
from blue_yonder import Bird
```
This is because Butterflies and Birds are the main 'clients' of the blue sky of course.

After using this template repository to create your own repository in your account, clone it to your computer and create a git excluded file .env using a .env_example format and use it to set the environment variables. As an alternative you can use git excluded config.yaml file formatted as it is shown in config_example.yaml file and go_configure function in a py file next to it.

#### Examples
The BlueSky service uses sessions and tokens associated with your account that let you make changes in the environment of the BlueSky. While authorized you can post text or images, change the preferences of your account and perform many other actions that suits you best.

In browser all the necessary credentials are (automatically) stored in cookies of your browser, but if you are building your own automation you need to take care of all that youself, otherwise the 'log-in' service of BlueSky would be overwhelmed by repeated log-in attempts and we don't want that to happen. That is why the very first example is:
#### [1. How to save a session](./how_to_save_session.py)
This mechanism, together with the ability of blue-yonder Client to check the validity of the passed 'jwt' when it is instantiated will help the service to avoid overloads.
#### [2. How to post text](./post_text.py)