#include<bits/stdc++.h>
#define fr(i,j,k) for(int i=j; i<k; i++)
#define frh(i,j,k,h) for(int i=j; i<k; i+=h)
#define MOD 998244353
#define BITS 32
#define MX 412345
using namespace std;

template<const int mod, const int maxf>
struct NTT {
    int rts[maxf + 1];
    int bitrev[maxf];
    int iv[maxf + 1];

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
        int k = 0; while ((1 << k) < maxf) k++;
        bitrev[0] = 0;
        for (int i = 1; i < maxf; i++) {
            bitrev[i] = bitrev[i >> 1] >> 1 | ((i & 1) << k - 1);
        }
        int pw = fpow(prt(), (mod - 1) / maxf);
        rts[0] = 1;
        for (int i = 1; i <= maxf; i++) {
            rts[i] = (long long) rts[i - 1] * pw % mod;
        }
        for (int i = 1; i <= maxf; i <<= 1) {
            iv[i] = fpow(i, mod - 2);
        }
    }
    void dft(int a[], int n, int sign) {
        int d = 0; while ((1 << d) * n != maxf) d++;
        for (int i = 0; i < n; i++) {
            if (i < (bitrev[i] >> d)) {
                swap(a[i], a[bitrev[i] >> d]);
            }
        }
        for (int len = 2; len <= n; len <<= 1) {
            int delta = maxf / len * sign;
            for (int i = 0; i < n; i += len) {
                int *w = sign > 0 ? rts : rts + maxf;
                for (int k = 0; k + k < len; k++) {
                    int &a1 = a[i + k + (len >> 1)], &a2 = a[i + k];
                    int t = (long long) *w * a1 % mod;
                    a1 = a2 - t;
                    a2 = a2 + t;
                    a1 += a1 < 0 ? mod : 0;
                    a2 -= a2 >= mod ? mod : 0;
                    w += delta;
                }
            }
        }
        if (sign < 0) {
            int in = iv[n];
            for (int i = 0; i < n; i++) {
                a[i] = (long long) a[i] * in % mod;
            }
        }
    }
    void multiply(int a[], int b[], int na, int nb, int c[]) {
        static int fa[maxf], fb[maxf];
        int n = na + nb - 1; while (n != (n & -n)) n += n & -n;
        for (int i = 0; i < n; i++) fa[i] = fb[i] = 0;
        for (int i = 0; i < na; i++) fa[i] = a[i];
        for (int i = 0; i < nb; i++) fb[i] = b[i];
        dft(fa, n, 1), dft(fb, n, 1);
        for (int i = 0; i < n; i++) fa[i] = (long long) fa[i] * fb[i] % mod;
        dft(fa, n, -1);
        for (int i = 0; i < n; i++) c[i] = fa[i];
    }
    vector<int> multiply(vector<int> a, vector<int> b) {
        static int fa[maxf], fb[maxf], fc[maxf];
        int na = a.size(), nb = b.size();
        for (int i = 0; i < na; i++) fa[i] = a[i];
        for (int i = 0; i < nb; i++) fb[i] = b[i];
        multiply(fa, fb, na, nb, fc);
        int k = na + nb - 1;
        vector<int> res(k);
        for (int i = 0; i < k; i++) res[i] = fc[i];
        return res;
    }
};

NTT<MOD, 1 << 18> ntt;
int Q, N, M;
int A[MX], B[MX], C[BITS], odds[MX], evens[MX], fact[MX], invfact[MX], multed[MX];

inline int modadd(int a, int b) {
	int c = a + b;
	if (c >= MOD) c -= MOD;
	return c;
}

inline int modmul(int a, int b) {
	return (a * 1LL * b) % MOD;
}

inline int pow(int x, int y) { 
    int res = 1;     
    while(y) {
		if(y & 1)
			res = modmul(res, x);
		x = modmul(x, x);
		y >>= 1;
	}
	return res;
} 

inline int nCr(int n, int r) {
	if(n < r) return 0;
	return modmul(modmul(fact[n], invfact[n-r]), invfact[r]);
}

int main() {
    cin >> N;
    fact[0] = 1;
    fr(i,1,N+1) {
        fact[i] = modmul(fact[i-1], i);
    }
    invfact[N] = pow(fact[N], MOD-2);
    for(int i = N-1; i >= 0; i--) {
        invfact[i] = modmul(invfact[i+1], i+1);
    }
    fr(c,1,N+1) {
        int a;
        cin >> a;
        fr(i,0,BITS) if(a & (1 << i)) C[i]++;
    }
    fr(i,0,BITS) {
        int ja = 0, jb = 1, jo, je, pow2 = pow(2, i);
		frh(k,1,C[i]+1,2) A[ja++] = nCr(C[i], k);
		B[0] = nCr(N-C[i], 0);
		frh(k,1,N-C[i]+1,2) B[jb++] = nCr(N-C[i]+1, k+1);
		ntt.multiply(A, B, ja, jb, odds);
		
		jo = ja+jb-1;
		jb = 0;
		frh(k,1,N-C[i]+2,2) B[jb++] = nCr(N-C[i]+1, k);
		ntt.multiply(A, B, ja, jb, evens);
		
		je = ja+jb-1;
		fr(k,1,jo) odds[k] = modadd(odds[k], odds[k-1]);
		fr(k,1,je) evens[k] = modadd(evens[k], evens[k-1]);
		
		fr(k,0,jo) multed[k*2 + 1] = modadd(multed[k*2 + 1], modmul(pow2, odds[k]));
		fr(k,0,je) multed[(k+1)*2] = modadd(multed[(k+1)*2], modmul(pow2, evens[k]));
    }
    cin >> Q;
    while(Q--) {
        cin>>M;
        cout<<multed[M]<<endl;
    }
}