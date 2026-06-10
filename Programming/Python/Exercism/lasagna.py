EXPECTED_BAKE_TIME = 40    
def bake_time_remaining(elasped_time):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elasped_time   
def preparation_time_in_minutes(number_of_layers):
    """Return preparation time based on 2 mins per layer."""
    return number_of_layers * 2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total time spent (prep time + bake time)."""
    return (number_of_layers * 2) + elapsed_bake_time
