max_profit = 0
best_x, best_y, best_z = 0, 0, 0

kin_max = 250
dyn_max = 800
bp_max = 450
pl_max = 600

for x in range(kin_max + 1):
    for y in range(dyn_max // 2 + 1):
        for z in range(dyn_max // 5 + 1):
            kin = x
            dyn = 2 * x + 2 * y + 5 * z
            bp = 2 * x + 1 * y + 2 * z
            pl = 8 * x + 6 * y + 4 * z
            
            if kin <= kin_max and dyn <= dyn_max and bp <= bp_max and pl <= pl_max:
                profit = 90 * x + 50 * y + 45 * z
                if profit > max_profit:
                    max_profit = profit
                    best_x, best_y, best_z = x, y, z

print(f"Максимальная прибыль: {max_profit}")
print(f"Оптимальное количество: Телевизоры: {best_x}, Стереосистемы: {best_y}, Акустические системы: {best_z}")
