from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.generate()

textgen.train_from_file('data.txt', num_epochs=1)
textgen.generate()
