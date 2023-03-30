import data_preperation
from data_preperation import DataProcessor
import glob
import re


def generate_files(files: list[str], train_precentage: float, val_precentage: float, test_precentage: float):
    """ Creates the training, validation and test files in order to train the model.
    Arguments:
        files(list[str]) - The addresses of the files  - 
        train_precentage(float) - the split precentage of the train
        val_precentage(float) - the split precentage of the validation
        test_precentage(float) - the split precentage of the test
    """
    train = round(train_precentage * len(files))
    val = round(val_precentage * len(files))
    test = round(test_precentage * len(files))
    counter = 1  # indicator of splitting the files
    for f in files:
        dp = DataProcessor(
            data_folder_address="./punctuation-restoration/data/he/", xml_file_address=f)
        xml_file = dp.read_xml_file()
        xml_file = dp.remove_tag_with_extract(file_data=xml_file)
        text_file = dp.get_text_data(file_data=xml_file)
        seperated_words = re.split(' ', text_file)
        list_of_words = dp.organize_tuples(text_data_list=seperated_words)
        # organize the train, validation and test files
        if counter <= train:
            dp.write_train_data(train_data=list_of_words)
            counter += 1
        elif counter > train and counter < (train + val):
            dp.write_val_data(validation_data=list_of_words)
            counter += 1
        else:
            dp.write_test_data(test_data=list_of_words)
            counter += 1


def main():
    files = glob.glob(
        'C:\\Users\\mrafi\\Desktop\\punctuation model\\he\\OpenSubtitles\\raw\\he\\**\\*\\*.xml', recursive=True)
    # Splits the data to: train, val, test
    train_precentage = 0.6
    val_precentage = 0.25
    test_precentage = 1 - train_precentage - val_precentage
    generate_files(files=files, train_precentage=train_precentage,
                   val_precentage=val_precentage, test_precentage=test_precentage)


if __name__ == "__main__":
    main()
