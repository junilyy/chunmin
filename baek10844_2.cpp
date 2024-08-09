#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int k = 1000000000;

int N;
int ans = 0;
int c;

int stair(int a, int b){
        
        if(a == 1){
            if(b == 0) return 0;
            else return 1;
        }
        
        else{
            if(b == 0){
                c = stair(a-1, 1);
            }
            else if(b == 9){
                c = stair(a-1, 8);
            }
            else c = stair(a-1, b-1) + stair(a-1, b+1);
            
            return c;
        }              
    }


int main() {
    cin >> N;
    for (int i = 0; i <= 9; i++){
        ans += stair(N, i);
    }
    ans %= k;

    cout << ans << '\n';

	return 0;
}