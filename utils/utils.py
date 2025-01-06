def convert_to_json(data):
    data['_id'] = str(data['_id'])
    return data