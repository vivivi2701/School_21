[
    "id",
    "created_at",
    "name",
    "has_test",
    "alternate_url"
],  # заголовки цсв
(.items[] | [
    .id,
    .created_at,
    .name,
    (.has_test | tostring),
    .alternate_url
]) # для каждого объекта берем нужные поля
| @csv # встроенный фильтп jq для корерктного вывода csv (с кавычками и экранированием)
