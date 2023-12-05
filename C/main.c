#include <stdio.h>
#include <string.h>

#define LIST_LIMIT 100
#define CONTACT_LIMIT 25
#define PHONE_LIMIT 13

char contacts[LIST_LIMIT][CONTACT_LIMIT] = {"John M.", "Karen S.", "Kevin C."};
char phone_num[LIST_LIMIT][PHONE_LIMIT] = {"+33612345678", "+33687654321", "+33611223344"};
int length = 3;

int addContact()
{
    if (length >= LIST_LIMIT - 1)
    {
        return 1;
    }

    char name[CONTACT_LIMIT];
    printf("Enter name (e.g. John)\n");
    printf(">> ");
    scanf("\n%[^\n]", name);

    char number[PHONE_LIMIT];
    printf("Enter phone number (e.g. +33612345678)\n");
    printf(">> ");
    scanf("\n%[^\n]", number);

    if (strlen(name) >= CONTACT_LIMIT || strlen(number) >= PHONE_LIMIT)
    {
        return 1;
    }

    strcpy(contacts[length], name);
    strcpy(phone_num[length], number);
    length++;

    return 0;
}

int removeContact() {

    int pos, i;
    printf("Choose the index of the element you want to delete\n>> ");
    scanf("%d", &pos);

    if (pos > length || pos < 0)
    {
        printf("The index %d doesn't exists.", pos);
        return 1;
    }
 
    // use for loop to delete the element and update the index
    for (i = pos; i < length -1; i++)  
    {  
        // arr[i] = arr[i+1]; // assign arr[i+1] to arr[i]
        strcpy(contacts[i+1], contacts[i]);
    }

    for (i = pos; i < length -1; i++)  
    {  
        printf("%s", &contacts[i]);
    }

    return 0;
}

int removeElement ()  
{  
    // declaration of the int type variable  
    int arr[50];  
    int pos, i, num; // declare int type variable  
    printf (" \n Enter the number of elements in an array: \n ");  
    scanf (" %d", &num);  
      
    printf (" \n Enter %d elements in array: \n ", num);  
      
    // use for loop to insert elements one by one in array  
    for (i = 0; i < num; i++ )  
    {   printf (" arr[%d] = ", i);  
        scanf (" %d", &arr[i]);  
    }  
      
    // enter the position of the element to be deleted  
    printf( " Define the position of the array element where you want to delete: \n ");  
    scanf (" %d", &pos);  
      
    // check whether the deletion is possible or not  
    if (pos >= num+1)  
    {  
        printf (" \n Deletion is not possible in the array.");  
    }  
    else  
    {  
        // use for loop to delete the element and update the index  
        for (i = pos - 1; i < num -1; i++)  
        {  
            arr[i] = arr[i+1]; // assign arr[i+1] to arr[i]  
        }  
          
        printf (" \n The resultant array is: \n");  
          
        // display the final array  
        for (i = 0; i< num - 1; i++)  
        {  
            printf (" arr[%d] = ", i);  
            printf (" %d \n", arr[i]);  
        }  
    }  
    return 0;  
}  

int displayContacts()
{
    printf("\n+------------------ CONTACTS -----------------+\n");
    int i;
    for (i = 0; i < length; i++)
    {
        int len = strlen(contacts[i]);
        printf("| %d | %s", i, contacts[i]);
        int j;
        for (j = 0; j < CONTACT_LIMIT - len; j++)
        {
            printf(" ");
        }
        printf("| %s |\n", phone_num[i]);
    }
    printf("+---------------------------------------------+\n\n");

    return 0;
}

int findContact()
{

    char query[CONTACT_LIMIT];
    printf("Enter a search query\n>> ");
    scanf("\n%[^\n]", query);

    int i;
    for (i = 0; i < length; i++)
    {
        if (strcmp(query, contacts[i]) == 0)
        {
            printf("The number of %s is %s.\n", contacts[i], phone_num[i]);
            return 0;
        }
    }
    printf("No contact named %s was found.\n", query);
}

int main()
{
    int leave = -1;
    while (leave != 0)
    {
        printf("+----------------------------+\n");
        printf("|  What do you want to do?   |\n");
        printf("|  0 - Quit                  |\n");
        printf("|  1 - Display contacts      |\n");
        printf("|  2 - Add a new contact     |\n");
        printf("|  3 - Delete a contact      |\n");
        printf("|  4 - Find a contact        |\n");
        printf("+----------------------------+\n");
        printf(">> ");
        scanf("%d", &leave);
        if (leave == 0)
        {
            return 0;
        }
        else if (leave == 1)
        {
            displayContacts();
        }
        else if (leave == 2)
        {
            addContact();
        }
        else if (leave == 3)
        {
            removeContact();
        }
        else if (leave == 4)
        {
            findContact();
        }
    }
    return 0;
}