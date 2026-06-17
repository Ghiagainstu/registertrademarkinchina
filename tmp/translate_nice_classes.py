import json, re, time, urllib.parse, urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path('.')
SRC = ROOT / 'dist' / 'scripts' / 'classes-data.js'
OUT = ROOT / 'dist' / 'scripts' / 'classes-data-ja.js'

# parse JS array via node for reliability
import subprocess, textwrap, tempfile
src = SRC.read_text(encoding='utf-8')
tmp = ROOT / 'tmp' / 'parse_classes_en.js'
tmp.write_text(textwrap.dedent(f'''
    const s = {json.dumps(src)};
    const m = s.match(/const NICE_CLASSES = (\\[[\\s\\S]*\\]);/);
    if (!m) {{ process.exit(1); }}
    const data = eval(m[1]);
    process.stdout.write(JSON.stringify(data));
'''), encoding='utf-8')
raw = subprocess.check_output(['node', str(tmp)], cwd=str(ROOT)).decode('utf-8')
data = json.loads(raw)

# collect unique strings to minimize network calls
strings = []
seen = set()
for cls in data:
    for key in ['name', 'desc']:
        v = cls[key]
        if v not in seen:
            seen.add(v)
            strings.append(v)
    for v in cls['items']:
        if v not in seen:
            seen.add(v)
            strings.append(v)

cache = {}
lock_count = 0

def translate(q):
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ja&dt=t&q=' + urllib.parse.quote(q)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                raw = r.read().decode('utf-8', 'ignore')
            arr = json.loads(raw)
            out = ''.join(part[0] for part in arr[0] if part[0])
            return out
        except Exception:
            if attempt == 5:
                return q
            time.sleep(1.2 * (attempt + 1))
    return q

with ThreadPoolExecutor(max_workers=8) as ex:
    futs = {ex.submit(translate, s): s for s in strings}
    for i, fut in enumerate(as_completed(futs), 1):
        s = futs[fut]
        cache[s] = fut.result()
        if i % 100 == 0:
            print(f'translated {i}/{len(strings)}', flush=True)

for cls in data:
    cls['name'] = cache[cls['name']]
    cls['desc'] = cache[cls['desc']]
    cls['items'] = [cache[v] for v in cls['items']]

OUT.write_text('const NICE_CLASSES = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n', encoding='utf-8')
print(f'wrote {OUT} classes={len(data)} items={sum(len(c["items"]) for c in data)} unique_strings={len(strings)}')
