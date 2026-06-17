import json

def load_notes():
    try:
        with open("notes.json","r") as file:
            return (json.load(file))
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_notes(notes):
    with open("notes.json","w") as file:
        json.dump(notes,file,indent=4)

def add_note(notes):
    uip = input("Type a note: ")
    if uip:
        notes.append(uip)
        save_notes(notes)
        print("Note saved successfully!")
        return notes
    else:
        print("Note cannot be empty.")
        return notes

def view_notes(notes):
    if notes:
        print("Your Notes:")
        print("----------------------")
        for index,note in enumerate(notes,start=1):
            print(f"{index}. {note}")
        print("----------------------")
    else:
        print("No notes found.")

def delete_note(notes):
    view_notes(notes)
    if notes:
        try:
            ip = int(input("Enter a note number to delete: "))
            if ip >= 1 and ip <= len(notes):
                notes.pop(ip-1)
                save_notes(notes)
                print("Note deleted successfully!") 
                return notes
            else:
                print("Invalid note number.")
                return notes
        except ValueError:
            print("Invalid Input Type")
            return notes

    else:
        print("No notes to delete")
        return notes
            

def main():
    notes = load_notes()
    while True:
        i = input('''
========================================
        Notes Saver App
========================================
1. View Notes
2. Add Note
3. Delete Note
4. Exit
Enter your choice: 
''')
        if i == "1":
            view_notes(notes)
        elif i == "2":
            notes = add_note(notes)
        elif i == "3":
            notes = delete_note(notes)
        elif i == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
