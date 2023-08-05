#include <iostream>

int FindBiggest(int a, int b, int c)
{
    int max;

    if (a > b && a > c) max = a;
    else if (a > b && a < c) max = c;
    else if (a < b && b > c) max = b;
    else if (a < b && b < c) max = c;

    return max;
}

int FindSame(int front, int middle, int rear)
{

    if (front == middle && front == rear)
    {
        return 10000 + front * 1000;
    }

    else if (front == middle && middle != rear)
    {
        return 1000 + front * 100;
    }

    else if (front != middle && middle == rear)
    {
        return 1000 + middle * 100;
    }

    else if (front != middle && middle != rear && front == rear)
    {
        return 1000 + front * 100;
    }

    else
    {
        int biggest = FindBiggest(front, middle, rear);
        return 100 * biggest;
    }
}

int main(void)
{
    int a, b, c, res;

    std::cin >> a >> b >> c;

    res = FindSame(a, b, c);

    std::cout << res << std::endl;

    // 같은 눈 3개 10, 000원 + (같은 눈) * 1000
    // 같은 눈 2개 1, 000원 + (같은 눈) * 100
    // 같은 눈 1개 (가장 큰 눈) * 100

    return 0;
}