# Text-Summarization


Follow the below instructions for running the test-file

git clone https://github.com/arunhiremath92/Text-Summarization
cd Text-Summarization

mkdir -P data

wget http://www.cs.toronto.edu/~rkiros/models/dictionary.txt -P ./data

wget http://www.cs.toronto.edu/~rkiros/models/utable.npy -P ./data

wget http://www.cs.toronto.edu/~rkiros/models/btable.npy -P ./data

wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz -P ./data

wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl -P ./data

wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz -P ./data

wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl -P ./data


python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python test.py


After executing the last line it should download some stuff (~2-GB) and run the test
program.


