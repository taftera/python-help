def store_known():
  save_kanji = WORD['kanji'].strip()
  save_hiragana = WORD['hiragana']
  save_translation = WORD['translation']
  try:
    with open('data/words_learned.csv', mode='r') as data_file: 
      print(data_file)
  except FileNotFoundError:
    with open('data/words_learned.csv', mode='w') as data_file:
      print('new file created')
      data_file.write(f"kanji,hiragana,translation")
      data_file.write(f"\n{save_kanji},{save_hiragana},{save_translation}")
  else:
    with open('data/words_learned.csv', mode='a') as data_file:
      data_file.write(f"\n{save_kanji},{save_hiragana},{save_translation}")
