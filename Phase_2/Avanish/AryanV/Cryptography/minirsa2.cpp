#include <iostream>
#include <cmath>
using namespace std;
 
// calculate phi(n) for a given number n
int phi(int n) {
   int result = n;
   for (int i = 2; i <= sqrt(n); i++) {
       if (n % i == 0) {
           while (n % i == 0) {
               n /= i;
           }
           result -= result / i;
       }
   }
   if (n > 1) {
       result -= result / n;
   }
   return result;
}
 
// calculate gcd(a, b) using the Euclidean algorithm
int gcd(int a, int b) {
   if (b == 0) {
       return a;
   }
   return gcd(b, a % b);
}
 
// calculate a^b mod m using modular exponentiation
int modpow(int a, int b, int m) {
   int result = 1;
   while (b > 0) {
       if (b & 1) {
           result = (result * a) % m;
       }
       a = (a * a) % m;
       b >>= 1;
   }
   return result;
}
 
// generate a random primitive root modulo n
int generatePrimitiveRoot(int n) {
   int phiN = phi(n);
   int factors[phiN], numFactors = 0;
   int temp = phiN;
   // get all prime factors of phi(n)
   for (int i = 2; i <= sqrt(temp); i++) {
       if (temp % i == 0) {
           factors[numFactors++] = i;
           while (temp % i == 0) {
               temp /= i;
           }
       }
   }
   if (temp > 1) {
       factors[numFactors++] = temp;
   }
   // test possible primitive roots
   for (int i = 2; i <= n; i++) {
       bool isRoot = true;
       for (int j = 0; j < numFactors; j++) {
           if (modpow(i, phiN / factors[j], n) == 1) {
               isRoot = false;
               break;
           }
       }
       if (isRoot) {
           return i;
       }
   }
   return -1;
}
 
int main() {
   int p = 61;
   int q = 53;
   int n = p * q;
   int phiN = (p - 1) * (q - 1);
   int e = generatePrimitiveRoot(phiN);
   int d = 0;
   while ((d * e) % phiN != 1) {
       d++;
   }
   cout << "Public key: {" << e << ", " << n << "}" << endl;
   cout << "Private key: {" << d << ", " << n << "}" << endl;
   int m = 123456;
   int c = modpow(m, e, n);
   int decrypted = modpow(c, d, n);
   cout << "Original message: " << m << endl;
   cout << "Encrypted message: " << c << endl;
   cout << "Decrypted message: " << decrypted << endl;
   return 0;
}