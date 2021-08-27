import sys

try:
    # パス取得
    file_paths = sys.argv[1:]

    # 不要行の削除
    for path in file_paths:
        # ファイルの内容をリスト化
        with open(path,"r") as outfile:
            data = outfile.readlines()

        # 抽出データの書込み
        with open(path,"w+") as datafile:
            for linenum, line in enumerate(data):
                if "*      Firefly" in line:
                    for line in data[linenum-2:]:
                        datafile.write(line)
except:
    pass