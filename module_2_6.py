# ДЗ модуль 2_6. Доп. задание по модулю 2_hard."Древний шифр."
# ==========================================================
for k in range(3, 21):
    str_ = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (i + j) == 0:
                str_ += str(i) + str(j)
    print(str_)
print(f"При k: {k} ключ {i}--{str_}")
