import collections
import json
import pathlib

import requests


def main() -> dict:
    
    rev_deps = pathlib.Path('asyncio_reverse_deps.txt').read_text().split('\n')
  
    meta_data = collections.defaultdict(dict)

    
    for project_name in rev_deps:
        project_name = project_name.rstrip()

        if not project_name:
            continue

        url = f"https://www.pypi.org/pypi/{project_name}/json"

        response = requests.get(url)

        # Some libraries like pytestmsfabric from wheelodex aren't on PyPi, so don't:
        # response.raise_for_status()

        # meta_data = response.json()['data']['dist_info']['metadata']
        meta_data[project_name] = response.json()

    pathlib.Path('asyncio_rev_deps_metadata.json').write_text(json.dumps(meta_data))

if __name__ =='__main__':
    main()
  
