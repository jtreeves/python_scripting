with open('prime.txt', 'r') as primes:
    prime_list = primes.readlines()
    double_prime_list = []
    for each_prime in range(len(prime_list)):
        double_prime_list[each_prime] = str(int(prime_list[each_prime * 2]))
    double_prime_file = open('double_prime.txt', 'r+')
    double_prime_file.write('\n'.join(double_prime_list))
    double_prime_file.close()


def multiply_by_two(num):
  return num * 2

with open('prime_numbers.txt') as prime_numbers_file:
  prime_numbers = prime_numbers_file.readlines()
  for num in prime_numbers:
    print(multiply_by_two(int(num)))
    
with open('one_to_hundred.txt') as numbers_file:
  list_of_numbers = numbers_file.readlines()
  result = []
  
  for num_txt in list_of_numbers:
    if 'Five' in num_txt:
      remove_newline_txt = num_txt[:-1]
      # print(remove_newline_txt)
      result.append(remove_newline_txt)
    elif 'Fifteen' in num_txt:
      remove_newline_txt = num_txt[:-1]
      # print(remove_newline_txt)
      result.append(remove_newline_txt)
  print(result)