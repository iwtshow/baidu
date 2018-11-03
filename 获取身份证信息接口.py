
import re, json
from flask import Flask, request

app = Flask(__name__)

@app.route("/getPersonCardInfo")
def getPersonCardInfo():
    cardno = request.args.get("cardno", "")
    card_info = get_cardno_info(cardno)
    return json.dumps(card_info, ensure_ascii=False)

def get_cardno_info(cardno):
    ret = {"err": 1, "area": "", "birthday": "", "sex": ""}

    cardno = cardno.upper()
    if re.fullmatch("[1-6]\\d{16}[\\d|X]", cardno) == None:
        return ret

    code = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    i, s = 0, 0
    while i < 17:
        s += int(cardno[i]) * code[i]
        i += 1

    s = (12 - (s % 11)) % 11

    if s == 10:
        s = "X"
    else:
        s = str(s)

    if s != cardno[17]:
        return ret

    # 提取身份证号中的信息
    area_code = cardno[:6]
    with open("pid_data.txt", "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line == "":
                break

            if line[:6] == area_code:
                ret["area"] = line.split()[1]
                break

    birthday = cardno[6:14]
    birthday = "%s年%d月%d日" % (birthday[0:4], int(birthday[4:6]), int(birthday[6:8]))
    ret["birthday"] = birthday
    sex = "男"
    if int(cardno[-2]) % 2 == 0:
        sex = "女"
    ret["sex"] = sex
    if ret["area"] != "" and ret["birthday"] != "" and ret["sex"] != "":
        ret["err"] = 0
    return ret

if __name__ == '__main__':
    app.run(debug=True)
