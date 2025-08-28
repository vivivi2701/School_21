#!/bin/sh

INPUT_CSV="../ex01/hh.csv"
OUTPUT_SORTED_CSV="../ex02/hh_sorted.csv"

if [ ! -f "$INPUT_CSV" ]; then
    echo "Файл $INPUT_CSV не найден! Запустите упр. 01."
    exit 1
fi # Проверили, что файл хх.цсв сущ-т

head -n 1 "$INPUT_CSV" > "$OUTPUT_SORTED_CSV" # берем заголовок и пишем его в новый файл

tail -n +2 "$INPUT_CSV" | sort -t, -k2,2 -k1,1 >> "$OUTPUT_SORTED_CSV" #Сортируем остльн. строки по 2му(created_at) и 1му(id) столбцам, используя запятую как разделитель.-n +2 - берем все строки кроме заг-ка. Рез-т добавляем в файл с щаголовком.
# -t, - разделитель полей(запятая), -k2,2 - сортируем по 2му столбцу, -k1,1 - по 1му столбцу

#cp hh_sorted.csv ../ex03/hh_sorted.csv
echo "Сортировка завершена. Рез-т сохранен в $OUTPUT_SORTED_CSV"
