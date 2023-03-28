#include <iostream>
#include <vector>

std::vector<bool> sieve_of_eratosthenes(int n){

    std::vector<bool> is_prime(n+1, true);
    is_prime[0] = false;
    is_prime[1] = false;

    for(int i = 2 ; i*i <= n ; ++i){
        if(is_prime[i]){
            for(int j = i*i ; j <= n ; j+=i){
                is_prime[j] = false;
            }
        }
    }
    return is_prime;
}

int main(){

    int n = 30;
    std::vector<bool> primes = sieve_of_eratosthenes(n);

    for(int i = 2 ; i<n ; ++i){
        if(primes[i])
            std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}