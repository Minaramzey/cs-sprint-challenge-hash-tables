#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = [None] * length
    for t in tickets:
        if t.source == "NONE":
            route[0] = t.destination
        else:
           cache[t.source] = t.destination
    if length > 1:
        for i in range(1, length):
            route[i] =cache[route[i-1]]

    return route



