#!/bin/sh

INPUT="../ex03/hh_positions.csv"
OUTPUT="hh_uniq_positions.csv"

if [ ! -f "$INPUT" ]; then
    echo "ФАйл $INPUT не найден! запустите упр 03."
    exit 1
fi

echo ' "name", "count" ' > "$OUTPUT"

#Подсчет уникальных значений
tail -n +2 "$INPUT" | cut -d',' -f3 | tr -d '"' | sort | uniq -c | sort -nr | \
while read -r count name; do
    echo "\"$name\",$count"
done >> "$OUTPUT"

echo "Подсчет завершен. Рез-т сохранен в $OUTPUT"
