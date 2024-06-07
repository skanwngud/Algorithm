// 유효한 팰린드롬
// 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

#include <iostream>
#include <string>

int main(int argc, char *argv[])
{
    if (argc <= 1)
    {
        std::cerr << "you must input string, just one more" << std::endl;
        return 0;
    }

    bool result = true;

    std::string inp, reInp;

    inp = argv[1];

    // 입력받은 string 에서 대소문자와 숫자만 남김
    for (int i = 0; i < inp.length(); i++)
    {
        if (isalpha(inp[i]))  // 문자인 경우 소문자 변환 후 신규 스트링에 추가
        {
            inp[i] = tolower(inp[i]);  // 일괄적으로 소문자 변환
            reInp.push_back(inp[i]);
        }

        else if (isnumber(inp[i]))  // 숫자인 경우 신규 스트링에 추가
        {
            reInp.push_back(inp[i]);
        }
    }

    for (int i = 0; i < reInp.length() - 1; i++)  // 문자열의 가장 끝은 무조건 공백 (\0) 이므로 한 칸 더 앞으로
    {
        if (reInp[i] != reInp[reInp.length() - 1 - i])  // 스트링의 처음과 끝을 순회하며 비교
        {
            result = false;
            break;
        }
    }

    return result;
}