int mySqrt(int x) {
    if (x == 0 || x == 1)
        return x;

    int begin = 1, end = x, result;
    
    while (begin <= end) {
        int mid = begin + (end - begin) / 2;

        if (mid <= x / mid) {
            result = mid;
            begin = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return result;
}
