import json, pathlib
s = 'asyncio_rev_deps_metadata'
d = json.loads(pathlib.Path(f'{s}.json').read_text())

keys = list(d)

d_pytest = {}
for k in keys:
    v = d[k]
    info = v.get('info',{})
    deps = info.get('requires_dist',None) or []
    if any('pytest' in dep for dep in deps):
        d_pytest[k] = info
        d.pop(k)
pathlib.Path(f'{s}_pytest.json').write_text(json.dumps(d_pytest, indent='\t'))


keys = list(d)
N = len(keys)
step = 255
for i in range(0,N,step):
    d_i = {k: d[k].get('info',{}) for k in keys[i:min(N,i+step)]}
    pathlib.Path(f'{s}_{i}.json').write_text(json.dumps(d_i, indent='\t'))

