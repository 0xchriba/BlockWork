

# blockwork

blockwork is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].

###Initial Setup

Setup a Ganache server.

Add domain and port to src/blockwork/setup.py

brew install ipfs

ipfs daemon

Add domain and port to src/blockwork/setup.py

Deploy solidity/framework.sol to Ganache using Remix Online Text Editor.

Add contract address and abi to src/blockwork/setup.py.



### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv blockwork`
    2. `$ . blockwork/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

Initialize environment:
  ./start_env.sh

Run server:
  python manage.py runserver
