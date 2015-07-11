"""Builder pattern example."""


from patterns.builder import Builder


builder = Builder(open)
file = builder.set_file('file.txt').set_mode('r+').build()
file.close()
