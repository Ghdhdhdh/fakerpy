class fakerpy():
    def __init__(self):
        pass
    def name():
        import json
        import random
        # Read the json file and return all the names
        with open('names.json') as f:
            data = json.load(f)
            return data[random.randint(0, len(data) - 1)]
    def email():
        import random
        return fakerpy.name() + str(random.randint(0,9)) + '@gmail.com'

