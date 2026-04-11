#include <stdio.h>
#include <string.h>


struct Customer {
    char name[100];
    char mobileNumber[15];
    char idNumber[20];
    char idType[50];       
    char checkInDate[15];
};


void read_string(char *str, int size, char *prompt) {
    printf("%s", prompt);
    fgets(str, size, stdin);

    str[strcspn(str, "\n")] = '\0';
}


int get_valid_input(int min, int max, char *prompt) {
    int choice;

    while (1) {
        printf("%s", prompt);

        if (scanf("%d", &choice) == 1 && choice >= min && choice <= max)
            break;

        printf("\n--- Invalid input. Enter a number between %d and %d. ---\n", min, max);

        while (getchar() != '\n'); 
    }

    while (getchar() != '\n'); 
    return choice;
}


int main(){
    struct Customer C;
    int totalCost = 0;
    int choice = 0;
    int days = 0;
    int finalCost = 0;


     char starNames[3][10] = {"5 star", "3 star", "1 star"};
     int starCosts[] = {2000, 1500, 1000};

     char viewNames[4][20] = {"Sea View", "Mountain View", "Regular View", "Ritual View"};
     int viewCosts[] = {2000, 2500, 1000, 1500};

     char roomNames[4][20] = {"Regular Room", "Modern Room", "Premium Room", "Luxury Room"};
     int roomCosts[] = {1000, 1500, 2000, 2500};

     char bedNames[4][10] = {"1 Bed", "2 Bed", "3 Bed", "4 Bed"};
     int bedCosts[] = {1000, 1500, 2000, 2500};

     char foodNames[2][20] = {"No Food", "All-inclusive Food"};
     int foodCosts[] = {0, 2000};

     char extraNames[4][25] = {"No Service", "Swimming Pool service", "Gym access", "Pool & Gym access"};
     int extraCosts[] = {0, 1000, 1000, 2000}; 

     char *selectedStar = NULL;
     char *selectedView = NULL;
     char *selectedRoom = NULL;
     char *selectedBed = NULL;
     char *selectedFood = NULL;
     char *selectedExtra = NULL;

    printf("===========================================\n");
    printf("----WELCOME TO THE HOTEL BOOKING SYSTEM----\n");
    printf("===========================================\n\n");

    
    printf("--- 🧑 Customer Details ---\n");
    read_string(C.name, sizeof(C.name), "Enter your full name: "); 
    read_string(C.mobileNumber, sizeof(C.mobileNumber), "Enter your mobile number: "); 
    read_string(C.idType, sizeof(C.idType), "Enter ID Type (e.g., Passport, License): "); 
    read_string(C.idNumber, sizeof(C.idNumber), "Enter your ID number: "); 
    read_string(C.checkInDate, sizeof(C.checkInDate), "Enter Check-in Date(DD/MM/YYYY): ");
    printf("\n\n");
    
    
    printf("--- 🏨 Hotel Star Rating ---\n");
    printf("Dear Customer **%s**! Which type of Hotel you prefer to book:\n", C.name);
    printf("1. %s (Base Cost: %d)\n", starNames[0], starCosts[0]);
    printf("2. %s (Base Cost: %d)\n", starNames[1], starCosts[1]);
    printf("3. %s (Base Cost: %d)\n", starNames[2], starCosts[2]);
    choice = get_valid_input(1, 3, "Please enter 1, 2, or 3: ");
    selectedStar = starNames[choice - 1];
    totalCost += starCosts[choice - 1];
    printf("\nYou chose a **%s** hotel. Base cost added: %d\n", selectedStar, starCosts[choice - 1]);
    printf("Your current total cost (per 24 hours) is: %d\n\n", totalCost);
    
    
    printf("--- 🏞️ Hotel View Selection ---\n");
    printf("Which type of view you want in your hotel ?\n");
    printf("1. %s (Extra Cost: %d)\n", viewNames[0], viewCosts[0]);
    printf("2. %s (Extra Cost: %d)\n", viewNames[1], viewCosts[1]);
    printf("3. %s (Extra Cost: %d)\n", viewNames[2], viewCosts[2]);
    printf("4. %s (Extra Cost: %d)\n", viewNames[3], viewCosts[3]);
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedView = viewNames[choice - 1];
    totalCost += viewCosts[choice - 1];
    printf("\nYou chose a **%s**. Cost added: %d\n", selectedView, viewCosts[choice - 1]);
    printf("Your current total cost (per 24 hours) is: %d\n\n", totalCost);
    
    
    printf("--- 🛌 Room Type Selection ---\n");
    printf("Which type of room do you want?\n");
    printf("1. %s (Extra Cost: %d)\n", roomNames[0], roomCosts[0]);
    printf("2. %s (Extra Cost: %d)\n", roomNames[1], roomCosts[1]);
    printf("3. %s (Extra Cost: %d)\n", roomNames[2], roomCosts[2]);
    printf("4. %s (Extra Cost: %d)\n", roomNames[3], roomCosts[3]);
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedRoom = roomNames[choice - 1];
    totalCost += roomCosts[choice - 1];
    printf("\nYou chose a **%s**. Cost added: %d\n", selectedRoom, roomCosts[choice - 1]);
    printf("Your current total cost (per 24 hours) is: %d\n\n", totalCost);


    printf("--- 🛏️ Bed Count Selection ---\n");
    printf("How many beds do you need for the room?\n");
    printf("1. %s (Extra Cost: %d)\n", bedNames[0], bedCosts[0]);
    printf("2. %s (Extra Cost: %d)\n", bedNames[1], bedCosts[1]);
    printf("3. %s (Extra Cost: %d)\n", bedNames[2], bedCosts[2]);
    printf("4. %s (Extra Cost: %d)\n", bedNames[3], bedCosts[3]);
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedBed = bedNames[choice - 1];
    totalCost += bedCosts[choice - 1];
    printf("\nYou chose a **%s** room. Cost added: %d\n", selectedBed, bedCosts[choice - 1]);
    printf("Your current total cost (per 24 hours) is: %d\n\n", totalCost);


    printf("--- 🍽️ Food Option Selection ---\n");
    printf("Do you want an all-inclusive food package?\n");
    printf("1. %s (Extra Cost: %d)\n", foodNames[0], foodCosts[0]);
    printf("2. %s (Extra Cost: %d)\n", foodNames[1], foodCosts[1]);
    choice = get_valid_input(1, 2, "Please enter 1 or 2: ");
    selectedFood = foodNames[choice - 1];
    totalCost += foodCosts[choice - 1];
    printf("\nYou chose **%s**. Cost added: %d\n", selectedFood, foodCosts[choice - 1]);
    printf("Your current total cost (per 24 hours) is: %d\n\n", totalCost);
    

    printf("--- ✨ Extra Service Selection ---\n");
    printf("Do you want any extra service?\n");
    printf("1. %s (Extra Cost: %d)\n", extraNames[0], extraCosts[0]);
    printf("2. %s (Extra Cost: %d)\n", extraNames[1], extraCosts[1]);
    printf("3. %s (Extra Cost: %d)\n", extraNames[2], extraCosts[2]);
    printf("4. %s (Extra Cost: %d)\n", extraNames[3], extraCosts[3]);
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedExtra = extraNames[choice - 1];
    totalCost += extraCosts[choice - 1];
    printf("\nYou chose **%s**. Cost added: %d\n", selectedExtra, extraCosts[choice - 1]);
    printf("Your current total cost (per 24 hours) is: %d\n\n", totalCost);


    printf("For how many days you want to book hotel?\n");
    scanf("%d" , &days);
    finalCost = days * totalCost;

    printf("\n==========================================\n");
    printf("✅ BOOKING CONFIRMATION\n");
    printf("   Check-in Date: %s\n", C.checkInDate);
    printf("   Total Days Booked: %d\n", days);
    printf("   Daily Cost: %d\n", totalCost);
    printf("   FINAL COST: %d\n", finalCost);
    printf("==========================================\n");

    FILE *fp;
    fp = fopen("bookings.txt", "a"); 

    if (fp == NULL) {
        printf("\nERROR: Could not open 'bookings.txt' for writing.\n");
        return 1;
    }

    fprintf(fp, "==========================================\n");
    fprintf(fp, "       NEW HOTEL BOOKING                  \n");
    fprintf(fp, "==========================================\n");

    fprintf(fp, "Customer Name: %s\n", C.name);
    fprintf(fp, "Mobile Number: %s\n", C.mobileNumber);
    fprintf(fp, "ID Type:       %s\n", C.idType);    
    fprintf(fp, "ID Number:     %s\n", C.idNumber);
    fprintf(fp, "Check-in Date: %s\n", C.checkInDate);

    fprintf(fp, "\n--- Booking Summary ---\n");
    fprintf(fp, "Star Rating:        %s\n", selectedStar);
    fprintf(fp, "View Type:          %s\n", selectedView);
    fprintf(fp, "Room Type:          %s\n", selectedRoom);
    fprintf(fp, "Bed Count:          %s\n", selectedBed);
    fprintf(fp, "Food Option:        %s\n", selectedFood);
    fprintf(fp, "Extra Services:     %s\n", selectedExtra);
    fprintf(fp, "Daily Cost:         %d\n", totalCost);
    fprintf(fp, "Total Days Booked:  %d\n", days); 
    fprintf(fp, "FINAL BOOKING COST: %d\n", finalCost);
    fprintf(fp, "==========================================\n\n\n\n");

    fclose(fp);

    printf("Booking confirmed\n");
    return 0;
}
