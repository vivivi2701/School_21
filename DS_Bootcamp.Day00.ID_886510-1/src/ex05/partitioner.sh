#!/bin/sh

INPUT="../ex03/hh_positions.csv"
OUTDIR="."

if [ ! -f "$INPUT" ]; then
  echo "Файл $INPUT не найден! Запустите упр 03."
  exit 1
fi

header=$(head -n 1 "$INPUT")

tail -n +2 "$INPUT" | while IFS=',' read -r id created_at name has_test alternate_url; do

  date=$(echo "$created_at" | cut -c1-10 | tr -d '"')  # Извлекаем дату YYYY-MM-DD из created_at
  file="$OUTDIR/$date.csv"


  if [ ! -f "$file" ]; then  # Если файл не существует, создаём и пишем заголовок
    echo "$header" > "$file"
  fi


  echo "\"$id\",\"$created_at\",\"$name\",$has_test,\"$alternate_url\"" >> "$file" # Добавляем строку в файл
done

echo "Разбиение по датам завершено. Пасиба."
