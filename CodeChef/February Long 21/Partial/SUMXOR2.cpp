#include<bits/stdc++.h>
#define pb push_back
#define fr(i,j,k) for(int i=j;i<k;i++)
#define frh(i,j,k,h) for(int i=j;i<k;i+=h)
#define MOD 998244353
#define BITS 31

using namespace std;

template<const int mod, const int maxf>
struct NTT {
    int pw;
    int fpow(int a, int k) {
        if (!k) return 1;
        int res = a, tmp = a;
        k--;
        while (k) {
            if (k & 1) {
                res = (long long) res * tmp % mod;
            }
            tmp = (long long) tmp * tmp % mod;
            k >>= 1;
        }
        return res;
    }
    int prt() {
        vector<int> dvs;
        for (int i = 2; i * i < mod; i++) {
            if ((mod - 1) % i) continue;
            dvs.push_back(i);
            if (i * i != mod - 1) dvs.push_back((mod - 1) / i);
        }
        for (int i = 2; i < mod; i++) {
            int flag = 1;
            for (int j = 0; j < dvs.size(); j++) {
                if (fpow(i, dvs[j]) == 1) {
                    flag = 0;
                    break;
                }
            }
            if (flag) return i;
        }
        assert(0);
        return -1;
    }
    NTT() {
        pw = prt();
    }
    void dft(int a[], int pw, int n) {
        for (int m = n, h; h = m / 2, m >= 2; pw = (long long) pw * pw % mod, m = h) {
            for (int i = 0, w = 1; i < h; i++, w = (long long) w * pw % mod) {
                for (int j = i; j < n; j += m) {
                    int k = j + h, x = a[j] - a[k];
                    a[j] += a[k];
                    a[j] -= a[j] >= mod ? mod : 0;
                    a[k] = (long long) w * (x + mod) % mod;
                }
            }
        }
        for (int i = 0, j = 1; j < n - 1; j++) {
            for (int k = n / 2; k > (i ^= k); k /= 2);
            if (j < i) swap(a[i], a[j]);
        }
    }
    int fa[maxf], fb[maxf], fc[maxf];
    void multiply(int a[], int b[], int na, int nb, int c[]) {
        int n = na + nb - 1; while (n != (n & -n)) n += n & -n;
        for (int i = na; i < n; i++) a[i] = 0;
        for (int i = nb; i < n; i++) b[i] = 0;
        int pwn = fpow(pw, (mod - 1) / n);
        dft(a, pwn, n), dft(b, pwn, n);
        for (int i = 0; i < n; i++) fc[i] = (long long) a[i] * b[i] % mod;
        dft(fc, fpow(pwn, mod - 2), n);
        int in = fpow(n, mod - 2);
        for (int i = 0; i < n; i++) fc[i] = (long long) fc[i] * in % mod;
    }
    void multiply(int a[], int b[], int na, int res[]) {
        multiply(a, b, na, na, fc);
        int k = na+1;
        for (int i = 0; i < k; i++) res[i] = fc[i];
    }
};

NTT<MOD, 1 << 18> ntt;
int fact[200001], invfact[200001];
int A[1 << 18] = {};
int B[1 << 18] = {};
int MX;

inline int modadd(int a, int b) {
	int c = a + b;
	if (c >= MOD) c -= MOD;
	return c;
}

inline string toBinary(int n) {
	return bitset<31>(n).to_string(); 
}

inline int pow(long long x, unsigned int y, int p) { 
    int res = 1;     
    x = x % p;
    if (x == 0) return 0;
    while (y > 0) {
        if (y & 1) 
            res = (res*x) % p; 

        y = y>>1;
        x = (x*x) % p; 
    } 
    return res; 
} 

inline int mod_inverse(int x) {
	return pow(x, MOD-2, MOD);
}

inline int nCr(int n, int r) {
	if(n < r) return 0;
	return (long long)((long long)fact[n]*invfact[r]%MOD)*invfact[n-r]%MOD;
}

void compute_ans(int N, int n0s, int ret[]) {
	int len = MX/2;
	int odds[len+2], evens[len+2], multed[len+1];
	
	int j = 0;
	frh(i,1,MX+1,2)
		A[j++] = nCr(N-n0s, i);
	B[0] = nCr(n0s, 0);
	j = 1;
	frh(i,1,MX,2)
		B[j++] = nCr(n0s+1, i+1);
	
	odds[0] = 0;
	ntt.multiply(A, B, len, multed);
	fr(i,0,len+1)
		odds[i+1] = modadd(odds[i], multed[i]);
	
	j = 0;
	frh(i,1,MX+1,2)
		A[j++] = nCr(N-n0s, i);	
	fr(i,0,len+1) B[i] = 0;
	j = 0;
	frh(i,0,MX-1,2)
		B[j++] = nCr(n0s+1, i+1);
	
	evens[0] = 0;
	ntt.multiply(A, B, len, multed);
	fr(i,0,len+1)
		evens[i+1] = modadd(evens[i], multed[i]);
	
	j = 0;
	fr(i,0,len) {
		ret[j++] = odds[i+1];
		ret[j++] = evens[i+1];
	}
}

int main() {
	int N, Q, M, ans, a;
	
	cin>>N;
	MX = N+2+(N%2);
	
	fact[0] = 1;
	fr(i,1,MX)
		fact[i] = (long long)fact[i-1]*i%MOD;

	invfact[MX-1] = mod_inverse(fact[MX-1]);
	for(int i = MX-2; i >= 0; i--)
		invfact[i] = (long long)invfact[i+1]*(i+1)%MOD;
	
	string A[N];
	fr(i,0,N) {
		cin>>a;
		A[i] = toBinary(a);
	}
	
	int C[BITS];
	fr(i,0,BITS) C[i] = 0;
	for(auto a : A)
		fr(i,0,BITS) if(a[i] == '1') C[i]++;
	
	int ht[BITS][MX];
	fr(i,0,BITS)
		compute_ans(N, N-C[i], ht[i]);
	
	cin>>Q;
	fr(q,0,Q) {
		cin>>M;
		ans = 0;
		fr(i,0,BITS)
			ans = (ans + (long long)ht[i][M-1]*pow(2, BITS-1-i, MOD))%MOD;
		cout<<ans<<endl;
	}
}