#### Project Requirements
PoetryUtils 2

Add these parameters to your bash profile to install PoetryUtils2 on your python
path

PYTHONPATH="<path_to_poetryutils2>/poetryutils2:$PYTHONPATH"

export PYTHONPATH

#### Project Setup

virtualenv --no-site-packages venv

source venv/bin/activate

python api/main.py
