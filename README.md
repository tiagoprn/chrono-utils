# chronofilter

Given timestamped records on stdin, prints on stdout the ones that will happen in the near future, taking the current timestamp as a reference.

Here (TODO: Put github link here) is an example on how to use it. Check also the tests (TODO: Put github link here) for more scenarios.

You can use the main script standalone on any python3 installation, since it does not require any third party dependency. To do that, you can simply download it with curl:
```
TODO
```

# Setting up the development environment

1. Make sure you have pyenv installed. If not, install it.

2. Install pipx on your python distribution using the system's installed python (generally python3). With pipx you can install python utilities on isolated environments, which fits perfectly to install poetry. To install it: `sudo pip3 instal pipx`

3. After installing pipx, run: `pipx install poetry`

4. Create and enter a folder with the project's name, where you will use pyenv to define the python version that will be used by poetry to automatically create the virtualenv: `pyenv local 3.9.1`

5. Clone this repository with git clone

6. Enter the cloned repository folder

7. Run the following command to setup the development environment: `make requirements`

PS: To understand a little more about poetry, you can check [this note of mine](https://tiagopr.nl/posts/published/using-poetry-for-dependencies-on-python-projects/).

