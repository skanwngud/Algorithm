#include <iostream>
#include <string>

int main(void)
{
    int iter;
    std::string res;

    std::cin >> iter;

    for (int i = 0; i < iter; i++)
    {
        res += " ";
    }

    for (int i = res.length() - 1; i > -1; --i)
    {
        res[i] = '*';
        std::cout << res << std::endl;
    }

    return 0;
}