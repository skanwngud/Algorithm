#include <iostream>
#include <string>

int main(void)
{
    std::string id;

    std::cin >> id;
    id.append("??!");

    std::cout << id << std::endl;

    return 0;
}