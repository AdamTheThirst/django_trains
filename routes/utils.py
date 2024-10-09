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
    qs = Bus.objects.all()
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    route_travel_time = data['route_travel_time']
    all_ways = dfs_path(graph, from_city.id, to_city.id)
    if not len(list(all_ways)):
        raise ValueError('Маршрута нет')
    return context