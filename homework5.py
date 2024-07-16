# Создание переменные разных типов данных в кортеже
immutable_var = (1, "dva", "три", 4.0)
print (immutable_var)

# Невозможность изменение значений переменных в кортеже напрямую
# immutable_var.append(2222)
# print (immutable_var)

# Создание изменяемых структур данных
mutable_list = [ "Гордость", "Зависть", "Чревоугодие", "Блуд", "Алчность", "Гнев", "Уныние"]
mutable_list.extend(["и прочие радости жизни", "?"])
mutable_list.remove("?")
print (mutable_list)
