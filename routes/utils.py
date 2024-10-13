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

        print(f'in function {right_ways=}')
    return right_ways

def get_times(qs, right_ways, route_travel_time) -> list:
    buses_routes = []
    all_buses = {}
    for q in qs:
        all_buses.setdefault((q.from_city_id, q.to_city_id), [])
        all_buses[(q.from_city_id, q.to_city_id)].append(q)

    for route in right_ways:
        tmp = {}
        tmp['buses'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_buses[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['buses'].append(q)
        tmp['total_time'] = total_time
        if total_time <= route_travel_time:
            buses_routes.append(tmp)
    if not buses_routes:
        raise ValueError('Время в пути больше заданного')
    else:
        return buses_routes


def get_routes(request, form) -> dict:
    context = {'form': form}
    if not form.is_valid():
        raise ValueError('Форма не валидна')

    # get data from form
    data = form.cleaned_data
    from_city = data.get('route_from_city')
    to_city = data.get('route_to_city')
    cities = data.get('cities')
    route_travel_time = data.get('route_travel_time')

    if from_city is None or to_city is None:
        raise ValueError('Не указаны города отправления или прибытия')

    qs = Bus.objects.all()
    graph = get_graph(qs)
    print(f'{graph=}')

    all_ways = list(dfs_path(graph, from_city.id, to_city.id))
    print(f'{all_ways=}')

    right_ways = get_right_ways(all_ways, cities)
    print(f'{right_ways=}')

    buses_routes = get_times(qs=qs, right_ways=right_ways, route_travel_time=route_travel_time)
    print(f'{buses_routes=}')

    sorted_routes = []
    if len(buses_routes) == 1:
        sorted_routes = buses_routes
    else:
        times = list(set(r['total_time'] for r in buses_routes))
        times = sorted(times)
        for time in times:
            for route in buses_routes:
                if time == route['total_time']:
                    sorted_routes.append(route)

    context['routes'] = sorted_routes
    print(f'{from_city.city=}')
    print(f'{to_city.city=}')
    context['cities'] = {'from_city': from_city.city, 'to_city': to_city.city}



    return context