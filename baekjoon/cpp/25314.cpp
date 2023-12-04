#include <iostream>
#include <string>

int main(void)
{
    int N;
    std::cin >> N;

    std::string answer;

    for (int i = 0; i < (int)(N / 4); i++)
    {
        answer += "long ";
    }

    answer += "int";

    std::cout << answer << std::endl;

    return 0;
}