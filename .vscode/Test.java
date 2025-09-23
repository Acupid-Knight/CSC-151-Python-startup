
import java.io.*;
import java.util.Scanner;

// By implementing Serializable interface
// we make sure that state of instances of class CharacterSheet
// can be saved in a file.
class CharacterSheet implements Serializable {
    private static final long serialVersionUID = 1L;
    
    // Character stats
    int experience;    // starts at zero
    String char_name;
    String char_class;  // 'fighter' , "theif", etc
    String player_name;



    // CharacterSheet class constructor
    public CharacterSheet(int experience, String char_name, String char_class, String player_name) {
        this.experience = experience;
        this.char_name = char_name;
        this.char_class = char_class;
        this.player_name = player_name;
    }
}

public class Test {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // TODO: get all the info

        /*
        // 
        int experience;    // starts at zero
        String char_name;
        String char_class  // 'fighter' , "theif", etc
        String player_name;
        */
        // Ask the User to type the info
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the experience points (or 0): ");
        int exp = scanner.nextInt();
        scanner.nextLine();  // Consume newline

        System.out.print("Enter the player name: ");
        String player_name = scanner.nextLine();

        System.out.print("Enter the character name: ");
        String char_name = scanner.nextLine();

        System.out.print("Enter the character class(fighter, theif, mage): ");
        String char_class = scanner.nextLine();
        // cleanup
        scanner.close();

        // Make the object
     CharacterSheet tracker = new CharacterSheet(exp, char_name, char_class, player_name);
        // Write it to a file
        System.out.println("Writing file...");
        // Serializing 'tracker'
        FileOutputStream fos = new FileOutputStream("char_sheet.data");
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(tracker);

        // De-serializing 'tracker'
        FileInputStream fis = new FileInputStream("char_sheet.data");
        ObjectInputStream ois = new ObjectInputStream(fis);
     CharacterSheet new_charsheet =  (CharacterSheet) ois.readObject(); // down-casting object
        System.out.println("Reading file...");
        System.out.println("Char Name: " + new_charsheet.char_name + ", xp: " + new_charsheet.experience);
        System.out.println("Char Class: " + new_charsheet.char_class);
        System.out.println("player: " + new_charsheet.player_name);
        // TODO: print all the other data 
        // closing streams
        oos.close();
        ois.close();
    }
}

