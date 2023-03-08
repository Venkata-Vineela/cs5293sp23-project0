import argparse
import func

def main(url):
        # Download data
        incident_data = func.fetch(url)

        # Extract data
        incidents = func.extract(incident_data)

        func.database(incidents)
        # Create new database
#        db = te.insertion()

        #insert data
 #       te.insertion()

        #Print incident counts
#        te.insertion()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, help="Incident summary url.")
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

