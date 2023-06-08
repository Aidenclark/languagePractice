function isMatch(s, p) {
  const m = s.length;
  const n = p.length;

  // Create a 2D DP table
  const dp = new Array(m + 1);
  for (let i = 0; i <= m; i++) {
    dp[i] = new Array(n + 1).fill(false);
  }

  // Base case: an empty pattern matches an empty string
  dp[0][0] = true;

  // Handle the case when s is empty but p has '*'
  for (let j = 1; j <= n; j++) {
    if (p[j - 1] === '*') {
      dp[0][j] = dp[0][j - 2];
    }
  }

  // Fill the DP table
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (p[j - 1] === s[i - 1] || p[j - 1] === '.') {
        dp[i][j] = dp[i - 1][j - 1];
      } else if (p[j - 1] === '*') {
        dp[i][j] = dp[i][j - 2];
        if (p[j - 2] === s[i - 1] || p[j - 2] === '.') {
          dp[i][j] |= dp[i - 1][j];
        }
      }
    }
  }

  return dp[m][n];
}
