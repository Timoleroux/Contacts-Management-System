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
            printf("Remove\n");
        }
        else if (leave == 4)
        {
            findContact();
        }
    }
    return 0;
}