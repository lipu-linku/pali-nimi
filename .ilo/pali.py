"""
mi lipu e nimi ale kepeken ni.

sina wile sin e lipu ale la
  - o kama jo e poki `data.json` tan lipu http://linku.la/jasima/data.json,
  - o ni lon open pi lipu ni: `python ./.ilo/pali.py`
"""

import json
import os

KULUPU_WILE = {"core", "widespread"}

LIPU_NIMI = """## %(nimi)s

#### sona pu

%(sona_pu)s

#### sona Linku pi toki Inli

%(toki_Inli)s

#### sona Linku pi toki pona

%(toki_pona)s

#### sona sin

"""


def o_lipu_e_nimi(nimi: str, sona: dict):
    poki = nimi[0]
    nimi_lipu = nimi + ".md"
    ma_lipu = poki + os.sep + nimi_lipu
    os.makedirs(poki, exist_ok=True)

    sona_pu = ""
    if nimi_pu := sona.get("pu_verbatim", {}):
        sona_pu = nimi_pu.get("en", "")
        if not sona_pu:
            sona_pu = nimi_pu.get("eo", "")

    ijo_pana = {
        "nimi": nimi,
        "sona_pu": sona_pu,
        # nimi kijetesantakalu li jo ala
        "toki_Inli": sona["def"]["en"],
        "toki_pona": sona["def"]["tok"],
    }

    with open(ma_lipu, "w") as lipu:
        lipu.write(LIPU_NIMI % ijo_pana)

    print("mi pali e lipu %s" % ma_lipu)


def pali():
    lipu_sona = open("data.json", "r")
    ale = lipu_sona.read()
    lipu_sona.close()

    ale = json.loads(ale)
    ale = ale["data"]
    for nimi, sona in ale.items():
        if sona["usage_category"] not in KULUPU_WILE:
            continue
        o_lipu_e_nimi(nimi, sona)


if __name__ == "__main__":
    pali()
