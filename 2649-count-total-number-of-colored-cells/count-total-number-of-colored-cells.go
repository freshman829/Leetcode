func coloredCells(n int) int64 {
    sum := 0
    if n == 1 {
        return 1
    }
    for i := 1; i <= 2 * n - 3; i+= 2 {
        sum += i
    }
    println(sum)
    return int64(sum * 2 + 2 * n - 1)
}