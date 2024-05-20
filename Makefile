compile:
	gcc -g -Wall -pedantic-errors AppleHeartRateConverter.c -o AppleHeartRateConverter.out

run:
	./AppleHeartRateConverter.out 5

clean:
	rm *.out