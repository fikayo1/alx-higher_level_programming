def find_peak(list_of_integers):
    """
        find the peak in an unsorted array
        Args:
            list_of_integers
        Return:
            peak
    """
    if len(list_of_integers) == 0:
        return("None")
    else:
        return(max(list_of_integers))
