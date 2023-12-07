/*
 * @Author: kingqaquuu
 * @Date: 2023/12/6 14:14
 * @FileName: 3.cpp
 */

#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
const int mod = 1e9 + 7;
using ll = long long;
ll coef[N];
int n, m, to_solve;
string s, tmp;
vector<string> vec;
void solve() {
    stack<map<ll, ll>> expr;
    for (auto& str: vec) {
        if (str.empty()) {continue;}
        if (str[0] == 'x') { // var
            ll index = atoi(str.substr(1).c_str());
            map<ll, ll> tp;
            if (index == to_solve) {
                tp[1] = 1;
            } else {
                tp[0] = coef[index] % mod;
            }
            expr.push(tp);
        } else if (str.size() == 1 && !isdigit(str[0])) { // operator
            auto pre = expr.top(); expr.pop();
            auto suf = expr.top(); expr.pop();
            map<ll, ll> res;
            if (str == "+") {
                for(auto& p: pre) {
                    res[p.first] = (p.second % mod);
                }
                for (auto& p: suf) {
                    res[p.first] = (res[p.first] + p.second) % mod;
                }
            } else if (str == "-") {
                for(auto& p: suf) {
                    res[p.first] = (p.second % mod);
                }
                for (auto& p: pre) {
                    res[p.first] = (res[p.first] - p.second) % mod;
                }
            } else {
                for (auto& p: pre) {
                    for (auto& q: suf) {
                        ll zs = p.first + q.first;
                        ll bs = (p.second * q.second) % mod;
                        res[zs] = (res[zs] + bs) % mod;
                    }
                }
            }
            expr.push(res);
        } else { // digit
            ll digit = atoi(str.c_str());
            digit %= mod;
            map<ll, ll> tp;
            tp[0] = digit;
            expr.push(tp);
        }
    }
    assert(expr.size() == 1);
    ll res = 0;
    while (!expr.empty()) {
        auto final_expr = expr.top();
        expr.pop();
        for (auto& p: final_expr) {
            ll pw = 1;
            ll bs = (p.second * p.first) % mod;
            ll c = p.first - 1;
            while (c > 0) {
                c--;
                pw = (pw * coef[to_solve]) % mod;
            }
            pw = (pw * bs) % mod;
            res = (res + pw) % mod;
        }
    }
    res %= mod;
    res = (res + mod) % mod;
    cout << res << '\n';



}
int main() {
    cin >> n >> m;
    getchar();
    getline(cin, s);
    stringstream ss(s);
    while (getline(ss, tmp, ' ')) {
        vec.push_back(tmp);
    }
    for (int i = 1; i <= m; i++) {
        cin >> to_solve;
        for (int j = 1; j <= n; j++) {
            cin >> coef[j];
        }
        solve();
    }
}