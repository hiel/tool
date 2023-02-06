# 파이썬 문자열을 json으로 변환
# '' -> ""
# None, True, False -> null, true, false

import json

try:
    string = """
{'a': True, 'b': False, 'c': None}
"""

    string = string.replace("'", '$$$')
    string = string.replace('"', "'")
    string = string.replace("$$$", '"')
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    string = string.replace('None', 'null')

    parsed = json.loads(string)

    print(json.dumps(parsed, indent=4))

except Exception as e:
    import traceback
    trace = traceback.format_exc()
    print(str(e), trace)
