#include <iostream>
#include <string>

int main(void)
{
    int hour, minute, after;
    
    std::cin >> hour >> minute;
    std::cin >> after;

    minute += after;
    if (minute > 59)
    {
        int loop = (int)minute / 60;
        minute -= 60 * loop;
        hour += loop;

        if (hour > 23)
        {
            hour -= 24;
        };
    };

    std::cout << hour << " " << minute << std::endl;

    return 0;
}