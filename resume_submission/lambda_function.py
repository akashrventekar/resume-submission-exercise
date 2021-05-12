from collections import defaultdict
from typing import List, Dict


def lambda_handler(event, context):
    answers = {
        "Please provide a URL where we can download the source code of your resume submission web service.": "https://github.com/akashrventekar/resume-submission-exercise",
        "What is your full name?": "Akash Rajendra Ventekar",
        "Please return OK so that I know your service works.": "OK",
        "What is your email address?": "akashrventekar@gmail.com",
        "Please provide a phone number we can use to reach you.": "(256) 468-9279",
        "Which position are you applying for?": "Senior Software Engineer, Exchange",
        "How many years of software development experience do you have?": "6+",
        "How did you hear about this position?": "LinkedIn",
        "Please list your relevant university degree(s).": "Bachelors Of Engineering - Computer Science and Engineering | Masters of Science - Computer Science | Currently pursuing MBA",
        "Please provide a URL where we can download your resume and cover letter.": 'https://akash-resume.s3.amazonaws.com/Akash+R+Ventekar.pdf',
        "Can you provide proof of eligibility to work in the US?": "Yes",
    }

    if "Please solve this puzzle" in str(event['queryStringParameters']['d']):
        answers[str(event['queryStringParameters'][
                        'd'])] = solve_puzzle(input=str(event['queryStringParameters']['d']))
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain", },
        "body": answers[str(event['queryStringParameters'][
                                'd'])]
    }


def solve_puzzle(input: str) -> str:
    puzzle_details_list = extract_puzzle_details(input=input)

    relationship_dict = create_relationship(input=puzzle_details_list)

    desc_sorted_list = create_sorted_list(relationship=relationship_dict)

    solved_puzzle_list = create_final_output_list(input=desc_sorted_list)

    return solved_puzzle_string(input=solved_puzzle_list)


def extract_puzzle_details(input: str) -> List:
    '''
        TC: O(n)
        SC: O(n)
    '''
    input_variables = input.split(":")[1].splitlines()
    return input_variables[1:]


def create_relationship(input: List) -> Dict:
    '''
        TC: O(n)
        SC: O(n)
        This function will create a relationship dictionary with greater item as the key and smaller item as value
    '''
    relationship_dict = defaultdict()
    for i in range(1, len(input)):
        if '>' in input[i]:
            index = input[i].index('>')
            relationship_dict[i] = index
        if '<' in input[i]:
            index = input[i].index('<')
            relationship_dict[index] = i
    return relationship_dict


def create_sorted_list(relationship: Dict):
    '''
        TC: O(n^2)
        SC: O(n)
        This will create relationship between all items and sort it in Descending order
    '''
    final_max_min_list = []

    for key, value in relationship.items():
        temp_max_min_list = []
        if len(final_max_min_list) == 0:
            final_max_min_list.append(key)
            final_max_min_list.append(value)
        elif key in final_max_min_list and value not in final_max_min_list:
            index_key = final_max_min_list.index(key)
            final_max_min_list = final_max_min_list[:index_key + 1] + [value] + final_max_min_list[
                                                                                index_key + 1:]
        elif value in final_max_min_list and key not in final_max_min_list:
            index_value = final_max_min_list.index(value)
            final_max_min_list = final_max_min_list[:index_value] + [key] + final_max_min_list[
                                                                            index_value:]
        elif key in final_max_min_list and value in final_max_min_list:
            continue
        else:
            temp_max_min_list.append(key)
            temp_max_min_list.append(value)
            if key in relationship.values():
                final_max_min_list.extend(temp_max_min_list[:])
            else:
                temp_max_min_list.extend(final_max_min_list)
                final_max_min_list = temp_max_min_list[:]
    return final_max_min_list

def create_final_output_list(input: List) -> List[List]:
    '''
        TC: O(n^2)
        SC: O(n^2)
    '''
    full_list = []
    my_list = [" "]
    char = "A"
    for i in range(len(input)):
        my_list.append(chr(ord(char[0]) + i))
    full_list.append(my_list)

    for i in range(len(input)):
        elements_list = ["-"] * (len(input) + 1)
        string = chr(ord(char[0]) + input[i] - 1)
        elements_list[0] = string
        elements_list[input[i]] = "="
        for j in range(len(input)):
            if i < j:
                elements_list[input[j]] = ">"
            elif i > j:
                elements_list[input[j]] = "<"
        full_list.append(elements_list[:])
        elements_list.clear()
    return (sorted(full_list))

def solved_puzzle_string(input: List[List]) -> str:
    '''
           TC: O(n^2)
           SC: O(n)
       '''
    final_output_string = ""
    for i in range(len(input)):
        final_output_string += "".join(input[i])
        if i < len(input) - 1:
            final_output_string += "\n"

    return final_output_string
