import pandas1 as pd
# python字典格式
population_dict = {'California': 566516,
                   'Texas': 645441,
                   'New York': 214451,
                   'Florida': 120565}
# Python Series对象
population = pd.Series(population_dict)
# python字典格式
area_dict = {'California': 6,
             'Texas': 21,
             'New York': 20,
             'Florida': 5}
# Python Series对象
area = pd.Series(area_dict)
# Python DataFrame
states = pd.DataFrame({'population': population,
                       'area': area})
print(states)
# print(states.index)
# print(states.columns)
# print(states.area)
# print(states.population)


print(area[(area > 0) & (area < 20)])
