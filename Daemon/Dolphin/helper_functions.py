# game id hex converter

def hex_converter(hex_list, game_list_raw, game_list_processed):
    import codecs
    #print(hex_list)
    for hex in hex_list:
        hex_str = hex
        res = codecs.decode(hex_str, 'hex').decode('utf-8')
        duplicate = []
        for data in game_list_raw:
            if res == data["Game ID"] and res not in duplicate:
                duplicate.append(res)
                #print(f"Game ID is {res} and Game Name is {data['Game Name']}")
                game_list_processed.append({"Game ID": res, "Game Name": data['Game Name']})

def simple_hex_convert(hex):
    import codecs
    hex_str = hex
    res = codecs.decode(hex_str, 'hex').decode('utf-8')
    return res