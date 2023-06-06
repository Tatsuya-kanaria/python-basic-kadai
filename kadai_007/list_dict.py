# %%
list = [
"月曜日は晴れです",
"火曜日は雨です",
"水曜日は晴れです",
"木曜日は晴れです",
"金曜日は曇りです",
"土曜日は曇りのち雨です",
"日曜日は雷雨です"]

dictionary = {
"mon":"晴れ",
"tue":"雨",
"wed":"晴れ",
"thu":"晴れ",
"fri":"曇り",
"thu":"曇りのち雨",
"sun":"雷雨",
}

list_ = [print(x) for x in list if "水曜日" in x]

dict_ = {print(f'{key}:{value}') for key, value in dictionary.items() if "wed" in key }


# %%
