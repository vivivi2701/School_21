#!/bin/sh
# chmod +x json_to_csv.sh - если permission denied

INPUT_JSON="../ex00/hh.json"
OUTPUT_CSV="../ex01/hh.csv"

if [ ! -f "$INPUT_JSON" ]; then
    echo "Файл "$INPUT_JSON" не найден! Запустите сначала упр. 00 ."
    exit 1
fi # Проверяем, чтоо файл хх.жсон существует

jq -f filter.jq "$INPUT_JSON" > "$OUTPUT_CSV" #(../ex02/hh.csv) запуск жк с фильтром из филтер.жк  и сохраняем рез-т в хх.цсв
#cp hh.csv ../ex02/hh.csv

echo "Преобразование завершено. Результат сохранен в $OUTPUT_CSV."
