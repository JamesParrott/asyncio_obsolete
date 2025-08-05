import json, pathlib
s = 'asyncio_rev_deps_metadata'
d = json.loads(pathlib.Path(f'{s}.json').read_text())

keys = list(d)
d1 = {k: d[k] for k in keys[:705]}
d2 = {k: d[k] for k in keys[705:]}
pathlib.Path(f'{s}_i.json').write_text(json.dumps(d1))

pathlib.Path(f'{s}_ii.json').write_text(json.dumps(d2))
