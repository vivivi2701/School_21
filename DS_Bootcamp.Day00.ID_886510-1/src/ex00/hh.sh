#!/bin/sh

OUTPUT_JSON="hh.json"

if [ -z "$1" ]; then
    echo "Usage: $0 <поисковый_запрос>"
    exit 1
fi

QUERY=$(printf "%s" "$1" | jq -sRr @uri)
curl "https://api.hh.ru/vacancies?text=${QUERY}&per_page=20" | jq . > "$OUTPUT_JSON" #../ex01/hh.json
#cp hh.json ../ex01/hh.json

echo "ДАнные сохранены в $OUTPUT_JSON"
