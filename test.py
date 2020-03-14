import skipthoughts
model = skipthoughts.load_model()
encoder = skipthoughts.Encoder(model)
vocab = ['robots', 'are', 'very', 'cool', '<eos>', 'BiDiBu']
vectors = encoder.encode(vocab)
print(vectors)
