#include <bits/stdc++.h>
#define ll long long
#define vi vector<long long>
#define vb vector<bool>
#define si set<long long>
#define sb set<bool>
#define ss set<string>
#define vs vector<string>
#define msi map<string, long long>
#define mci map<char, long long>
#define mss map<string, string>
#define msb map<string, bool>
#define REP(i,a,b) for (int i = a; i < b; i++)
#define MAX 50
using namespace std;
ll start;
ll ans = 0;
void sol(ll n, ll pai, vi seq[], ll pais[]){
    if(seq[n].empty() && n == start) return;
    if(seq[n].empty()) {ans++; sol(pai, pais[pai], seq, pais);return;}

    pais[n] = pai;
    ll prox = seq[n].back();
    seq[n].pop_back();
    if(prox == pai && !seq[n].empty()){
        prox = seq[n].back();
        seq[n].pop_back();
    }
    if(prox == pai && seq[n].empty()){
        ans++; sol(pai, pais[pai], seq, pais);return;
    }

    ans++;
    sol(prox, n, seq, pais);
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t; cin >> t;
    REP(i, 0, t){
        si seqfake[MAX];
        ll pais[MAX];
        ll n; cin >> n;
        ll v, a; cin >> v >> a;
        REP(j, 0, a){
            ll n1, n2; cin >> n1 >> n2;
            seqfake[n1].insert(n2);
            seqfake[n2].insert(n1);
        }

        vi seq[MAX];
        REP(k, 0, v){
            for(auto num: seqfake[k]){
                seq[k].push_back(num);
            }
        }
        start = n;
        sol(n, -1, seq, pais);
        cout << ans << "\n";
        ans = 0;
    }

    return 0;
}
