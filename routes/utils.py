from buses.models import Bus

def dfs_path(graph: dict, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))

def get_graph(qs) -> dict:
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph

def get_right_ways(all_ways: list, cities: list) -> list:
    if not len(all_ways):
        raise ValueError('Маршрута нет')
    if cities:
        cities_id_list = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in cities_id_list):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Маршрута через эти города нет')
    else:
        right_ways = all_ways

        print(f'{right_ways=}')


def get_routes(request, form) -> dict:
    context = {'form': form}
    if not form.is_valid():
        raise ValueError('Форма не валидна')

    # get data from form
    data = form.cleaned_data
    from_city = data.get('route_from_city')
    to_city = data.get('route_to_city')
    cities = data.get('cities')

    if from_city is None or to_city is None:
        raise ValueError('Не указаны города отправления или прибытия')

    qs = Bus.objects.all()
    graph = get_graph(qs)
    print(f'{graph=}')
    route_travel_time = data.get('route_travel_time')
    all_ways = list(dfs_path(graph, from_city.id, to_city.id))
    print(f'{all_ways=}')

    right_ways = get_right_ways(all_ways, cities)

    buses = []
    all_buses ={}
    for q in qs:
        all_buses.setdefault((q.from_city_id, q.to_city_id), [])
        all_buses[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        tmp = {}
        tmp['buses'] = []
        total_time = 0
        for i in range(len(route)-1):
            qs = all_buses[(route[i], route[i+1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['buses'].append(qs)
        tmp['total_time'] = total_time
        if total_time <= route_travel_time:
            buses.append(tmp)
    if not buses:
        raise ValueError('Время в пути больше заданного')




    return context