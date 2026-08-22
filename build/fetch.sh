#!/bin/sh
# Исходники Natural Earth 1:50 млн. В репозиторий не кладём — 4 МБ, качаются за пару секунд.
set -e
cd "$(dirname "$0")"
BASE=https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson
curl -sL -o countries.geojson $BASE/ne_50m_admin_0_countries.geojson
curl -sL -o rivers.geojson    $BASE/ne_50m_rivers_lake_centerlines.geojson
curl -sL -o lakes.geojson     $BASE/ne_50m_lakes.geojson
echo "готово: countries / rivers / lakes"
