from patterns.csv_utils import Ride
from patterns import save_file

#Builder pattern 
def build_print_report(rides):
    txt_report = create_content(rides)
    save_file.create_file(txt_report,"financial-report.txt")

def create_content(rides):
    builder = [_create_headers("Taxi Report"), _create_table_headers()]
    for ride in rides:
        builder.append(_add_ride(ride))
    return "".join(builder)

def _create_headers(title: str):
    return "\t \t \t" + title + "\t \t \t"


def _create_table_headers():
    return """\n
            \t TaxiID
            \t Pickup time
            \t Dropoff time
            \t Passenger count
            \t Trip Distance
            \t Total amount"""

def _add_ride(ride):
    return "".join([
        "\n",
        "\t" + ride.taxi_id,
        "\t" + ride.pick_up_time.isoformat(),
        "\t" + ride.drop_of_time.isoformat(),
        "\t" + ride.passenger_count,
        "\t" + ride.trip_distance,
        "\t" +_format_amount(ride.tolls_amount),
    ])


def _format_amount(amount):
    if amount < 0:
        return "(" + amount+ ")"
    return str(amount)
