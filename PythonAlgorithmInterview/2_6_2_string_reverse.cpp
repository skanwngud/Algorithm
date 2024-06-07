#include <iostream>
#include <string>
#include <vector>

int main(void)
{
    // char inp[] = { 'h', 'e', 'l', 'l', 'o'};
    char inp[] = {'H', 'a', 'n', 'n', 'a', 'h'};

    char temp;

    std::cout << inp << std::endl;

    for (int i = 0; i < (int)(sizeof(inp) / 2); i++)
    {
        temp = inp[i];
        inp[i] = inp[(int)(sizeof(inp) - 1 - i)];
        
        inp[(int)(sizeof(inp) - 1 - i)] = temp;
    }

    std::cout << inp << std::endl;

    return 0;
}