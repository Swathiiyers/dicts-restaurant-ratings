"""Restaurant rating lister."""

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

        # Sort dictionary. Iterate over key value pairs.
        for restaurant, rating in sorted(restaurant_ratings.items()):
            # Print restaurant and rating statement.
            print restaurant + " is rated at " + rating


# Call function.
read_ratings('scores.txt')
