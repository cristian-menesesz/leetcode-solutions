HashSet<string> _signatures;

    bool ReorderedPowerOf2(int n) {
        string DigitFreq(int x) {
            int[] freq = new int[10];
            while (x > 0) {
                freq[x % 10]++;
                x /= 10;
            }
            return string.Join(",", freq);
        }

        if (_signatures == null) {
            _signatures = new HashSet<string>();
            for (int i = 0; i < 31; i++) {
                _signatures.Add(DigitFreq(1 << i));
            }
        }

        return _signatures.Contains(DigitFreq(n));
    }
