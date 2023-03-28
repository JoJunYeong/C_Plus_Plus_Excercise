
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j] = False

    return is_prime


def main():
    n = 300
    primes = sieve_of_eratosthenes(n)
    for i in range(n):
        if primes[i]:
            print(i,"")



if __name__ == "__main__":
    main()