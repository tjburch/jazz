# TODO: generate song class
# TODO: establish table merging proceedure so I only need one dataframe to pass
"""I think we want 2 dataframes. 
One with the pitches and all their info 
Second with all the metadata
Assume dataframe has been skimmed down to this song *only*
""" 

class Song:

    def __init__(self, music_dataframe, meta_dataframe):
        self.pitches = music_dataframe.pitch
        self.beats = music_dataframe.beat
        self.title = meta_dataframe.title

        self.measures = []
        for i in range(min(music_dataframe.bar), max(music_dataframe.bar)):
            this_measure_df = music_dataframe[music_dataframe == i]
            self.measures.append(Measure(this_measure_df))

class Measure:

    def __init__(self, measure_df):
        self.notes = []
        for i, row in measure_df.iterrows():
            self.notes.append(Note(measure_df.at[i,'pitch'], measure_df.at[i,'beat']))


class Note:

    def __init__(self, pitch, beat):
        self.pitch = pitch
        self.beat = beat


