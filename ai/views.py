from django.http import HttpResponse, JsonResponse
import json

def solve(request):
    data = json.loads(request.body)

    tiles = data['tiles']
    playerx = data['playerx']
    playery = data['playery']
    destinationx = data['destinationx']
    destinationy = data['destinationy']
    player_type = data['player_type']

    width = 3
    height = 3

    matrix = []
    for i in range(height):
        matrix.append(tiles[i * width:i * width + width])

    start = (playerx, playery)
    end = (destinationx, destinationy)
    if player_type == 'a*':
        path = astar(matrix, start, end)

    return JsonResponse({ 'path': path })


def astar(matrix, start, end):
    return [
        {'x': 1, 'y': 1},
        {'x': 2, 'y': 1},
        {'x': 2, 'y': 2},
    ]