#include <iostream>
#include <cmath>
using namespace std;

int k = 1000000000;

int N;
int a[9][101];
int ans = 0;

int main() {
    cin >> N;
    for(int i = 1; i <= 9; i++) {
        a[i][1] = 1;
    }
    for(int i = 2; i <= N; i++) {
        for(int j =0; j <= 9; j++)
        {
            if(j==0) {
                a[j][i] = a[1][i-1];
            }
            else if(j== 9) {  
                a[j][i] = a[8][i-1];
            }
            else {
                a[j][i] += a[j-1][i-1];
                a[j][i] += a[j+1][i-1];
            }
            a[j][i] %= k;
        }
    }

    for(int i = 0; i <= 9; i++) {
        ans += a[i][N];
        ans %= k;
    }
    
    cout << ans << '\n';

	return 0;
}