# app.py

from bs4 import BeautifulSoup

# load in from html_tasks directory

# function to iterate over all the file names
file_name = "test_data.html"

# iterate this taks through each html doc in the 
    
def handle_app_data(file_name: str):
    """handle the applications from a single html

    :param file_name: route to html file
    :type file_name: str
    """
    
    with open(file_name, "r") as file:
        soup_obj = BeautifulSoup(file, 'html.parser')
    
    def get_app_elements(soup_obj: BeautifulSoup) -> list:
        """Generate the application card element fromthe raw html in the soup object.

        :param soup_obj: soup object that has the simplify page loaded.
        :type soup_obj: BeautifulSoup
        :return: 
        :rtype: _type_
        """
        return soup_obj.find_all(attrs={"data-testid":"application-card"})

    def strip_single_app_card(app_card,
                                keys: list = ["title", 
                                            "comapny",
                                            "location",
                                            "date_opened"],
                            archived: bool = False) -> dict:
        """This function generates the data associated with a single application 
        card. This is run after the find_all command is run on all the raw data.

        :param app_card: raw text to parse to grab the data.
        :type app_card: bs4.element.Tag
        :param keys: keys to match the static data to, defaults to ["title", "comapny", "location", "date_opened"]
        :type keys: list, optional
        :param archived: is this from the archived html?, defaults to False
        :type archived: bool, optional
        :return: data that represents a single app card
        :rtype: dict
        """
        # print(app_card)
        raw_text_list = app_card.text.split('\n')
        # print(raw_text_list)
        stripped_text = []
        for d in raw_text_list: # fixed length
            # if non empty string after being stripped
            if d and d.strip(): 
                stripped_text.append(d.strip().lower())
        
        print(stripped_text)
        # take first three and fifth element :2, 3
        static_data = stripped_text[:3] + [stripped_text[4]]
        
        application_dict = dict(zip(keys, static_data))
            
        # sub-problem: assign bool to each level
        def assign_status_levels():
            status_levels = ["applied", "screen","interview","offer"]
            for i, status in enumerate(status_levels):
                statuses_to_check = status_levels[:i] + status_levels[i+1:]
                
                # index of this status in the main data
                target_index = stripped_text.index(status)
                try:
                    # date exists after status?
                    if stripped_text[target_index+1] not in statuses_to_check:
                        application_dict[status] = 1
                    else:
                        application_dict[status] = 0
                except IndexError:
                    application_dict[status] = 0
        
        assign_status_levels() 
        
        application_dict["archived"] = 1 if archived else 0
        
        return application_dict

    def convert_dicts_to_list(data: list[dict]):
        """convert list of dicts to list of lists with a header.
        
        :param data: data to switch to table form
        :type data: list[dict]
        :return: list of lists in table form
        :rtype: list[list]
        """
        # to have single header row and 
        table_csv_list = []
        
        headers = list(data[0].keys())
        headers_str = [str(h) for h in headers]
        
        table_csv_list.append(headers_str)
        
        for d in data: # list of dicts
            row_data = list(d.values())
            
            row_data_str = [str(d) for d in row_data]
            
            table_csv_list.append(row_data_str)
        
        return table_csv_list
        
    def build_csv(data: list[list], 
                write_mode: str = "a"):
        """build csv from the raw data

        :param data: table list of
        :type data: list[list]
        :param write_mode: write mode for the opening of the file, defaults to "a"
        :type write_mode: str, optional
        """
        
        with open("output.csv", write_mode) as built_csv:
            for line in data:
                line_str = ','.join(line) + '\n'
                built_csv.write(line_str)

    def add_to_db():
        # add this to a DB of the currnet applications, don't overwrite, but add new ones
        pass
    
    app_elements = get_app_elements(soup_obj)
    # print(app_elements[0]) # TODO works here
    
    app_elements_stripped = [strip_single_app_card(elem) 
                            for elem in app_elements]
    
    tabled_data = convert_dicts_to_list(app_elements_stripped)
    
    build_csv(tabled_data)

# iterate through all files
handle_app_data(file_name)