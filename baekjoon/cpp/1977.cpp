#include <iostream>
#include <math.h>

int main(void)
{
    int M, N, n, min, sum;
    double m;

    std::cin >> M >> N;

    m = std::sqrt(M);
    n = std::sqrt(N);

    if(m > (int)m)
    {
        m = (int)m + 1;
    }

    else if(m == (int)m)
    {
        m = (int)m;
    }

    if(m > n)
    {
        std::cout << -1 << std::endl;
        return 0;
    }

    for(int i = m; i < n + 1; i++)
    {
        sum += std::pow(i, 2);
    }

    min = std::pow(m, 2);

    return 0;
}