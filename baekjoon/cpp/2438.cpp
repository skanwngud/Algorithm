#include <iostream>
#include <string>

int main(void)
{
    int iter;
    std::string res;

    std::cin >> iter;

    for (int i = 0; i < iter; i++)
    {
        res += '*';
        std::cout << res << std::endl;
    }

    return 0;
}