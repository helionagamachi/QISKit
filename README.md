# QISKit

## Setup


`git submodule init && git submodule update`


### Acessing the tutorial


`docke-compose up notebook`

go to the url pointed in the terminal


### For the python runtime:

Copy the `my.env.example` file into `my.env` and put up the IBMQE key there


`docker-compose run --rm python`

A new container will startup with a bash shell

Once there `sudo pip install -r requirements.txt`
