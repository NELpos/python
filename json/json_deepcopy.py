import json

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError("duplicate key: %r" % (k,))
        else:
           d[k] = v
    return d

def load():
    with open('test.json') as json_file:
        json_data = json.load(json_file, object_pairs_hook=dict_raise_on_duplicates)
        print(json_data)

if __name__=='__main__':
    load()