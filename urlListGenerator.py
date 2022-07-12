import json

def url_list_generator():

    url_list = []

    table_options = []

    with open('ParserSettings.json') as file:
        settings = json.load(file)
        url_base = settings['source']

        for i in settings['competitions']:
            url_list.append(url_base + str(i))

        for i in settings['tableOptions']:
            table_options.append(i)

    return url_list, table_options
