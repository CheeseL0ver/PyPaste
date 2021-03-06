# PyPaste [![Build Status](https://travis-ci.org/CheeseL0ver/PyPaste.svg?branch=master)](https://travis-ci.org/github/CheeseL0ver/PyPaste)

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

## Licensing

- Source code Copyright &copy; 2020 Shandon Anderson.

  ![GPL3](https://www.gnu.org/graphics/lgplv3-147x51.png)

  This program is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses>.

