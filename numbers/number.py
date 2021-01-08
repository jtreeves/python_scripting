with open('prime.txt', 'r') as primes:
    prime_list = primes.readlines()
    double_prime_list = []
    for each_prime in range(len(prime_list)):
        double_prime_list[each_prime] = str(int(prime_list[each_prime * 2]))
    double_prime_file = open('double_prime.txt', 'r+')
    double_prime_file.write('\n'.join(double_prime_list))
    double_prime_file.close()