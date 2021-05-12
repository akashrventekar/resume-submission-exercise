from collections import defaultdict



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
        "Please list your relevant university degree(s).": "Bachelors Of Engineering - Computer Science and Engineering | Masters of Scienc - Computer Science | Currently pursuing MBA",
        "Please provide a URL where we can download your resume and cover letter.": '<a href="https://akash-resume.s3.amazonaws.com/Akash+R+Ventekar.pdf<">link text</a>',
        "Can you provide proof of eligibility to work in the US?": "Yes",
    }

    if "Please solve this puzzle" in str(event['queryStringParameters']['d']):
        answers[str(event['queryStringParameters'][
                        'd'])] = return_output(input=str(event['queryStringParameters']['d']))
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain", },
        "body": answers[str(event['queryStringParameters'][
               'd'])]
    }


def convert_lol_final_result_string(lol):
    final_output_string = ""
    for i in range(len(lol)):
        final_output_string += "".join(lol[i])
        if i < len(lol) - 1:
            final_output_string += "\n"

    return final_output_string


def create_final_output(input_list):
    full_list = []
    my_list = [" "]
    char = "A"
    for i in range(len(input_list)):
        my_list.append(chr(ord(char[0]) + i))
    full_list.append(my_list)

    for i in range(len(input_list)):
        elements_list = ["-"] * (len(input_list) + 1)
        string = chr(ord(char[0]) + input_list[i] - 1)
        elements_list[0] = string
        elements_list[input_list[i]] = "="
        for j in range(len(input_list)):
            if i < j:
                elements_list[input_list[j]] = ">"
            elif i > j:
                elements_list[input_list[j]] = "<"
        full_list.append(elements_list[:])
        elements_list.clear()
    return (sorted(full_list))


def create_max_min_list(relationship_dict):
    final_max_min_list = []

    for key, value in relationship_dict.items():
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
            if key in relationship_dict.values():
                final_max_min_list.extend(temp_max_min_list[:])
            else:
                temp_max_min_list.extend(final_max_min_list)
                final_max_min_list = temp_max_min_list[:]
    return final_max_min_list


def return_output(input):
    input_variables = convert_string_to_list(input=input)

    relationship_dict = create_relationship_dict(input_variables)

    max_min_list = create_max_min_list(relationship_dict)

    list_of_lists_answer = create_final_output(input_list=max_min_list)

    return convert_lol_final_result_string(lol=list_of_lists_answer)


def convert_string_to_list(input):
    print(input.split(":")[1])
    input_variables = input.split(":")[1].splitlines()
    return input_variables[1:]


def create_relationship_dict(input_variables):
    relationship_dict = defaultdict()
    for i in range(1, len(input_variables)):
        if '>' in input_variables[i]:
            index = input_variables[i].index('>')
            relationship_dict[i] = index
        if '<' in input_variables[i]:
            index = input_variables[i].index('<')
            relationship_dict[index] = i
    return relationship_dict
