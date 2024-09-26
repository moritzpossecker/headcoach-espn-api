import requests


def get_refs(url: str, ref_parent='items', ref_name='$ref') -> list[str]:
    response = requests.get(url)
    parent = response.json()[ref_parent]
    refs = []
    for child in parent:
        refs.append(child[ref_name])
    return refs
