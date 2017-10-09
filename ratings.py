"""Restaurant rating lister."""


def ask_user_input():
    """prompt user to enter new restaurant and rating, 
    return these values to the calling function
    """
    new_restaurant = raw_input("Enter a new restaurant:")

    new_rating = raw_input("Enter a new rating: ")
    return new_restaurant, new_rating

#Trying to add validation for the rating betwen 1 and 5:  
    # while True:
    #     if new_restaurant in range(1, 6):
            
    #     else:
    #         print "Enter a rating between 1 and 5"
    #     break



def read_ratings(file_path):
    """Given a file, prints ratings in alphabetical order by restaurant."""

    # Create empty dictionary.
    restaurant_ratings = {}

    # Open file. Create file object.
    with open(file_path) as text_file:

        # Iterate line-by-line over file object.
        for line in text_file:
            # Strip trailing white space.
            line = line.rstrip()
            # Unpack list of tuples.
            restaurant, rating = line.split(':')

            # Adding key-value pairs to dictionary.
            restaurant_ratings[restaurant] = rating

        return restaurant_ratings


def add_rating(restaurant_ratings):
    """Adds user restaurant and rating to dictionary."""

    restaurant, rating = ask_user_input()
    restaurant_ratings[restaurant] = rating

    # Sort dictionary. Iterate over key value pairs.
    for restaurant, rating in sorted(restaurant_ratings.items()):
        # Print restaurant and rating statement.
        print restaurant + " is rated at " + rating

    #add_user_rating(restaurant_ratings)

# Call function.
file_dictionary = read_ratings('scores.txt')
add_rating(file_dictionary)

