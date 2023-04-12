import re
import pandas as pd


def katalk_msg_parse(file_path):
    print(file_path)
    my_katalk_data = list()
    katalk_msg_pattern = "[0-9]{4}[년.] [0-9]{1,2}[월.] [0-9]{1,2}[일.] [0-9]{1,2}:[0-9]{1,2},.*:"
    date_info = "[0-9]{4}년 [0-9]{1,2}월 [0-9]{1,2}일 \S요일"
    in_out_info = "[0-9]{4}[년.] [0-9]{1,2}[월.] [0-9]{1,2}[일.] [0-9]{1,2}:[0-9]{1,2}:.*"

    for line in open(file_path, 'rt', encoding='UTF8'):
        if re.match(date_info, line) or re.match(in_out_info, line):
            continue
        elif line == '\n':
            continue
        elif re.match(katalk_msg_pattern, line):
            line = line.split(",")
            date_time = line[0]
            user_text = line[1].split(" : ", maxsplit=1)
            user_name = user_text[0].strip()
            text = user_text[1].strip()
            my_katalk_data.append({'date_time': date_time,
                                   'user_name': user_name,
                                   'text': text
                                   })

        else:
            if len(my_katalk_data) > 0:
                my_katalk_data[-1]['text'] += "\n"+line.strip()

    my_katalk_df = pd.DataFrame(my_katalk_data)

    return my_katalk_df