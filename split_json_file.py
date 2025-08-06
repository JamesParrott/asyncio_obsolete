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

def write_files_of_255_entries(dict_, file_name):
    keys_ = list(dict_)
    N = len(keys_)
    step = 255
    for i in range(0,N,step):
        d_i = {k: dict_[k] for k in keys_[i:min(N,i+step)]}
        pathlib.Path(f'{file_name}_{i}.json').write_text(json.dumps(d_i, indent='\t'))

write_files_of_255_entries(d_pytest, f'{s}_pytest')
write_files_of_255_entries({k: v.get('info',{}) for k, v in d.items()}, s)