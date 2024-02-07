items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy(items, max_cost):
    items_copy = sorted(items, key=lambda x: items[x]["calories"]/items[x]['cost'], reverse=True)
    result = []
    total_cal, total_cost = 0.0, 0.0
    for i in items_copy:
        if (total_cost + items[i]["cost"]) <= max_cost:
            total_cost += items[i]["cost"]
            total_cal += items[i]["calories"]
            result.append(i)
    return {"items": result, "cal": total_cal, "cost": total_cost}


def dynamic(foods, max_cost):

    cost = [food['cost'] for food in foods.values()]
    cal = [food['calories'] for food in foods.values()]
    names = [food for food in foods.keys()]
    n = len(foods)
    # базовий елемент таблиці - калорії, ціна, список вибраних проуктів
    def_item = {'cal':0, 'cost': 0, 'items': []}
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[def_item for w in range(max_cost + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for c in range(max_cost + 1):
            if i == 0 or c == 0:
                K[i][c] = def_item
            elif cost[i - 1] <= c:
                cur = cal[i - 1] + K[i - 1][c - cost[i - 1]]['cal']
                if cur > K[i - 1][c]['cal']:
                    # print(K[i - 1][c]) 
                    K[i][c] = {'cal':cur, 'cost':cost[i - 1] + K[i - 1][c - cost[i - 1]]['cost'], 'items': K[i - 1][c - cost[i - 1]]['items'] + [names[i - 1]]}
                else:
                    K[i][c] = K[i - 1][c]
            else:
                K[i][c] = K[i - 1][c]

    # for el in K:
    #     print(el)

    return K[n][max_cost]
    

# it = items.copy()
# for val in it.values():
#     val.update({"cal/cost": val["calories"]/val["cost"]}) 
# it = sorted(it, key=lambda x: items[x]["cal/cost"], reverse=True)
# print(it)
if __name__ == "__main__":
    
    # Бюджет
    budget = 100

    res_greedy = greedy(items, budget)
    print("Greedy. Choices: ", res_greedy['items'], "Total Cal: ", res_greedy['cal'], "Total Cost: ", res_greedy['cost'])
    res_dyn = dynamic(items, budget)
    # print(res_dyn)
    print("Dynamic. Choices: ", res_dyn['items'], "Total Cal: ", res_dyn['cal'], "Total Cost: ", res_dyn['cost'])