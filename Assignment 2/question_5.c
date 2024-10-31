 #include <stdio.h>

int main()
{
    int n, i, j, length, largest;

    printf("Enter Number of values: ");
    scanf("%d", &n);

    int array[n];

    for (i = 0; i < n; i++)
    {
        printf("Enter Number %d: ", i+1);
        scanf("%d", &array[i]);
    }
    
    printf("\n----Horizontal Histogram----\n");
    printf("\n");
    for (i = 0; i < n; i++)
    {   
        printf("%d ", array[i]);
        length = array[i];
        for (j = 0; j < length; j++)
        {
            printf("* ");
        }
        printf("\n");
    }

    printf("\n----Vertical Histogram----\n");
    printf("\n");

    largest = array[0];
    for (i = 0; i < n; i++)
    {
        if (array[i] > largest)
        {
            largest = array[i];
        }
        
    }

    for (i = largest; i > 0; i--)
    {

        for (j = 0; j < n; j++)
        {
            if (array[j] >= i)
            {
                printf("* ");
            }
            else
            {
                printf("  ");
            }
            
        }
        printf("\n");
    }
    for (i = 0; i < n; i++)
    {
        printf("%d ", array[i]);
    }
    
    
    return 0;
}
