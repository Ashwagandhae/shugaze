import re
from openai import OpenAI
from secret import the_key


def get_similar_shoes(shoe_name: str):
    client = OpenAI(api_key=the_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a shoe expert. When given a shoe model, return a Python list of similar shoes. These shoes could be of the same brand but they do not need to be. Ideally, it should reflect a number of different brands too. (make sure these shoes would be listed on stockx). do not include any introductory lines, just give me the actual list. and make sure this list can be easily saved as an array in python",
            },
            {
                "role": "user",
                "content": f"Give me 5 similar shoes to {shoe_name}.",
            },  # this is where user input comes in...
        ],
    )

    # extracts the response. response is a string.
    response_content = response.choices[0].message.content

    # function to extract the individual shoe names from response.
    def extract_quoted_words(text):
        # find words inside double quotes
        quoted_words = re.findall(r'"([^"]*)"', text)
        return quoted_words

    # puts the similar shoes in an array/list...
    similar_shoe_list = extract_quoted_words(response_content)

    # shoe list should be fed into divo's program to find price data on those shoes; predict future shoe prices.
    return similar_shoe_list


def get_similar_shoes_test(shoe_name: str):
    if shoe_name == "Nike Free RN 5.0 2020":
        return [
            "Nike Flex Experience RN 8",
            "HOKA Mach 5",
            "Adidas Adizero SL",
            "On Cloudswift 3",
        ]
    elif shoe_name == "Adidas Samba OG":
        return [
            "New Balance 574",
            "Adidas Gazelle",
            "Nike Dunk Low",
            "Nike Cortez",
            "Puma Suede Classic",
        ]
    elif shoe_name == "New Balance 2002R":
        return [
            "New Balance 574 ",
            "Nike Zoom Vomero",
            "Nike Air Max 90",
            "Adidas Yeezy Boost 700",
            "Asics Gel-Kayano",
        ]
    else:
        return []
