# chmod +x requirements.sh to run
#!/bin/bash

python3 -m pip install --upgrade pip
pip install virtualenv
python3 -m venv env
source env/bin/activate
pip install GitPython
pip install chardet # 4.0.0
pip install shutil
pip install pandas==1.2.4
pip install matplotlib
pip install numpy
pip install seaborn
pip install sklearn
# pip install nltk
# pip install torch torchvision torchaudio
# pip install yfinance
