import sys
import json
import re

(file_,) = sys.argv[1:2] or ('',)

with open(file_,'rt') as f:
    d = json.load(f)


for k in [
    "agentuity",
    "aiomoqt",
    "aiosimon-io",
    "batch-executor",
    "chuk-llm",
    "emmi",
    "graph-context",
    "hipcheck-sdk",
    "LiveChessCloud",
    "llama-metasearch",
    "local-flight-map",
    "logos-shift-client",
    "lumeo",
    "mcp-agent-x",
    "mcp-text-editor",
    "ninjakiwi-api",
    "orange-mcp-llm-bridge",
    "ostium-python-sdk",
    "pic-prompt",
    "piedpiper-engine",
    "py-http-auto-test",
    "response-bandwidth-limiter",
    "revup",
    "smart-agent",
    "stone-connect",
    "superstream-beta",
    "superstream-py-beta",
    "superstream-py",
    "test-impact-analyzer",
    "yandex-query-magic",


]:
    # extras = set()
    v = d[k]
    deps = []
    asyncio_dep_spec = "asyncio==3.4.3"  # Test the last non no-op release by default
    info_deps = v.get('requires_dist', [])
    for dep in info_deps:

        # Split on white space to ignore pins of the tuple-like form "package-name (<2,>1)"
        dep_no_extras = dep.partition(';')[0].split()[0]
        m = re.match(r'\w[a-z0-9\-]+', dep_no_extras)
        if m and m.group(0) == 'asyncio':
            asyncio_dep_spec = dep_no_extras
        else:
            deps.append(f'"{dep_no_extras}"')
        # if 'pytest' not in dep:
        #     continue
        # extra = dep.partition('extra ==')[2]
        # m = re.search(r'[\'"](?P<extra_name>.*)[\'"]', extra)
        # if m:
        #     extras.add(m.group('extra_name').strip())

    print('          - {' f'package_name: {k}, ', end='')
    # print('to_install: ',end='')
    # if extras:
    #     print(f'".[{",".join(extras)}]",' '},')
    # else:
    #     print('".", },')
    print(f"deps: '{" ".join(deps)}'," '}')
