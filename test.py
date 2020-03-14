import torch
from torch.autograd import Variable
import sys
sys.path.append('skip-thoughts.torch/pytorch')
from skipthoughts import UniSkip

dir_st = 'data/skip-thoughts'
vocab = ['robots', 'are', 'very', 'cool', '<eos>', 'BiDiBu']
uniskip = UniSkip(dir_st, vocab)

input = Variable(torch.LongTensor([
    [1,2,3,4,0], # robots are very cool 0
    [6,2,3,4,5]  # bidibu are very cool <eos>
])) # <eos> token is optional
print(input.size()) # batch_size x seq_len

output_seq2vec = uniskip(input, lengths=[4,5])
print(output_seq2vec.size()) # batch_size x 2400

output_seq2seq = uniskip(input)
print(output_seq2seq.size()) # batch_size x seq_len x 2400
