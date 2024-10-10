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


def get_routes(request, form) -> dict:
    context = {'form': form}
    if not form.is_valid():
        raise ValueError('Форма не валидна')
    data = form.cleaned_data
    from_city = data.get('route_from_city')
    to_city = data.get('route_to_city')

    print(from_city, to_city)

    if from_city is None or to_city is None:
        raise ValueError('Не указаны города отправления или прибытия')

    qs = Bus.objects.all()
    graph = get_graph(qs)
    print(graph)
    route_travel_time = data['route_travel_time']
    all_ways = dfs_path(graph, from_city.id, to_city.id)
    if not len(list(all_ways)):
        raise ValueError('Маршрута нет')
    return context