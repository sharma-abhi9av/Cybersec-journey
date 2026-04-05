"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """

    return list(wagon)
    pass


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    x, y, z, *rest = each_wagons_id
    return [z, *missing_wagons, *rest, x, y]



def add_missing_stops(route , **stops):
    """Add missing stops to route dict.
    
    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(stops.values())
    return route
    
    

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended = {**route, **more_route_information}
    return extended
    pass


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    final = [list(row) for row in zip(*wagons_rows)]
    return final
    pass
