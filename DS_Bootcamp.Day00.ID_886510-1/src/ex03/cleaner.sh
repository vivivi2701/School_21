#!/bin/sh

INPUT="../ex02/hh_sorted.csv"
OUTPUT="hh_positions.csv"

if [ ! -f "$INPUT" ]; then
    echo "Файл $INPUT не найден! Запустите упр 02."
    exit 1
fi

head -n 1 "$INPUT" > "$OUTPUT"

tail -n +2 "$INPUT" | while IFS=',' read -r id created_at name has_test alternate_url; do
    clean_name=$(echo "$name" | tr -d '"')

    levels=""
    for level in Junior Middle Senior; do
        case "$clean_name" in
            *"$level"*)
                if [ -z "$levels" ]; then
                    levels="$level"
                else
                    levels="$levels/$level"
                fi
                ;;
        esac
    done

    if [ -z "$levels" ]; then
        levels="-"
    fi

    echo "\"$id\",\"$created_at\",\"$levels\",$has_test,\"$alternate_url\""
done >> "$OUTPUT"

echo "Очистка завершена. Рез-т сохранен в $OUTPUT"

