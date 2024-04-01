from Assignment2 import *

# Creating visitors and tickets
visitor1 = Visitor("Ahmed", "Alwahabi", 30, "UAE", Gender.MALE, "Ahmed@example.com")
activity1 = Activity("Sample Exhibition", Location.EXHIBITION_HALL, "2024-04-01", "2024-04-30")
visitor1.purchase_ticket(TicketType.ONLINE, activity1, TicketStatus.VALID, "yes")

activity2 = Activity("Historical Tour", Location.OUTDOOR_SPACE, "2024-05-15", "2024-05-16")
visitor1.purchase_ticket(TicketType.INPERSON, activity2, TicketStatus.VALID, "yes")

activity3 = Activity("Music Concert", Location.EXHIBITION_HALL, "2024-06-01", "2024-06-02")
visitor1.purchase_ticket(TicketType.ONLINE,  activity3, TicketStatus.VALID, "yes")

visitor2 = Visitor("Jane", "Doe", 25, "British", Gender.FEMALE, "jane@example.com")
activity4 = Activity("Art Exhibition", Location.PERMANENT_GALLERY, "2024-04-10", "2024-04-20")
visitor2.purchase_ticket(TicketType.ONLINE,  activity4, TicketStatus.VALID, "no")

activity5 = Activity("City Tour", Location.OUTDOOR_SPACE, "2024-05-20", "2024-05-21")
visitor2.purchase_ticket(TicketType.INPERSON, activity5, TicketStatus.VALID, "yes")

activity6 = Activity("Charity Event", Location.EXHIBITION_HALL, "2024-06-10", "2024-06-11")
visitor2.purchase_ticket(TicketType.ONLINE,  activity6, TicketStatus.VALID, "no")

# Creating guiders
guider1 = Guider("Alice", "Smith", 35, "Australian", Gender.FEMALE)
guider1.assign_tour(Tour("Art Walk", Location.PERMANENT_GALLERY, "2024-04-05", "2024-04-06", guider1))
guider1.assign_tour(Tour("Historical Sites Tour", Location.OUTDOOR_SPACE, "2024-05-25", "2024-05-26", guider1))
guider1.assign_tour(Tour("Nature Exploration", Location.OUTDOOR_SPACE, "2024-06-15", "2024-06-16", guider1))

guider2 = Guider("Bob", "Johnson", 40, "Canadian", Gender.MALE)
guider2.assign_tour(Tour("Art Appreciation Tour", Location.PERMANENT_GALLERY, "2024-04-15", "2024-04-16", guider2))
guider2.assign_tour(Tour("City Landmarks Tour", Location.OUTDOOR_SPACE, "2024-05-30", "2024-05-31", guider2))
guider2.assign_tour(Tour("Adventure Tour", Location.OUTDOOR_SPACE, "2024-06-20", "2024-06-21", guider2))

# Creating artists and artworks for each
artist1 = Artist("Michael", "Jordan", 50, "American", Gender.MALE, "Mic.Jordan")
artist1.create_artwork("The Jump", "1984-01-01", "Iconic basketball jump", Location.PERMANENT_GALLERY)
artist1.create_artwork("The Dunk", "1985-01-01", "Legendary basketball dunk", Location.PERMANENT_GALLERY)
artist1.create_artwork("The Shot", "1989-01-01", "Memorable buzzer-beater", Location.PERMANENT_GALLERY)

artist2 = Artist("Leonardo", "Da Vinci", 67, "Italian", Gender.MALE, "L.Davinci")
artist2.create_artwork("Mona Lisa", "1503-01-01", "Renowned portrait painting", Location.PERMANENT_GALLERY)
artist2.create_artwork("The Last Supper", "1495-01-01", "Famous religious painting", Location.PERMANENT_GALLERY)
artist2.create_artwork("Vitruvian Man", "1490-01-01", "Canonical drawing", Location.PERMANENT_GALLERY)

# Creating exhibitions
exhibition1 = Exhibition("Renaissance Art Exhibition", Location.EXHIBITION_HALL, "2024-04-01", "2024-04-30", "Renaissance Art")
exhibition1.add_artwork_to_exhibition(artist2.create_artwork("Vitruvian Man", "1490-01-01", "Canonical drawing", Location.PERMANENT_GALLERY))
exhibition1.add_artwork_to_exhibition(artist2.create_artwork("Mona Lisa", "1503-01-01", "Renowned portrait painting", Location.PERMANENT_GALLERY))
exhibition1.add_artwork_to_exhibition(artist2.create_artwork("The Last Supper", "1495-01-01", "Famous religious painting", Location.PERMANENT_GALLERY))

exhibition2 = Exhibition("Modern Art Exhibition", Location.EXHIBITION_HALL, "2024-05-01", "2024-05-31", "Modern Art")
exhibition2.add_artwork_to_exhibition(artist1.create_artwork("The Jump", "1984-01-01", "Iconic basketball jump", Location.PERMANENT_GALLERY))
exhibition2.add_artwork_to_exhibition(artist1.create_artwork("The Dunk", "1985-01-01", "Legendary basketball dunk", Location.PERMANENT_GALLERY))
exhibition2.add_artwork_to_exhibition(artist1.create_artwork("The Shot", "1989-01-01", "Memorable buzzer-beater", Location.PERMANENT_GALLERY))

# Creating tours
tour1 = Tour("Historical Tour", Location.OUTDOOR_SPACE, "2024-06-01", "2024-06-02", guider1)
tour2 = Tour("Nature Exploration", Location.OUTDOOR_SPACE, "2024-06-15", "2024-06-16", guider2)

# Creating events
event1 = Event("Charity Gala", Location.EXHIBITION_HALL, "2024-07-01", "2024-07-02", "Charity Foundation", EventPurpose.FUNDRAISING)
event2 = Event("Concert Night", Location.EXHIBITION_HALL, "2024-07-15", "2024-07-16", "Music Society", EventPurpose.CONCERT)

# Creating the catalog
museum_catalog = Catalog()

# Adding visitors, guiders, artists, artworks and activities to the catalog
museum_catalog.add_visitor_to_catalog(visitor1)
museum_catalog.add_visitor_to_catalog(visitor2)

museum_catalog.add_guider_to_catalog(guider1)
museum_catalog.add_guider_to_catalog(guider2)

museum_catalog.add_artist_to_catalog(artist1)
museum_catalog.add_artwork_to_catalog(artist2)


museum_catalog.add_artwork_to_catalog(artist1._Artist__artworks[0])
museum_catalog.add_artwork_to_catalog(artist1._Artist__artworks[1])
museum_catalog.add_artwork_to_catalog(artist1._Artist__artworks[2])
museum_catalog.add_artwork_to_catalog(artist2._Artist__artworks[0])
museum_catalog.add_artwork_to_catalog(artist2._Artist__artworks[1])
museum_catalog.add_artwork_to_catalog(artist2._Artist__artworks[2])

museum_catalog.add_exhibition_to_catalog(exhibition1)
museum_catalog.add_exhibition_to_catalog(exhibition2)

museum_catalog.add_tour_to_catalog(tour1)
museum_catalog.add_tour_to_catalog(tour2)

museum_catalog.add_event_to_catalog(event1)
museum_catalog.add_event_to_catalog(event2)

# MENU BASED INTERFACE

# Create a password that the guiders and admins will use to access the system

password_admin = "8827472Admin"
password_guider = "8737264Guider"

# a function for purchasing a ticket
def purchase_option(visitor):
    purchase_option = input("Do you want to view the catalog or purchase a ticket? Enter 'view' or 'purchase': ")
    if purchase_option == "view":
        museum_catalog.print_catalog()
    elif purchase_option == "purchase":
        museum_catalog.print_catalog()
        # Ask for ticket details and purchase
        ticket_activity = input("Enter the title of the activity for which you want to purchase a ticket: ")
        group_response = input("Are you in a group (yes/no): ")

        ticket = visitor.purchase_ticket(TicketType.ONLINE, Activity(ticket_activity, Location.EXHIBITION_HALL, "2024-04-01", "2024-04-30"), TicketStatus.VALID, group_response)
        print("Ticket purchased successfully!")
        visitor.print_tickets()

# Below are functions that we need for the admin menu
# Admin menu options
def admin_menu():
    print("\nAdmin Menu:")
    print("1. Add Visitor")
    print("2. Add Artist")
    print("3. Add Artwork")
    print("4. Add Exhibition")
    print("5. Add Event")
    print("6. Add Tour")
    print("7. View Catalog")
    print("8. Exit")

# Admin menu functionality
def admin_functionality(choice):
    if choice == "1":
        add_visitor()
    elif choice == "2":
        add_artist()
    elif choice == "3":
        add_artwork()
    elif choice == "4":
        add_exhibition()
    elif choice == "5":
        add_event()
    elif choice == "6":
        add_tour()
    elif choice == "7":
        museum_catalog.print_catalog()
    elif choice == "8":
        print("Exiting admin menu...")
    else:
        print("Invalid choice.")

# Add visitor function
def add_visitor():
    fname = input("Enter visitor's first name: ")
    lname = input("Enter visitor's last name: ")
    age = int(input("Enter visitor's age: "))
    nationality = input("Enter visitor's nationality: ")
    gender_input = input("Enter visitor's gender (Male/Female): ")
    gender = Gender.MALE if gender_input.lower() == "male" else Gender.FEMALE
    email = input("Enter visitor's email: ")

    new_visitor = Visitor(fname, lname, age, nationality, gender, email)
    museum_catalog.add_visitor_to_catalog(new_visitor)
    print(f"Visitor {fname} {lname} added successfully.")

# Add artist function
def add_artist():
    fname = input("Enter artist's first name: ")
    lname = input("Enter artist's last name: ")
    age = int(input("Enter artist's age: "))
    nationality = input("Enter artist's nationality: ")
    gender_input = input("Enter artist's gender (Male/Female): ")
    gender = Gender.MALE if gender_input.lower() == "male" else Gender.FEMALE
    social_media = input("Enter artist's social media handle: ")

    new_artist = Artist(fname, lname, age, nationality, gender, social_media)
    museum_catalog.add_artist_to_catalog(new_artist)
    print(f"Artist {fname} {lname} added successfully.")

# Add artwork function
def add_artwork():
    artist_id = input("Enter the ID of the artist for the artwork: ")
    title = input("Enter the title of the artwork: ")
    creation_date = input("Enter the creation date of the artwork (YYYY-MM-DD): ")
    historical_significance = input("Enter the historical significance of the artwork: ")
    location_input = input("Enter the location of the artwork (Permanent Gallery/Exhibition Hall/Outdoor Space): ")
    location_input = location_input.upper().replace(" ", "_")  # Convert to uppercase and replace space with underscore

    artist = None
    for a in museum_catalog._Catalog__artists:
        if a.get_artist_id() == artist_id:
            artist = a
            break

    if artist:
        new_artwork = artist.create_artwork(title, creation_date, historical_significance, location_input)
        museum_catalog.add_artwork_to_catalog(new_artwork)
        print(f"Artwork '{title}' by {artist.get_fname()} {artist.get_lname()} added successfully.")
    else:
        print("Artist not found.")

# Add exhibition function
def add_exhibition():
    title = input("Enter the title of the exhibition: ")
    start_date = input("Enter the start date of the exhibition (YYYY-MM-DD): ")
    end_date = input("Enter the end date of the exhibition (YYYY-MM-DD): ")
    theme = input("Enter the theme of the exhibition: ")
    location_input = input("Enter the location of the exhibition (Permanent Gallery/Exhibition Hall/Outdoor Space): ")
    location = location_input.upper().replace(" ", "_")

    new_exhibition = Exhibition(title, location, start_date, end_date, theme)
    museum_catalog.add_exhibition_to_catalog(new_exhibition)
    print(f"Exhibition '{title}' added successfully.")

# Add event function
def add_event():
    title = input("Enter the title of the event: ")
    start_date = input("Enter the start date of the event (YYYY-MM-DD): ")
    end_date = input("Enter the end date of the event (YYYY-MM-DD): ")
    organizer = input("Enter the organizer of the event: ")
    purpose = input("Enter the purpose of the event (Fundraising/Concert/Light Show): ")
    location_input = input("Enter the location of the event (Permanent Gallery/Exhibition Hall/Outdoor Space): ")
    location = location_input.upper().replace(" ", "_")

    new_event = Event(title, location, start_date, end_date, organizer, purpose)
    museum_catalog.add_event_to_catalog(new_event)
    print(f"Event '{title}' added successfully.")

# Add tour function
def add_tour():
    title = input("Enter the title of the tour: ")
    start_date = input("Enter the start date of the tour (YYYY-MM-DD): ")
    end_date = input("Enter the end date of the tour (YYYY-MM-DD): ")
    location_input = input("Enter the location of the event (Permanent Gallery/Exhibition Hall/Outdoor Space): ")
    location = location_input.upper().replace(" ", "_")
    tour_guide_id = input("Enter the ID of the tour guide: ")

    tour_guide = None
    for g in museum_catalog._Catalog__guiders:
        if g.get_guider_id() == tour_guide_id:
            tour_guide = g
            break

    if tour_guide:
        new_tour = Tour(title, location, start_date, end_date, tour_guide)
        museum_catalog.add_tour_to_catalog(new_tour)
        print(f"Tour '{title}' added successfully.")
    else:
        print("Tour guide not found.")

# Asking the user to introduce themselves
print("Welcome to the Louvre Museum!")
user_choice = input("Who are you?\n"
                    "  -Enter 1 if you're a visitor.\n"
                    "  -Enter 2 if you're a guider.\n"
                    "  -Enter 3 if you're an admin.\n"
                    "Your choice: ")

# Visitor
if user_choice == "1":
    visitor_type = input("Are you an old visitor or a new visitor? Enter 'old' or 'new': ")

    if visitor_type == "old":
        visitor_id = input("Please enter your visitor ID: ")
        # Search for the visitor in the catalog
        found_visitor = None
        for visitor in museum_catalog._Catalog__visitors:
            if visitor.get_visitor_id() == visitor_id:
                found_visitor = visitor
                break

        if found_visitor:
            print(f"Welcome back, {found_visitor.get_fname()}!")
            purchase_option(found_visitor)


    elif visitor_type == "new":
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        age = int(input("Enter your age: "))
        nationality = input("Enter your nationality: ")
        gender_input = input("Enter your gender (Male/Female): ")
        gender = Gender.MALE if gender_input.lower() == "male" else Gender.FEMALE
        email = input("Enter your email: ")

        # Create a new visitor object
        new_visitor = Visitor(fname, lname, age, nationality, gender, email)
        museum_catalog.add_visitor_to_catalog(new_visitor)
        print(f"Welcome, {new_visitor.get_fname()}! Your visitor ID is: {new_visitor.get_visitor_id()}")
        purchase_option(new_visitor)
    else:
        print("Invalid input. Please enter 'old' or 'new'.")

# Guider
elif user_choice == "2":
    guider_password = input("Please enter the guider password: ")
    if guider_password == password_guider:
        print("You are now logged in as a guider.")
        guider_id = input("Please enter your Guider ID: ")

        # Search for the guider in the catalog
        found_guider = None
        for guider in museum_catalog._Catalog__guiders:
            if guider.get_guider_id() == guider_id:
                found_guider = guider
                break

        if found_guider:
            print(f"Welcome, {found_guider.get_fname()}!")
            found_guider.print_guider_tours()
        else:
            print("Guider ID not found. Please try again.")
    else:
        print("Incorrect guider password. Access denied.")

# Admin
elif user_choice == "3":
    admin_password = input("Please enter the admin password: ")
    if admin_password == password_admin:
        print("You are now logged in as an admin.")
        while True:
            admin_menu()
            choice = input("Enter your choice (1-8): ")
            if choice == "8":
                print("Exiting admin menu...")
                break
            else:
                admin_functionality(choice)

    else:
        print("Incorrect admin password. Access denied.")
else:
    print("Invalid choice. Please enter a number between 1 and 3.")