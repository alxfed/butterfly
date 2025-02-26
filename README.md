# Butterfly
This is a **template repository** for using the 'blue-yonder' package. In order to create a repository with this template in your account or the account of your organization just click the 'Use this template' button on the top of this page and fill all the necessary information about ownership of the repository. The copy of this repo will appear in your account where you will be able to use and modify it the way you want.
![image description](./pictures/use_template.png)
<br>The `blue-yonder` package is a pypi Python package that allows you to program your own automation of simple tasks on BlueSky network using Python. It can also be your door to the brave new world of AI, because it can serve as a connector between your Language Models and your social presence account on BlueSky if you know Python and can write programs that you need.

#### Installation of 'blue-yonder' package
To install the `blue-yonder` package from pypi.org, run the following command in your terminal:
```Bash
pip install blue-yonder 
```

#### Usage
To use the `blue-yonder` package, import it in your Python code:
```Python
from blue_yonder import Actor, Another, yonder
```
Notice that the name of the library that you are using is `blue_yonder`, with an underscore.
<br>There are more 'playful' aliases for the `blue_yonder` Client too; namely:
```Python
from blue_yonder import Butterfly, Flower, yonder
```
This is because Butterflies are the main 'clients' of the blue sky of course... and they interact with Flowers.

After using this template repository to create your own repository in your account, clone it to your computer and create a git excluded file .env using a .env_example format; use it to set the environment variables. As an alternative you can use git excluded config.yaml file formatted as it is shown in config_example.yaml file and go_configure function in a py file next to it.

#### Examples
The BlueSky service uses handle, password as well as assessions and tokens associated with your account that let you make changes in the environment of the BlueSky. While authorized you can post text or images, change the preferences of your account and perform many other actions.

#### [0. How to log-in (and the `.env` file)](./how_to_log_in.py)
The best way to let your Python programs work with the BlueSky API is to use an .env file to store all the necessary credentials, which will be used automatically by the `blue-yonder` package in your log-in. As an alternative you can store them in a config.yaml file (and exclude it from git).
#### [1. How to save a session](./how_to_save_session.py)
In browser all the necessary credentials obtained from BlueSky when you log-in are (automatically) stored in cookies of your browser, but if you are building your own automation you need to take care of that youself. This mechanism will help the Bluesky service to avoid overloads and will also save you 'limits' (there is a maximum number of authenticated API calls that you can make per minute and per day).
#### [2. How to post text](./post_text.py)
This is a most basic example of a plain text post that will be on your profile. 
```Python
text = 'This is a post.'
my_actor = Actor()
result = my_actor.post(text)
```
#### [3. Post a reply](./post_reply.py)
```Python
post = 'https://bsky.app/profile/multilogue.bsky.social/post/3lfngdvswe725'
reply_text = 'This is a reply'
reply = my_actor.in_reply_to(post).post(reply_text)
```
#### [4. How to post a quote](./post_quote.py)
This is an example of a plain text post quoting any other Bluesky post.
```Python
url = 'https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l'
result = my_actor.with_quoted_post(url).post(plain_text)
```
#### [5. How to post a reply with a quote](./post_reply_with_quote.py)
You can add a quote of another Bluesky post to a reply.
```Python
url = 'https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l'
reply = my_actor.in_reply_to(post).with_quoted_post(url).post(reply_text)
```
#### [6. Post text and embed an image](./post_embed_image.py)
This is an example of a text (which can be an empty string) post with an embedded image.
#### [7. Post text and a link to external page](./post_embed_external.py)
This is an example of a post with a link (actually a 'site card') to a page on any external site.
