li = {}
same_game_li_cnt = 0
same_pic_li_cnt = 0
same_pic_same_game_li_cnt = 0

total_cnt = 0

with open("train_1.tsv", "r") as f:
    f.readline()
    for idx, line in enumerate(f.readlines()):
        split = line.split("\t")
        photo, game_id, message, anno = split[1], split[2], split[6], split[7]
        if anno not in li.keys():
            li[anno] = {"game_id": {}, "photo_id": {}, "total_cnt": 0}
        li[anno]["game_id"][game_id] = 0
        li[anno]["photo_id"][photo] = 0

del li['-']
del li['']
del li['?']
with open("train_1.tsv", "r") as f:
    f.readline()
    for idx, line in enumerate(f.readlines()):
        split = line.split("\t")
        photo, game_id, message = split[1], split[2], split[6]
        for word in li.keys():
            if word in message:
                if game_id not in li[word]["game_id"].keys():
                    li[word]["game_id"][game_id] = 1
                else:
                    li[word]["game_id"][game_id] += 1
                if photo not in li[word]["photo_id"].keys():
                    li[word]["photo_id"][photo] = 1
                else:
                    li[word]["photo_id"][photo] += 1
                total_cnt += 1
                li[word]["total_cnt"] += 1

for word in li.keys():
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
    print("Lexical Innovation: ", word)
    print(li[word]["total_cnt"])
    print("Same game:")
    for game_id in li[word]["game_id"].keys():
        if li[word]["game_id"][game_id] > 1:
            same_game_li_cnt += 1
            print(("\t" + str(game_id)), "{:.3f}".format(float(li[word]["game_id"][game_id])/li[word]["total_cnt"]))

    print("Same photo:")
    for idx, photo_id in enumerate(li[word]["photo_id"].keys()):
        if li[word]["photo_id"][photo_id] > 1:
            same_pic_li_cnt += 1
            print(("\t" + str(idx+1)), "{:.3f}".format(float(li[word]["photo_id"][photo_id])/li[word]["total_cnt"]))
print(li)
print("Total Lexical Innovation count:", total_cnt)
print("Same Game Sustained Lexical Innovation Counts:", same_game_li_cnt)
print("Same Photo Sustained Lexical Innovation Counts:", same_pic_li_cnt)
