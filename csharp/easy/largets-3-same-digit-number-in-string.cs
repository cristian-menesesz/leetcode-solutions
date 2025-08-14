string LargestGoodInteger(string num)
    {
        int count = 1;
        int ans = -1;

        for (int i = 1; i < num.Length; i++)
        {
            if (num[i] == num[i - 1])
            {
                count++;
                if (count == 3)
                {
                    ans = Math.Max(ans, num[i] - '0');
                }
            }
            else
            {
                count = 1;
            }
        }

        return ans != -1 ? new string((char)('0' + ans), 3) : "";
    }
