#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Customer {
    string name;
    string mobileNumber;
    string idNumber;
    string idType;       
    string checkInDate;
};

void read_string(string &str, string prompt) {
    cout << prompt;
    getline(cin, str);
}

int get_valid_input(int min, int max, string prompt) {
    int choice;

    while (1) {
        cout << prompt;

        if (cin >> choice && choice >= min && choice <= max)
            break;

        cout << "\n--- Invalid input. Enter a number between " << min << " and " << max << ". ---\n";

        cin.clear();
        cin.ignore(1000, '\n');
    }

    cin.ignore(1000, '\n');
    return choice;
}

int main(){
    Customer C;
    int totalCost = 0;
    int choice = 0;
    int days = 0;
    int finalCost = 0;

    string starNames[3] = {"5 star", "3 star", "1 star"};
    int starCosts[] = {2000, 1500, 1000};

    string viewNames[4] = {"Sea View", "Mountain View", "Regular View", "Ritual View"};
    int viewCosts[] = {2000, 2500, 1000, 1500};

    string roomNames[4] = {"Regular Room", "Modern Room", "Premium Room", "Luxury Room"};
    int roomCosts[] = {1000, 1500, 2000, 2500};

    string bedNames[4] = {"1 Bed", "2 Bed", "3 Bed", "4 Bed"};
    int bedCosts[] = {1000, 1500, 2000, 2500};

    string foodNames[2] = {"No Food", "All-inclusive Food"};
    int foodCosts[] = {0, 2000};

    string extraNames[4] = {"No Service", "Swimming Pool service", "Gym access", "Pool & Gym access"};
    int extraCosts[] = {0, 1000, 1000, 2000}; 

    string selectedStar, selectedView, selectedRoom, selectedBed, selectedFood, selectedExtra;

    cout << "===========================================\n";
    cout << "----WELCOME TO THE HOTEL BOOKING SYSTEM----\n";
    cout << "===========================================\n\n";

    cout << "--- 🧑 Customer Details ---\n";
    read_string(C.name, "Enter your full name: "); 
    read_string(C.mobileNumber, "Enter your mobile number: "); 
    read_string(C.idType, "Enter ID Type (e.g., Passport, License): "); 
    read_string(C.idNumber, "Enter your ID number: "); 
    read_string(C.checkInDate, "Enter Check-in Date(DD/MM/YYYY): ");
    cout << "\n\n";

    cout << "--- 🏨 Hotel Star Rating ---\n";
    cout << "Dear Customer **" << C.name << "**! Which type of Hotel you prefer to book:\n";
    cout << "1. " << starNames[0] << " (Base Cost: " << starCosts[0] << ")\n";
    cout << "2. " << starNames[1] << " (Base Cost: " << starCosts[1] << ")\n";
    cout << "3. " << starNames[2] << " (Base Cost: " << starCosts[2] << ")\n";
    choice = get_valid_input(1, 3, "Please enter 1, 2, or 3: ");
    selectedStar = starNames[choice - 1];
    totalCost += starCosts[choice - 1];
    cout << "\nYou chose a **" << selectedStar << "** hotel. Base cost added: " << starCosts[choice - 1] << "\n";
    cout << "Your current total cost (per 24 hours) is: " << totalCost << "\n\n";

    cout << "--- 🏞️ Hotel View Selection ---\n";
    cout << "Which type of view you want in your hotel ?\n";
    cout << "1. " << viewNames[0] << " (Extra Cost: " << viewCosts[0] << ")\n";
    cout << "2. " << viewNames[1] << " (Extra Cost: " << viewCosts[1] << ")\n";
    cout << "3. " << viewNames[2] << " (Extra Cost: " << viewCosts[2] << ")\n";
    cout << "4. " << viewNames[3] << " (Extra Cost: " << viewCosts[3] << ")\n";
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedView = viewNames[choice - 1];
    totalCost += viewCosts[choice - 1];
    cout << "\nYou chose a **" << selectedView << "**. Cost added: " << viewCosts[choice - 1] << "\n";
    cout << "Your current total cost (per 24 hours) is: " << totalCost << "\n\n";

    cout << "--- 🛌 Room Type Selection ---\n";
    cout << "Which type of room do you want?\n";
    cout << "1. " << roomNames[0] << " (Extra Cost: " << roomCosts[0] << ")\n";
    cout << "2. " << roomNames[1] << " (Extra Cost: " << roomCosts[1] << ")\n";
    cout << "3. " << roomNames[2] << " (Extra Cost: " << roomCosts[2] << ")\n";
    cout << "4. " << roomNames[3] << " (Extra Cost: " << roomCosts[3] << ")\n";
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedRoom = roomNames[choice - 1];
    totalCost += roomCosts[choice - 1];
    cout << "\nYou chose a **" << selectedRoom << "**. Cost added: " << roomCosts[choice - 1] << "\n";
    cout << "Your current total cost (per 24 hours) is: " << totalCost << "\n\n";

    cout << "--- 🛏️ Bed Count Selection ---\n";
    cout << "How many beds do you need for the room?\n";
    cout << "1. " << bedNames[0] << " (Extra Cost: " << bedCosts[0] << ")\n";
    cout << "2. " << bedNames[1] << " (Extra Cost: " << bedCosts[1] << ")\n";
    cout << "3. " << bedNames[2] << " (Extra Cost: " << bedCosts[2] << ")\n";
    cout << "4. " << bedNames[3] << " (Extra Cost: " << bedCosts[3] << ")\n";
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedBed = bedNames[choice - 1];
    totalCost += bedCosts[choice - 1];
    cout << "\nYou chose a **" << selectedBed << "** room. Cost added: " << bedCosts[choice - 1] << "\n";
    cout << "Your current total cost (per 24 hours) is: " << totalCost << "\n\n";

    cout << "--- 🍽️ Food Option Selection ---\n";
    cout << "Do you want an all-inclusive food package?\n";
    cout << "1. " << foodNames[0] << " (Extra Cost: " << foodCosts[0] << ")\n";
    cout << "2. " << foodNames[1] << " (Extra Cost: " << foodCosts[1] << ")\n";
    choice = get_valid_input(1, 2, "Please enter 1 or 2: ");
    selectedFood = foodNames[choice - 1];
    totalCost += foodCosts[choice - 1];
    cout << "\nYou chose **" << selectedFood << "**. Cost added: " << foodCosts[choice - 1] << "\n";
    cout << "Your current total cost (per 24 hours) is: " << totalCost << "\n\n";

    cout << "--- ✨ Extra Service Selection ---\n";
    cout << "Do you want any extra service?\n";
    cout << "1. " << extraNames[0] << " (Extra Cost: " << extraCosts[0] << ")\n";
    cout << "2. " << extraNames[1] << " (Extra Cost: " << extraCosts[1] << ")\n";
    cout << "3. " << extraNames[2] << " (Extra Cost: " << extraCosts[2] << ")\n";
    cout << "4. " << extraNames[3] << " (Extra Cost: " << extraCosts[3] << ")\n";
    choice = get_valid_input(1, 4, "Please enter 1, 2, 3, or 4: ");
    selectedExtra = extraNames[choice - 1];
    totalCost += extraCosts[choice - 1];
    cout << "\nYou chose **" << selectedExtra << "**. Cost added: " << extraCosts[choice - 1] << "\n";
    cout << "Your current total cost (per 24 hours) is: " << totalCost << "\n\n";

    cout << "For how many days you want to book hotel?\n";
    cin >> days;
    finalCost = days * totalCost;

    cout << "\n==========================================\n";
    cout << "✅ BOOKING CONFIRMATION\n";
    cout << "   Check-in Date: " << C.checkInDate << "\n";
    cout << "   Total Days Booked: " << days << "\n";
    cout << "   Daily Cost: " << totalCost << "\n";
    cout << "   FINAL COST: " << finalCost << "\n";
    cout << "==========================================\n";

    ofstream fp("bookings.txt", ios::app);

    if (!fp) {
        cout << "\nERROR: Could not open 'bookings.txt' for writing.\n";
        return 1;
    }

    fp << "==========================================\n";
    fp << "       NEW HOTEL BOOKING                  \n";
    fp << "==========================================\n";

    fp << "Customer Name: " << C.name << "\n";
    fp << "Mobile Number: " << C.mobileNumber << "\n";
    fp << "ID Type:       " << C.idType << "\n";    
    fp << "ID Number:     " << C.idNumber << "\n";
    fp << "Check-in Date: " << C.checkInDate << "\n";

    fp << "\n--- Booking Summary ---\n";
    fp << "Star Rating:        " << selectedStar << "\n";
    fp << "View Type:          " << selectedView << "\n";
    fp << "Room Type:          " << selectedRoom << "\n";
    fp << "Bed Count:          " << selectedBed << "\n";
    fp << "Food Option:        " << selectedFood << "\n";
    fp << "Extra Services:     " << selectedExtra << "\n";
    fp << "Daily Cost:         " << totalCost << "\n";
    fp << "Total Days Booked:  " << days << "\n"; 
    fp << "FINAL BOOKING COST: " << finalCost << "\n";
    fp << "==========================================\n\n\n\n";

    fp.close();

    cout << "Booking confirmed\n";
    return 0;
}
