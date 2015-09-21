def price_to_float(value):
    value = value.replace(' ', '')
    dot_positions = [pos for pos in range(0,len(value)) if value[pos] == '.']
    comma_positions = [pos for pos in range(0,len(value)) if value[pos] == ',']

    if not dot_positions and not comma_positions:
        pass
    elif len(comma_positions) > 1 and len(dot_positions) > 1:
        raise ValueError('Not a recognizible number.')
    elif len(comma_positions) > 1 and len(dot_positions) == 0:
        value = value.replace(',', '')
    elif len(dot_positions) > 1 and len(comma_positions) == 0:
        value = value.replace('.', '')
    elif not dot_positions:
        if (len(comma_positions) - comma_positions[-1]) == 3:
            value = value.replace(',', '')
        else:
            value = value.replace(',', '.')
    elif not comma_positions:
        if (len(dot_positions) - dot_positions[-1]) == 3:
            value = value.replace(',', '')
        else:
            value = value.replace(',', '.')
    else:
        if dot_positions[-1] > comma_positions[-1]:
            value = value.replace(',', '')
            value = value.replace('.', '.')
        else:
            value = value.replace('.', '')
            value = value.replace(',', '.')

    return float(value)


