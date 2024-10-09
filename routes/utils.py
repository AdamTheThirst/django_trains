from buses.models import Bus


def get_graph(qs) -> dict:
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph

def get_routes(request, form) -> dict:
    qs = Bus.objects.all()
    graph = get_graph(qs)