def calculate_wpm(row):
    characters_typed = len(row['entered']) # num of characters typed
    time_taken_sec = row['end_time'] - row['start_time'] # time taken
    wpm = ((characters_typed / time_taken_sec) / 5) * 60 # wpm
    return wpm