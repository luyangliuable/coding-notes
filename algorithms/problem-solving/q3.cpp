vector<string> groupTransactions(vector<string> transactions) {
  vector<string> ans;
  sort(transactions.begin(), transactions.end());
  int cnt = 1;

  for (int i = 1; i < transactions.size(); i++) {
    if (transactions[i] == transactions[i - 1]) {
      cnt++;
    } else {
      ans.push_back(transactions[i - 1] + " " + to_string(cnt));
      cnt = 1;
    }
  }

  ans.push_back(transactions[transactions.size() - 1] + " " + to_string(cnt));

  return ans;
}
