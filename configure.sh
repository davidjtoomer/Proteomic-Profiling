# activate the virtual environment
conda env create -f environment.yml
source activate secreted-labeler

# securely install pip and all dependencies
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install -r requirements.txt

# make sure all dependencies are imported properly
python testenvironment.py || exit 1