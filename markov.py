import mysql.connector

def calculate_letter_probabilities(text):
    letter_counts = {}
    total_letters = 0

    for char in text:
        if char.isalpha():  
            total_letters += 1
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    letter_probabilities = {letter: count / total_letters for letter, count in letter_counts.items()}
    return letter_probabilities

def save_to_database(letter_probabilities, connection):
    cursor = connection.cursor()

    for letter, probability in letter_probabilities.items():
        cursor.execute(
            "INSERT INTO markov (do, posle, prob) VALUES (%s, %s, %s)",
            (letter, "", probability)  
        )

    connection.commit()
    cursor.close()

if __name__ == "__main__":
    db_connection = mysql.connector.connect(
        host="localhost",
        user="daniil",
        password="1507",
        database="NikitinDM"
    )

    file_path = "pushkin.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        input_text = file.read()

    letter_probabilities = calculate_letter_probabilities(input_text)

    save_to_database(letter_probabilities, db_connection)

    db_connection.close()

