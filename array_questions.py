def find_peak_value(arr):
    n = len(arr)

    if arr[0] >= arr[1]:
        return arr[0]  # If the first element is greater than or equal to its neighbor, it's a peak
    if arr[n-1] >= arr[n-2]:
        return arr[n-1]  # If the last element is greater than or equal to its neighbor, it's a peak
    
    # Iterate through the array to find a peak in the middle
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return arr[i]  # If the element is greater than or equal to its neighbors, it's a peak
    return None  # If no peak is found, return None

# Example usage
arr = [1, 3, 20, 40, 1, 0]
peak = find_peak_value(arr)
if peak is not None:
    print("Peak element:", peak)
else:
    print("No peak element found.")
