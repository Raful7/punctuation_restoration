from bs4 import BeautifulSoup


class DataProcessor:
    # The folder to put the model data in
    he_data_folder_address = ''
    # The folder address to read the XML from
    xml_file_address = ''
    # The name of the XML file I want to read in.
    file_name = ''

    def __init__(self, data_folder_address: str, xml_file_address: str):
        """This method is the constructor. Used to initiate the object.
        Arguments:
            data_folder_address(str) - the address of the data folder we build.
            xml_file_address(str) - the name of the xml file we analyze
        """
        self.he_data_folder_address = data_folder_address
        self.xml_file_address = xml_file_address
        self.file_name = self.xml_file_address.split('\\')
        self.file_name = self.file_name[len(self.file_name)-1][:-4]
  
    def read_xml_file(self):
        """Reads XML file.
        Arguments:
            address(str) - the address to the xml file we want to read.
        Returns:
            bs4.BeautifulSoup - the data in the xml file.
        """
        # Reading the data inside the xml file to a variable under the name  data
        with open(self.xml_file_address, 'r', encoding="utf8") as f:
            data = f.read()
        bs_data = BeautifulSoup(data, 'xml')
        return bs_data

    # TODO:look again on this function+
    def remove_tag_with_extract(self, file_data: BeautifulSoup):
        """ Removes the meta tag from the document.
        Arguments:
            file_data(BeautifulSoup) - the XML file itself.
        Returns:
            BeautifulSoup - the repaired data.
        """
        meta_tag = file_data.meta.extract()
        return file_data

    def get_text_data(self, file_data: BeautifulSoup):
        """Returns the textual data from the tags after removing the ' and "\n".
        Arguments:
            file_data(BeautifulSoup) - the XML file itself.
        Returns:
            str. the textual data.
        """
        file_text = file_data.get_text()
        file_text = file_text.replace('\n', '')
        file_text = file_text.replace("\'", "")
        return file_text

    def organize_tuples(self, text_data_list: list):
        """ Organizes a list of tuples with the right indicator
        Arguments:
            text_data(str) - the raw data.
        Returns:
            list(tuple) - list of tuples.
        """
        text_data_indicators = []
        for i in range(len(text_data_list)):
            if text_data_list[i] != '' and text_data_list[i][-3:] != '...':
                # print(text_data_list[i])
                last_char = text_data_list[i][-1]
                # print(last_char)
                match last_char:
                    case ",":
                        text_data_list[i] = text_data_list[i][:len(
                            text_data_list[i])-1]
                        text_data_indicators.append(
                            (text_data_list[i], 'COMMA'))
                    case ".":
                        text_data_list[i] = text_data_list[i][:len(
                            text_data_list[i])-1]
                        text_data_indicators.append(
                            (text_data_list[i], 'PERIOD'))
                    case "?":
                        text_data_list[i] = text_data_list[i][:len(
                            text_data_list[i])-1]
                        text_data_indicators.append(
                            (text_data_list[i], 'QUESTION'))
                    case "!":
                        text_data_list[i] = text_data_list[i][:len(
                            text_data_list[i])-1]
                        text_data_indicators.append(
                            (text_data_list[i], 'EXCLAMATION'))
                    case _:
                        text_data_indicators.append((text_data_list[i], 'O'))
        return text_data_indicators

    def write_data(self, data: list):
        """Creates the file in the address and writes the data to the file.
        Arguments:
            data(List) - list of tuples. The word and the indicator.
            file_name(str) - the file name, to add it to the address.
        """
        f = open(self.he_data_folder_address +
                 self.file_name, "w", encoding="utf-8")
        for tuple_element in data:
            f.write(f"{tuple_element[0]}\t{tuple_element[1]}\n")
        f.close()

    def write_train_data(self, train_data: list):
        """Creates the file in the address and writes the train data to the file.
        Arguments:
            train_data(List) - list of tuples. The word and the indicator.
            file_name(str) - the file name, to add it to the address.
        """
        f = open(self.he_data_folder_address +
                 'train2023', "a", encoding="utf-8")
        for tuple_element in train_data:
            f.write(f"{tuple_element[0]}\t{tuple_element[1]}\n")
        f.close()

    def write_val_data(self, validation_data: list):
        """Creates the file in the address and writes the validation data to the file.
        Arguments:
            validation_data(List) - list of tuples. The word and the indicator.
            file_name(str) - the file name, to add it to the address.
        """
        f = open(self.he_data_folder_address +
                 'dev2023', "a", encoding="utf-8")
        for tuple_element in validation_data:
            f.write(f"{tuple_element[0]}\t{tuple_element[1]}\n")
        f.close()

    def write_test_data(self, test_data: list):
        """Creates the file in the address and writes the test data to the file.
        Arguments:
            test_data(List) - list of tuples. The word and the indicator.
            file_name(str) - the file name, to add it to the address.
        """
        f = open(self.he_data_folder_address +
                 'test2023', "a", encoding="utf-8")
        for tuple_element in test_data:
            f.write(f"{tuple_element[0]}\t{tuple_element[1]}\n")
        f.close()
  