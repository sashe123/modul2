from colorama import Fore, Style

# Заданий масив і значення k
array = [2, 1, -7, -8, 1, 0, -2, 1, -2, -6, -7, -9, 0, 6, 1, 8, 4, 4, -1, 1, 12, 10]
k = 4  # Задайте будь-яке ціле значення k > 0

# Розділяємо елементи масиву на групи відповідно до умови
negatives_less_k = [x for x in array if x < 0 and x < k]
positives_less_k = [x for x in array if x > 0 and x < k]
k_values = [x for x in array if x == k]
greater_than_k = [x for x in array if x > k]

# Формуємо новий масив, що відповідає умовам завдання
result_array = negatives_less_k + positives_less_k + k_values + greater_than_k

# Виводимо результати
print(Fore.WHITE + "Масив з 22 елементів:\n" + Style.RESET_ALL, end="")
for value in array:
    if value == k:
        print(Fore.WHITE + f"{value}*" + Style.RESET_ALL, end=" ")
    else:
        print(Fore.RED + f"{value}" + Style.RESET_ALL, end=" ")
print("\n")

print(Fore.WHITE + "Відсортований масив:\n" + Style.RESET_ALL, end="")
for value in result_array:
    if value == k:
        print(Fore.WHITE + f"{value}*" + Style.RESET_ALL, end=" ")
    else:
        print(Fore.GREEN + f"{value}" + Style.RESET_ALL, end=" ")
print()
