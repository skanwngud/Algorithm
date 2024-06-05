#include <string>
#include <vector>

#include <numeric>

#include <iostream>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    
    vector<int> odd;
    vector<int> even;

    int cnt = 0;

    for (auto &num: num_list)
    {
        ++cnt;

        if ((int)cnt % 2 == 1)
        {
            odd.push_back(num);
        }

        else
        {
            even.push_back(num);
        }
    }

    int odd_sum = accumulate(odd.begin(), odd.end(), 0);
    int even_sum = accumulate(even.begin(), even.end(), 0);

    answer = (odd_sum > even_sum) ? odd_sum : even_sum;

    return answer;
}