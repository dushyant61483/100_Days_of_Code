#include <iostream>
#include <queue>
#include <stack>
using namespace std;

struct Node {
    int id;
    string name;
    int roomNo;
    Node* next;
};

struct Guest {
    int id;
    string name;
};

Node* head = nullptr;

int nextID = 1;

queue<int> freeRooms;

void addGuest(int id, string name, int room) {
    Node* newNode = new Node{id, name, room, nullptr};

    if (head == nullptr) head = newNode;
    else {
        Node* temp = head;
        while (temp->next != nullptr)
            temp = temp->next;
        temp->next = newNode;
    }
}

bool removeGuest(int id) {
    Node* temp = head;
    Node* prev = nullptr;

    while (temp != nullptr) {
        if (temp->id == id) {
            if (prev == nullptr) head = temp->next;
            else prev->next = temp->next;

            cout << "Checked out from Room " << temp->roomNo << endl;

            freeRooms.push(temp->roomNo);

            delete temp;
            return true;
        }
        prev = temp;
        temp = temp->next;
    }
    cout << "Guest not found\n";
    return false;
}

void showGuests() {
    if (!head) {
        cout << "No guests\n";
        return;
    }

    Node* temp = head;
    while (temp) {
        cout << "ID: " << temp->id
             << " Name: " << temp->name
             << " Room: " << temp->roomNo << endl;
        temp = temp->next;
    }
}

void showQueue(queue<Guest> q) {
    if (q.empty()) {
        cout << "No waiting guests\n";
        return;
    }

    while (!q.empty()) {
        Guest g = q.front();
        cout << "ID: " << g.id << " Name: " << g.name << endl;
        q.pop();
    }
}

void showFreeRooms(queue<int> q) {
    if (q.empty()) {
        cout << "No rooms available\n";
        return;
    }

    cout << "Available Rooms: ";
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;
}

int main() {
    cout<<"\n\n----------------Hotel Management System----------------\n\n";
    queue<Guest> q;
    stack<string> st;

    for (int i = 101; i <= 110; i++) {
        freeRooms.push(i);
    }

    int choice;
    string name;

    while (true) {

        cout << "\n1.Add Guest\n2.Assign Room\n3.Checkout\n4.Show Guests\n5.Show History\n6.Show Waiting\n7.Show Free Rooms\n8.Exit\n";
        cout<< "Enter Your Choice: ";
        if (!(cin >> choice)) {
            cout << "Invalid input! Try again.\n";
            cin.clear();
            cin.ignore(10000, '\n');
            continue;
        }

        if (choice == 1) {
            cout << "Enter Name: ";
            cin >> name;

            Guest g;
            g.id = nextID++;
            g.name = name;

            q.push(g);

            cout << "Added: " << g.name << " (ID: " << g.id << ")\n";

            st.push("Added " + name);
        }

        else if (choice == 2) {
            if (q.empty()) {
                cout << "There is no Guest in waiting list.\n";
                continue;
            }

            if (freeRooms.empty()) {
                cout << "No rooms available\n";
                continue;
            }

            Guest g = q.front();

            showFreeRooms(freeRooms);

            int room;
            cout << "Select room: ";
            cin >> room;

            queue<int> temp = freeRooms;
            bool found = false;

            while (!temp.empty()) {
                if (temp.front() == room) {
                    found = true;
                    break;
                }
                temp.pop();
            }

            if (!found) {
                cout << "Room not available, try again\n";
                continue;
            }

            queue<int> newQueue;
            while (!freeRooms.empty()) {
                if (freeRooms.front() != room)
                    newQueue.push(freeRooms.front());
                freeRooms.pop();
            }
            freeRooms = newQueue;

            q.pop();
            addGuest(g.id, g.name, room);

            cout << "Room " << room << " given to " << g.name << endl;
            st.push("Assigned " + g.name);
        }

        else if (choice == 3) {
            int id;
            cout << "Enter ID: ";
            cin >> id;

            if (removeGuest(id))
                st.push("Checkout ID " + to_string(id));
        }

        else if (choice == 4) {
            showGuests();
        }

        else if (choice == 5) {
            stack<string> temp = st;
            while (!temp.empty()) {
                cout << temp.top() << endl;
                temp.pop();
            }
        }

        else if (choice == 6) {
            showQueue(q);
        }

        else if (choice == 7) {
            showFreeRooms(freeRooms);
        }

        else if (choice == 8) {
            break;
        }

        else {
            cout << "Invalid choice! Try again.\n";
        }
    }
}
