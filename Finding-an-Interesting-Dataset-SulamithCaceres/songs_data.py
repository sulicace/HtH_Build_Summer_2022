import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

song_data = pandas.read_csv("songs_normalize.csv")

print(song_data)