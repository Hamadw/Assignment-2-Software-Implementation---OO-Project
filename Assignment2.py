from enum import Enum
from datetime import datetime

class Gender(Enum):
   MALE = 'Male'
   FEMALE = 'Female'

class Location(Enum):
   PERMANENT_GALLERY = 'Permanent Gallery'
   EXHIBITION_HALL = 'Exhibition Hall'
   OUTDOOR_SPACE = 'Outdoor Space'

class ActivityType(Enum):
   EXHIBITION = 'Exhibition'
   TOUR = 'Tour'
   EVENT = 'Event'

class TicketType(Enum):
   ONLINE = 'Online'
   INPERSON = 'In-Person'

class TicketStatus(Enum):
   VALID = 'Valid'
   EXPIRED = 'Expired'

class EventPurpose(Enum):
   FUNDRAISING = 'Fundraising'
   CONCERT = 'Concert'
   LIGHT_SHOW = 'Light Show'

class Person:
    """ Class to represent a person"""

    # Constructor
    def __init__(self, fname, lname, age, nationality, gender):
        self._fname = fname
        self._lname = lname
        self._age = age
        self._nationality = nationality
        self._gender = gender

    # Setters and Getters
    def set_fname(self, fname):
        self._fname = fname

    def get_fname(self):
        return self._fname

    def set_lname(self, lname):
        self._lname = lname

    def get_lname(self):
        return self._lname

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_nationality(self, nationality):
        self._nationality = nationality

    def get_nationality(self):
        return self._nationality

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

class Visitor(Person):
    """Class to represent visitors"""
    visitor_count = 0

    # constructor
    def __init__(self, fname, lname, age, nationality, gender, email):
        super().__init__(fname, lname, age, nationality, gender)
        Visitor.visitor_count += 1
        self.__visitor_id = f"V{Visitor.visitor_count}"  # Generate visitor ID automatically
        self.__email = email
        self.__ticket_purchases = []

    # setters and getters
    def get_visitor_id(self):
        return self.__visitor_id

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    # A function that allows the visitor to purchase a ticket,
    # this function shows the composition relationship between the visitor and ticket
    def purchase_ticket(self, ticket_type, activity, ticket_status, group):
        if 18 <= self._age <= 60 and group != "yes":
            ticket_price = 63
        elif self._age < 18 or self._age > 60:
            ticket_price = 0
        elif group == "yes":
            ticket_price = 63*0.5  # Default price for other categories

        ticket = Ticket(ticket_type, ticket_price, datetime.now(), activity, ticket_status)
        ticket.calculate_final_price()
        self.__ticket_purchases.append(ticket)
        return ticket


    # this function that prints all tickets purchased by the visitor
    def print_tickets(self):
        if not self.__ticket_purchases:
            print("No tickets purchased.")
        else:
            print("Ticket details for the customer:")
            for i, ticket in enumerate(self.__ticket_purchases, 1):
                print(f"Ticket {i}:")
                print(f"  Type: {ticket.get_ticket_type()}")
                print(f"  Price: {ticket.get_price()}")
                print(f"  Purchase Time: {ticket.get_purchase_time()}")
                print(f"  Activity Details: {(ticket.get_activity_details()).get_title()}")
                print(f"  Ticket Status: {ticket.get_ticket_status()}")
                print()


class Guider(Person):
    """Class to represent guider"""
    guider_count = 0

    # constructor
    def __init__(self, fname, lname, age, nationality, gender):
        super().__init__(fname, lname, age, nationality, gender)
        Guider.guider_count += 1
        self.__guider_id = f"G{Guider.guider_count}"  # Generate guider ID automatically
        self.__assigned_tours = []

    # setters and getters
    def set_guider_id(self, guider_id):
        self.__guider_id = guider_id

    def get_guider_id(self):
        return self.__guider_id

    # Assign tours to the guider
    def assign_tour(self, tour):
        self.__assigned_tours.append(tour)

    # Print the details of the guiders their assigned tours
    def print_guider_tours(self):
        print("Guider Details:")
        print(f"Name: {self.get_fname()} {self.get_lname()}")
        print(f"Age: {self.get_age()}")
        print(f"Nationality: {self.get_nationality()}")
        print(f"Gender: {self.get_gender()}")
        print(f"Guider ID: {self.__guider_id}")

        if self.__assigned_tours:
            print("Assigned Tours:")
            for i, tour in enumerate(self.__assigned_tours, 1):
                print(f"Tour {i}:")
                print(f"  Title: {tour.get_title()}")
                print(f"  Location: {tour.get_location().value}")
                print(f"  Start Date: {tour.get_start_date()}")
                print(f"  End Date: {tour.get_end_date()}")
                print()
        else:
            print("The guider is free!")

class Artist(Person):
    """Class to represent artist"""
    artist_count = 0
    Guider.guider_count += 1

    # constructor
    def __init__(self, fname, lname, age, nationality, gender, social_media):
        super().__init__(fname, lname, age, nationality, gender)
        Artist.artist_count += 1
        self.__artist_id = f"A{Artist.artist_count}"  # Generate artist ID automatically
        self.__social_media = "@" + social_media
        self.__email = self.get_fname() + "." + self.get_lname() + "@lv.ac.ae"
        self.__artworks = []

    # setters and getters
    def set_artist_id(self, artist_id):
        self.__artist_id = artist_id

    def get_artist_id(self):
        return self.__artist_id

    def set_social_media(self, social_media):
        self.__social_media = social_media

    def get_social_media(self):
        return self.__social_media

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    # function that creates an artwork for an artist
    # This function shows the composition relationship between the artist and artwork
    def create_artwork(self, title, creation_date, historical_significance, location):
        artwork = ArtWork(title, self, creation_date, historical_significance, location)
        self.__artworks.append(artwork)
        return artwork

    # this function prints all artworks done by the artist
    def print_artworks(self):
        if not self.__artworks:
            print(f"The artist {self.get_fname()}, {self.get_lname()} has no artworks.")
        else:
            print("Artworks by", self.get_fname(), self.get_lname() + ":")
            for artwork in self.__artworks:
                print("- Title:", artwork.get_title())
                print("  Creation Date:", artwork.get_creation_date())
                print("  Historical Significance:", artwork.get_historical_significance())
                print("  Location:", artwork.get_location().value)

    # This function prints the contact details of the artist (email / social media)
    def print_contact_details(self):
        print("Contact Details for", self.get_fname(), self.get_lname() + ":")
        print("- Email:", self.__email)
        print("- Social Media:", self.__social_media)

class ArtWork:
    """Class to represent artworks"""

    # constructor
    def __init__(self, title, artist, creation_date, historical_significance, location):
        self.__title = title
        self.__artist = artist
        self.__creation_date = creation_date
        self.__historical_significance = historical_significance
        self.__location = location

    # setters and getters
    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_artist(self, artist):
        self.__artist = artist

    def get_artist(self):
        return self.__artist

    def set_creation_date(self, creation_date):
        self.__creation_date = creation_date

    def get_creation_date(self):
        return self.__creation_date

    def set_historical_significance(self, historical_significance):
        self.__historical_significance = historical_significance

    def get_historical_significance(self):
        return self.__historical_significance

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

class Ticket:
    """Class to represent tickets"""

    # constructor
    def __init__(self, ticket_type, price, purchase_time, activity_details, ticket_status):
        self.__ticket_type = ticket_type
        self.__price = price
        self.__purchase_time = purchase_time
        self.__activity_details = activity_details  # This attribute represent an object from the activity class
        self.__ticket_status = ticket_status

    # setters and getters
    def set_ticket_type(self, ticket_type):
        self.__ticket_type = ticket_type

    def get_ticket_type(self):
        return self.__ticket_type

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_purchase_time(self, purchase_time):
        self.__purchase_time = purchase_time

    def get_purchase_time(self):
        return self.__purchase_time

    def set_activity_details(self, activity_details):
        self.__activity_details = activity_details

    def get_activity_details(self):
        return self.__activity_details

    def set_visitor_information(self, visitor_information):
        self.__visitor_information = visitor_information

    def get_visitor_information(self):
        return self.__visitor_information

    def set_ticket_status(self, ticket_status):
        self.__ticket_status = ticket_status

    def get_ticket_status(self):
        return self.__ticket_status

    # this function calculates the final price of the ticket with VAT
    def calculate_final_price(self):
        vat = 0.05  # 5% VAT
        final_price = self.__price * (1 + vat)
        self.__price = final_price
        return self.__price

    # this function prints the details of the activity for a certain ticket
    def print_activity_details(self):
        print("Activity Details:")
        print("  Title:", self.__activity_details.get_title())
        print("  Location:", self.__activity_details.get_location().value)
        print("  Start Date:", self.__activity_details.get_start_date())
        print("  End Date:", self.__activity_details.get_end_date())

class Activity:
    """Class to represent activities"""

    # constructor
    def __init__(self, title, location, start_date, end_date):
        self._title = title
        self._location = location
        self._start_date = start_date
        self._end_date = end_date

    # setters and getters
    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location

    def set_start_date(self, start_date):
        self._start_date = start_date

    def get_start_date(self):
        return self._start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def get_end_date(self):
        return self._end_date

    def calculate_duration_in_days(self):
        start_date = datetime.strptime(self._start_date, '%Y-%m-%d')
        end_date = datetime.strptime(self._end_date, '%Y-%m-%d')
        duration = (end_date - start_date).days
        print("Duration in days:", duration)

class Exhibition(Activity):
    """Class to represent exhibitions"""

    # constructor
    def __init__(self, title, location, start_date, end_date, theme):
        super().__init__(title, location, start_date, end_date)
        self.__featured_artworks = []
        self.__theme = theme

    # setters and getters
    def set_theme(self, theme):
        self.__theme = theme

    def get_theme(self):
        return self.__theme

    # this function adds an artwork to the exhibition
    def add_artwork_to_exhibition(self, artwork):
        self.__featured_artworks.append(artwork)

    # this function removes an artwork from the exhibition
    def remove_artwork_from_exhibition(self, artwork):
        self.__featured_artworks.remove(artwork)

    # this function prints the featured artworks in the exhibition
    def print_featured_artworks(self):
        if not self.__featured_artworks:
            print("There is no featured artworks in this exhibition.")
        else:
            print("Featured Artworks in the Exhibition:")
            for artwork in self.__featured_artworks:
                print("- Title:", artwork.get_title())
                print("  Artist:", artwork.get_artist().get_fname(), artwork.get_artist().get_lname())
                print("  Creation Date:", artwork.get_creation_date())
                print("  Historical Significance:", artwork.get_historical_significance())
                print("  Location:", artwork.get_location().value)

class Tour(Activity):
    """Class to represent tours"""

    # constructor
    def __init__(self, title, location, start_date, end_date, guider):
        super().__init__(title, location, start_date, end_date)
        self.__guider = guider

    # setters and getters
    def set_guider(self, guider):
        self.__guider = guider

    def get_guider(self):
        return self.__guider

class Event(Activity):
    """Class to represent events"""

    # constructor
    def __init__(self, title, location, start_date, end_date, organizer, purpose):
        super().__init__(title, location, start_date, end_date)
        self.__organizer = organizer
        self.__purpose = purpose

    # setters and getters
    def set_organizer(self, organizer):
        self.__organizer = organizer

    def get_organizer(self):
        return self.__organizer

    def set_purpose(self, purpose):
        self.__purpose = purpose

    def get_purpose(self):
        return self.__purpose

class Catalog:
    """Class that represents the visitor, artists, guiders, artworks and the activities such as exhibitions, events, and tours in the museum"""

    # Constructor
    def __init__(self):
        self.__visitors = []
        self.__guiders = []
        self.__artists = []
        self.__artworks = []
        self.__exhibitions = []
        self.__tours = []
        self.__events = []

    # Add a visitor
    def add_visitor_to_catalog(self, visitor):
        self.__visitors.append(visitor)

    # Remove a visitor
    def remove_visitor_to_catalog(self, visitor):
        if visitor in self.__visitors:
            self.__visitors.remove(visitor)
        else:
            print(f"({visitor.get_visitor_id()}) visitor is not in the catalog.")

    # Add an artist
    def add_artist_to_catalog(self, artist):
        self.__artists.append(artist)

    # Remove an artist
    def remove_artist_to_catalog(self, artist):
        if artist in self.__artists:
            self.__artists.remove(artist)
        else:
            print(f"({artist.get_visitor_id()}) artist is not in the catalog.")

    # Add a guider
    def add_guider_to_catalog(self, guider):
        self.__guiders.append(guider)

    # Remove a guider
    def remove_guider_to_catalog(self, guider):
        if guider in self.__guiders:
            self.__guiders.remove(guider)
        else:
            print(f"({guider.get_guider_id()}) guider is not in the catalog.")

    # add an artwork
    def add_artwork_to_catalog(self, artwork):
        self.__artworks.append(artwork)

    # remove an artwork
    def remove_artwork_to_catalog(self, artwork):
        if artwork in self.__artworks:
            self.__artworks.remove(artwork)
        else:
            print(f"({artwork.get_title()}) artwork is not in the catalog.")

    # add an exhibition
    def add_exhibition_to_catalog(self, exhibition):
        self.__exhibitions.append(exhibition)

    # remove an exhibition
    def remove_exhibition_to_catalog(self, exhibition):
        if exhibition in self.__exhibitions:
            self.__exhibitions.remove(exhibition)
        else:
            print(f"({exhibition.get_title()}) exhibition is not in the catalog.")

    # Add a tour
    def add_tour_to_catalog(self, tour):
        self.__tours.append(tour)

    # Remove a tour
    def remove_tour_to_catalog(self, tour):
        if tour in self.__tours:
            self.__tours.remove(tour)
        else:
            print(f"({tour.get_title()}) tour is not in the catalog.")

    # Add an event
    def add_event_to_catalog(self, event):
        self.__events.append(event)

    # Remove an event
    def remove_event_to_catalog(self, event):
        if event in self.__events:
            self.__events.remove(event)
        else:
            print(f"({event.get_title()}) event is not in the catalog.")

    def print_catalog(self):
        print("The exhibitions in the museum:")
        for i, exhibition in enumerate(self.__exhibitions, 1):
            print(f"{i}. Title: {exhibition.get_title()}")
            print(f"   Location: {exhibition.get_location()}")
            print(f"   Start Date: {exhibition.get_start_date()}")
            print(f"   End Date: {exhibition.get_end_date()}")
            print(f"   Theme: {exhibition.get_theme()}")
            print()

        print("The events in the museum:")
        for i, event in enumerate(self.__events, 1):
            print(f"{i}. Title: {event.get_title()}")
            print(f"   Location: {event.get_location()}")
            print(f"   Start Date: {event.get_start_date()}")
            print(f"   End Date: {event.get_end_date()}")
            print(f"   Organizer: {event.get_organizer()}")
            print(f"   Purpose: {event.get_purpose()}")
            print()

        print("The tours in the museum:")
        for i, tour in enumerate(self.__tours, 1):
            print(f"{i}. Title: {tour.get_title()}")
            print(f"   Location: {tour.get_location()}")
            print(f"   Start Date: {tour.get_start_date()}")
            print(f"   End Date: {tour.get_end_date()}")
            print(f"   Guide: {tour.get_guider().get_fname()} {tour.get_guider().get_lname()}")
            print()

    def print_visitors(self):
        print("The visitors in the museum:")
        for i, visitor in enumerate(self.__visitors, 1):
            print(f"{i}. Visitor ID: {visitor.get_visitor_id()}")
            print(f"   Name: {visitor.get_fname()} {visitor.get_lname()}")
            print(f"   Age: {visitor.get_age()}")
            print(f"   Nationality: {visitor.get_nationality()}")
            print(f"   Gender: {visitor.get_gender().value}")
            print(f"   Email: {visitor.get_email()}")
            print()

    def print_guiders(self):
        print("The guiders in the museum:")
        for i, guider in enumerate(self.__guiders, 1):
            print(f"{i}. Guider ID: {guider.get_guider_id()}")
            print(f"   Name: {guider.get_fname()} {guider.get_lname()}")
            print(f"   Age: {guider.get_age()}")
            print(f"   Nationality: {guider.get_nationality()}")
            print(f"   Gender: {guider.get_gender().value}")
            print()

    def print_artists(self):
        print("The artists in the museum:")
        for i, artist in enumerate(self.__artists, 1):
            print(f"{i}. Guider ID: {artist.get_artist_id()}")
            print(f"   Name: {artist.get_fname()} {artist.get_lname()}")
            print(f"   Age: {artist.get_age()}")
            print(f"   Nationality: {artist.get_nationality()}")
            print(f"   Gender: {artist.get_gender().value}")
            print()