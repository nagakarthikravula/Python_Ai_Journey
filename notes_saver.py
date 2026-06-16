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
        for index,note in enumerate(notes):
            print(f"{index+1}. {note}")
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
        except ValueError:
            print("Invalid Input Type")
    else:
        print("No notes to delete")
        return notes
            

notes = load_notes()
notes = add_note(notes)
notes = add_note(notes)
print(notes)
view_notes(notes)
notes = delete_note(notes)
view_notes(notes)