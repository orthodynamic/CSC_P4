#include <stdio.h>

int game(int);

int main()
{
    int num, winning_num;

    printf("Enter the Number Of matchsticks: ");
    scanf("%d", &num);

    winning_num = game(num);
    if (winning_num == -1)
    {
        printf("It is impossible for A to win the game or atleast winning is not guaranteed");
    }
    else
    {
        printf("Player A need to pick %d match sticks on the first turn to guarantee a win", winning_num);
    }
    
    return 0;
}

int game(int n)
{
    if (n % 5 == 0)
    {
        return -1;
    }
    else
    {
        return (n % 5); 
    }
}
