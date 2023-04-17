crosshair_dict = {
    "tabsen big green": "CSGO-aQxtX-NfpQc-2WzBG-WOako-CJKeB",
    "faven big yellow": "CSGO-sdonn-s95jD-4YXc4-2mxst-A7JzN",
    "dycha": "CSGO-empbi-Y4jLL-Rz6Ce-v4mWS-CCmsF",
    "konfig skinny big green": "CSGO-Oa34q-kPJJR-CT8Uc-tssQ8-f8GSQ",
    "NickleBack skinny big turqoise": "CSGO-VLvKm-6M957-yUmbn-F7c4O-XdTOG",
    "apex big turqoise": "CSGO-idk3k-MD5qw-6b9rH-tr7u7-KPh8E",
    "hampus medium red skinny": "CSGO-ZLbpO-pnqGC-teHAB-VtNeb-6shrM"
}

# "beast med red": "CSGO-MjOay-7ikY8-2T6fL-uJGVG-icywQ",
# "hunter": "CSGO-Jp4hk-AfzML-FcpUT-2pfxZ-kSLoD",
# "xyp9x": "CSGO-D7JYc-fwCWJ-wThKn-ReFfT-478WB",
# "niko small white": "CSGO-oVQVm-VnzOz-RNsAf-FaZTC-z5VeL",
# "nafany": "CSGO-MjOay-7ikY8-2T6fL-uJGVG-icywQ",
# "zywoo small green": "CSGO-XERDP-sY4Lr-o9rcw-6xuUo-7FwzF",
# "hades": "CSGO-Cf76o-xhEXm-QC9aw-3VUp7-iNsuL",
# "jame": "CSGO-kQLy3-knZHs-y5tkt-wF7Ca-c8ksF",
# "el1an": "CSGO-ywVp4-hr45N-EYesN-7hrQe-VqnkP",
# "red zywoo": "CSGO-VDHdU-kpe6u-ZXLCz-bTjff-OnMHA",

base_crosshair_id = 'crosshair'
alias = 'alias'
last_index = len(crosshair_dict) - 1
# what we want to print:
# alias crosshair0 "apply_crosshair_code CSGO-MjOay-7ikY8-2T6fL-uJGVG-icywQ; 
# alias current_crosshair crosshair0; 
# alias change_crosshair crosshair1"
for i, player in enumerate(crosshair_dict): 
    print('// ', player)
    print(
        alias, base_crosshair_id + str(i), '"apply_crosshair_code',
        crosshair_dict[player] + ';',
        alias, 'current_crosshair', base_crosshair_id + str(i) + ';',
        alias, 'change_crosshair', base_crosshair_id + str((i + 1) % len(crosshair_dict)) + '"'
    )
