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
using namespace std;

vi colunas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};
queue<ll> fila;

ll busca(char e){
    REP(i, 0, 8){
        if (colunas[i] == e){
            return i;
        }
    }
    return -1;   
}

bool bfs(ll x, ll y, ll mov, ll l_f, ll c_f, bool marcados[8][8]){
    if(x < 0 or x >= 8) return false;
    if(y < 0 or y >= 8) return false;
    if(marcados[x][y]) return false;
    if(x == c_f && y == l_f) return true;
    marcados[x][y] = true;

    fila.push(x + 1);
    fila.push(y + 2);
    fila.push(mov + 1);
    fila.push(x - 1);
    fila.push(y + 2);
    fila.push(mov + 1);
    fila.push(x + 2);
    fila.push(y + 1);
    fila.push(mov + 1);
    fila.push(x - 2);
    fila.push(y + 1);
    fila.push(mov + 1);
    fila.push(x + 1);
    fila.push(y - 2);
    fila.push(mov + 1);
    fila.push(x - 1);
    fila.push(y - 2);
    fila.push(mov + 1);
    fila.push(x + 2);
    fila.push(y - 1);
    fila.push(mov + 1);
    fila.push(x - 2);
    fila.push(y - 1);
    fila.push(mov + 1);
    return false;

}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    string c1, c2;

    while (cin >> c1){
        cin >> c2;
        bool grafo[8][8] = {false};
        ll coluna1 = busca(c1[0]);
        ll linha1 = c1[1] - '0' - 1;
        ll coluna2 = busca(c2[0]);
        ll linha2 = c2[1] - '0' - 1;

        fila.push(coluna1);
        fila.push(linha1);
        fila.push(0);
        
        while (true){
            ll c = fila.front();
            fila.pop();
            ll l = fila.front();
            fila.pop();
            ll mov = fila.front();
            fila.pop();
            if (bfs(c, l, mov, linha2, coluna2, grafo)){
                cout << "To get from " << c1 << " to " << c2 << " takes " << mov << " knight moves." << "\n";
                fila = {};
                break;
            }
        }


    }

    return 0;
}
