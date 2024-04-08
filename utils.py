from datetime import datetime

import requests

from database import get_db
from database.models import User


def create_user_from_json(json_data):
    user_data = json_data['results'][0]
    user = User(
        gender=user_data['gender'],
        title=user_data['name']['title'],
        first_name=user_data['name']['first'],
        last_name=user_data['name']['last'],
        street_number=user_data['location']['street']['number'],
        street_name=user_data['location']['street']['name'],
        city=user_data['location']['city'],
        state=user_data['location']['state'],
        country=user_data['location']['country'],
        postcode=user_data['location']['postcode'],
        latitude=float(user_data['location']['coordinates']['latitude']),
        longitude=float(user_data['location']['coordinates']['longitude']),
        timezone_offset=user_data['location']['timezone']['offset'],
        timezone_description=user_data['location']['timezone']['description'],
        email=user_data['email'],
        uuid=user_data['login']['uuid'],
        username=user_data['login']['username'],
        password=user_data['login']['password'],
        salt=user_data['login']['salt'],
        md5=user_data['login']['md5'],
        sha1=user_data['login']['sha1'],
        sha256=user_data['login']['sha256'],
        dob_date=datetime.fromisoformat(user_data['dob']['date']),
        dob_age=user_data['dob']['age'],
        registered_date=user_data['registered']['date'],
        registered_age=user_data['registered']['age'],
        phone=user_data['phone'],
        cell=user_data['cell'],
        id_name=user_data['id']['name'],
        id_value=user_data['id']['value'],
        picture_large=user_data['picture']['large'],
        picture_medium=user_data['picture']['medium'],
        picture_thumbnail=user_data['picture']['thumbnail'],
        nat=user_data['nat']
    )
    return user


def main():
    response = requests.get("https://randomuser.me/api/")
    json_data = response.json()

    user = create_user_from_json(json_data)

    session = next(get_db())
    session.add(user)
    session.commit()
    session.close()


if __name__ == '__main__':
    main()
