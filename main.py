from preprocess import katalk_msg_parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

f_name = 'kakaotalk_data_preprocessing/text_data/test.txt'

df = katalk_msg_parse(BASE_DIR.joinpath(BASE_DIR, f_name))
print(df)