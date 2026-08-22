#!/bin/sh
# build.py -> map.json (+ самопроверка разреза), затем сборка index.html
set -e
cd "$(dirname "$0")"
[ -f countries.geojson ] || ./fetch.sh
python3 build.py
python3 - <<'PY'
t = open('tpl.html').read()
d = open('map.json').read()
open('../index.html','w').write(t.replace('__DATA__', d))
PY
echo "index.html собран"
