#!/bin/sh

OUTFILE="combined.csv"
CSV_DIR="../ex03"
[ -f "$OUTFILE" ] && rm "$OUTFILE"
# Удаляем файл, если существует


if [ ! -d "$CSV_DIR" ]; then
  echo "Каталог $CSV_DIR не найден!"
  exit 1
fi  # Проверяем, есть ли CSV-файлы

#shopt -s nullglob 2>/dev/null || true  # првоеряем, есть ли цсв-файлы.  для баш, игнорим ошибку если shopt нет в sh

files=$(ls "$CSV_DIR"/*.csv 2>/dev/null)

if [ -z "$files" ]; then
    echo "в папке $CSV_DIR нет CSV-файлов для объединения. Вернитесь к 3 упр."
    exit 1
fi

[ -f "$OUTFILE" ] && rm "$OUTFILE"  # Удаляем файл результата, если существует


first=1
for file in $(ls "$CSV_DIR"/*.csv | sort); do
  if [ $first -eq 1 ]; then

    cat "$file" >> "$OUTFILE" # Копируем заголовок и данные из первого файлaa
    first=0
  else

    tail -n +2 "$file" >> "$OUTFILE" # Из остальных файлов пропускаем заголовок (первую строку)
  fi
done

echo "Объединение файлов завершено. Результат в $OUTFILE. Пасиба."
