#include <stdio.h>

int main()
{
    int i, temp;
    int array[5];
    int swap, top = 4, small;

    for (i = 0; i < 5; i++)
    {
        printf("Enter Number %d: ", i+1);
        scanf("%d", &array[i]);
    }
    
    do
    {
        for (i = 0; i < 4; i++)
        {
            swap = 0;

            if (array[i] > array[i+1])
            {
                temp = array[i+1];
                array[i+1] = array[i];
                array[i] = temp;
                
                swap = 1;
            }

        }
        
        top -= 1;
    } while ( swap || top != 0);
   
    small = array[1];

    printf("Second smallest number is: %d", small);
    return 0;
}