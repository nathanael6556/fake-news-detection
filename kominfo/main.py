import retrieve_news_detail, retrieve_news_list, prepare_dataset


if __name__ == "__main__":
    print("Retrieving news list")
    retrieve_news_list.retrieve(1, 2000, 12)

    print("Retrieving news details")
    retrieve_news_detail.retrieve()

    print("Preparing dataset")
    prepare_dataset.prepare()
    
    print("Done!")
