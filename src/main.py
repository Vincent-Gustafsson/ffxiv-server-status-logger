from consumer import consume
from db_service import add_log

def main():
    consume(add_log)


if __name__ =="__main__":
    main()