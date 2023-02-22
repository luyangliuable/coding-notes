int getWhiteLightLength(int n, int m, vector<vector<int> > lights) {
  vector<pair<int, int> > l1;
  vector<pair<int, int> > l2;
  vector<pair<int, int> > l3;

  for(int i=0; i<m; i++) {
    if(lights[i][0] == 1) {
      l1.push_back(make_pair(lights[i][1],lights[i][2]));
    }
    if(lights[i][0] == 2) {
      l2.push_back(make_pair(lights[i][1],lights[i][2]));
    }
    if(lights[i][0] == 3) {
      l3.push_back(make_pair(lights[i][1],lights[i][2]));
    }
  }

  vector<int> iled;
  iled.resize(n+5);
  for(int i=0; i<n+2; i++) {
    iled[i] = 0;
  }

  sort(l1.begin(), l1.end());
  sort(l2.begin(), l2.end());
  sort(l3.begin(), l3.end());
  int ans = 0;


  for(int i=0; i<l1.size(); i++) {
    if((iled[l1[i].first] & 1) == 0) {
      for(int j=l1[i].first; j<= l1[i].second; j++) {
        if((iled[j] & 1) == 1) {
          break;
        }
        iled[j] |= 1;
      }
    }
    if((iled[l1[i].second] & 1) == 0) {
      for(int j=l1[i].second; j>= l1[i].first; j--) {
        if((iled[j] & 1) == 1) {
          break;
        }
        iled[j] |= 1;
      }
    }
  }

  for(int i=0; i<l2.size(); i++) {
    if((iled[l2[i].first] & 2) == 0) {
      for(int j=l2[i].first; j<= l2[i].second; j++) {
        if((iled[j] & 2) == 1) {
          break;
        }
        iled[j] |= 2;
      }
    }
    if((iled[l2[i].second] & 2) == 0) {
      for(int j=l2[i].second; j>= l2[i].first; j--) {
        if((iled[j] & 2) == 1) {
          break;
        }
        iled[j] |= 2;
      }
    }
  }

  for(int i=0; i<l3.size(); i++) {
    if((iled[l3[i].first] & 4) == 0) {
      for(int j=l3[i].first; j<= l3[i].second; j++) {
        if((iled[j] & 4) == 1) {
          break;
        }
        iled[j] |= 4;
      }
    }
    if((iled[l3[i].second] & 4) == 0) {
      for(int j=l3[i].second; j>= l3[i].first; j--) {
        if((iled[j] & 4) == 1) {
          break;
        }
        iled[j] |= 4;
      }
    }
  }

  for(int i=1; i<=n; i++) {
    if(iled[i] == 7) {
      ans++;
    }
  }
  return ans;


}
