def perfect(number): 

    divisors = list() 
    half = number//2 
    for idx in range(1, half + 1 ): 
        if number % idx == 0: 
            divisors.append(idx) 


    # print('Divisors for {0} are {1} and their sums is {2}'.format(number, divisors, sum(divisors))) 
    return True if sum(divisors) == number else False 


def main(): 
    try: 
        n = int(input("Give Gilbert a range:")) 
        print(list(filter(perfect, range(1, n)))) 

    except ValueError as v: 
        print(v) 
         

if __name__ == '__main__': 
    main() 


'''
    algorithm
        1) find divisors/factors of that number 
        2) add the divisors 
        3) check if the sum == number  
''' 
