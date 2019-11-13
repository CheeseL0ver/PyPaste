# PyPaste

#### A Python based [Pastebin](https://pastebin.com/) "CLI" tool

## Overview
Creates a paste on Pastebin that contains the input of what was passed from stdout.

## Installation
After cloning the repo simply run:

```
$ ./install.sh
```

> **NOTE:** Pypaste depends on the enivironment variable `PASTEBIN_DEV_KEY`. So, you must create an environment variable with the name `PASTEBIN_DEV_KEY` and set its value to that of your Pastebin generated API key. For more information on how to obtain an API go [here](https://pastebin.com/api#1).

After running the install.sh file you will be able to call `pypaste` from anywhere.

## Docker

If you want to keep the app contained in a Docker image use the following process:

```
$ ./run.sh
```

This will create the image and place you into an interactive shell of the running container. Next run:

```
$ ./install.sh
```

> **NOTE:** Pypaste depends on the enivironment variable `PASTEBIN_DEV_KEY`. If you are using the Docker container version you will need to edit the **Dockerfile** and replace the text `YOUR_API_KEY` with the API key provided to you by Pastebin. For more information on how to obtain an API go [here](https://pastebin.com/api#1).

> **NOTE:** Inside of the container the application will be use port **5000**, however to the actual machine the image is running on the port being used is port **5001**.

After running the install.sh file you will be able to call `pypaste` from anywhere.

## Usage

To run PyPaste:

```
$ pypaste < [INPUT]
```

or

```
$ [INPUT] | pypaste
```
